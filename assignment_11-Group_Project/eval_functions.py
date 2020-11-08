# %%
import os
import numpy as np
import pandas as pd
from glob import glob
import dataretrieval.nwis as nwis
import datetime

# %% Group Functions

def getstrm_wbs(station_id,end_date):
    """Get stream flow from 
    https://waterdata.usgs.gov/nwis/.
    ---------------------------------
    This function download streamflow. It needs 
    as input the station id number and the end date of data.
    Dataset start on 1989-01-01.
    ---------------------------------
    Parameters:
    station_id = list of string numbers
    end_date = string date as yyyy-mm-dd
    ----------------------------------
    Outputs:
    lastNames = dataframe with streamflow values and dates
    """
    start_date = '1989-01-01'
    flow_data = nwis.get_record(sites=station_id, service='dv',
                          start=start_date, end=end_date,
                          parameterCd='00060')
    flow_data.columns = ['flow', 'code', 'site_no']
    flow_data = flow_data.rename_axis("datetime")
    flow_data['datetime'] = pd.to_datetime(flow_data.index)
    return(flow_data)


def add_yymmdd(flow_data):
    """Add year,week,day columns to data 
    ---------------------------------
    This function adds year,week,day 
    colummns to data to facilitate computation
    ---------------------------------
    Parameters:
    data = dataframe data
    ----------------------------------
    Outputs:
    flow_data = dataframe with extra columns
    """

    #flow_data['datetime'] = pd.to_datetime(flow_data.index)
    flow_data['datetime'] = pd.to_datetime(flow_data.index)
    flow_data['year'] = pd.DatetimeIndex(flow_data.index).year
    flow_data['month'] = pd.DatetimeIndex(flow_data.index).month
    flow_data['day'] = pd.DatetimeIndex(flow_data.index).day
    flow_data['dayofweek'] = pd.DatetimeIndex(flow_data.index).dayofweek
    return(flow_data)


# Building a function for our Linear Regression Model
def mono_reg_mod(test_weeks):
    """Linear Regression Model data being offset only once.
    test weeks = natural log streamflow laged by 1 week (x values)
    test weeks = natural log streamflow (y values)
    """
    reg_model = LinearRegression()
    x_val_model1 = test_weeks['log_flow_tm1'].values.reshape(-1, 1)  # Testing values
    y_val_model1 = test_weeks['log_flow'].values  # Testing values
    reg_model.fit(x_val_model1, y_val_model1)  # Fit linear model
    coeff_det1 = np.round(reg_model.score(x_val_model1, y_val_model1), 7)  # r^2
    b = np.round(reg_model.intercept_, 7)  # Intercept
    m = np.round(reg_model.coef_, 7)  # Slope
    print('coefficient of determination:', np.round(coeff_det1, 7))
    # Intercept and the slope (Final equation) y= mx + b
    print('Final equation is y1 = :', m[:1], 'x + ', b)
    return(b,m,reg_model,coeff_det1)


# Building a function for our Linear Regression Model
def poly_reg_mod(test_weeks):
    """Linear Regression Model with data being offset on two separate occasions.
    test weeks = natural log of streamflow laged by 1 & 2 weeks (x values)
    test weeks = natural log of streamflow (y values)
    """
    poly_model = LinearRegression()
    x_val_model2 = test_weeks[['log_flow_tm1', 'log_flow_tm2']]  # Testing values
    y_val_model2 = test_weeks['log_flow']  # Testing values
    poly_model.fit(x_val_model2, y_val_model2)  # Fit linear model
    coeff_det2 = np.round(poly_model.score(x_val_model2, y_val_model2), 7)  # r^2
    c = np.round(poly_model.intercept_, 7)  # Intercept
    a = np.round(poly_model.coef_, 7)  # Slope(s)
    print('coefficient of determination:', np.round(coeff_det2, 7))
    # Intercept and the slope (Final equation) y= a1*x1 + a2*x2 + c
    print('Final equation is y2 = :', a[:1], 'x1 + ', a[1:2], 'x2 + ', c)
    return(c,a,poly_model,coeff_det2)


# Building a function for flow prediction outside of the AR model
def real_prediction(indexnumber, last_week_flow, last2_week_flow=None):
    """This function is prepping the linear regression model to be
    multiplied by a correction factor to bring it down to a more
    reasonable value for the forecast of week 1 and week 2.
    """
    if indexnumber == 0 and last2_week_flow is None:
        rp = (model.intercept_ + model.coef_[indexnumber] * last_week_flow)
    if indexnumber == 1:
        rp = (model2.intercept_ + model2.coef_[0] * last_week_flow +
              model2.coef_[indexnumber] * last2_week_flow)
    if indexnumber != 0 and indexnumber != 1:
        print('The index number =', indexnumber, 'is not valid. Enter 0 or 1.')
    return rp


# Building a function to produce our two week flow predictions
# using linaral model1 with only one data offsets
def flow_predic_mono(b, m, num_of_weeks, week_b4, forecast_weeks):
    """This function produces predicted flow values using coefficients provided
    by an Liner Autoregressive Model with only one data offset.
    'b' is the y-intersept and 'm' is the slope.
    'num_of_weeks' is how many weeks you would like to loop the model for.
    'week_b4' is the natural log flow of a known flow and
    'forecast_weeks' is a list of dates that you are predicting for.
    """
    week_b4_i = week_b4
    pred_i = np.zeros((num_of_weeks, 1))
    for i in range(1, num_of_weeks + 1):
            log_flow_pred_i = b + m[:1] * week_b4_i
            flow_pred_i = math.exp(log_flow_pred_i)
            pred_i[i-1] = flow_pred_i
            week_b4_i = log_flow_pred_i
    flow_predictions_lin = pd.DataFrame(pred_i, index = forecast_weeks,
                                        columns=["Predicted_Flows_Lin:"])
    return flow_predictions_lin


# Building a function to produce our two week flow predictions
# using linaral model2 with multiple data offsets
def flow_predic_poly(c, a, num_of_weeks, week_b4, forecast_weeks):
    """This function produces predicted flow values using coefficients provided
    by an Liner Autoregressive Model with two different data offsets.
    'c' is the y-intersept and 'a' is a list of two slopes provided by the model.
    'num_of_weeks' is how many weeks you would like to loop the model for.
    'week_b4' is the natural log flow of a known flow and
    'forecast_weeks' is a list of dates that you are predicting for.
    """
    week_b4_i = week_b4
    pred_i = np.zeros((num_of_weeks, 1))
    for i in range(1, num_of_weeks + 1):
            log_flow_pred_i = c + a[1] * week_b4_i + a[0] * (week_b4_i)
            flow_pred_i = math.exp(log_flow_pred_i)
            pred_i[i-1] = flow_pred_i
            week_b4_i = log_flow_pred_i
    flow_predictions_poly = pd.DataFrame(pred_i, index = forecast_weeks,
                                         columns=["Predicted_Flows_Poly:"])
    return flow_predictions_poly


# Building a function to produce our two week flow predictions
def week_prediction_all(flow, m, b, week_pred, end, prev_wks):
    """This function needs the stream flow data (flow), the intersection
    and slope values from AR model (m, b), and range of weeks you want to
    consider for weekly forecast (prev_wks and end). To indicate the week
    to forecast include the week number (week_pred = 1 or week_pred = 2)
    We are using the mean value of the data range you select - the standard
    deviation of the same data range
    """
    Corr_fact1 = 0.2
    #Corr_fact1 = 0.4*flow['log_flow'][no_weeks - prev_wks:no_weeks-end].std()
    #Corr_fact1 = flow['log_flow'][no_weeks-end] / flow['log_flow'][no_weeks-(end-1)]
    flow_range_value = flow['log_flow'][no_weeks-prev_wks:no_weeks-end].mean() -0.25*flow['log_flow'][no_weeks - prev_wks:no_weeks-end].std()
    prediction = math.exp((b + m * flow_range_value))*(1-Corr_fact1) # dryness of this year
    print('Week', week_pred, 'forecast using model is:', prediction,'Correction factor:',Corr_fact1)
    return prediction,Corr_fact1

# %% Class functions
def getLastNames():
    """Get classlist of last names.
    ---------------------------------
    This function takes no input and returns the list of
    students' last names in the class.  This makes it easy to
    access the class list from any script.
    ---------------------------------
    Parameters:
    none
    ----------------------------------
    Outputs:
    lastNames = list of strings
                contains students's last names
    """
    lastNames = ['ferre', 'fierro', 'hsieh', 'hull', 'kahler',
                 'lau', 'marcelain', 'marcovecchio', 'medina',
                 'mitchell', 'narkhede', 'neri', 'noonan',
                 'pereira', 'ridlinghaver', 'salcedo',
                 'schulze', 'stratman', 'tadych']
    return lastNames


def getFirstNames():
    """Get classlist of first names.
    ---------------------------------
    This function takes no input and returns the list of
    students' first names in the class.  This makes it easy to
    access the class list from any script.
    ---------------------------------
    Parameters:
    none
    ----------------------------------
    Outputs:
    firstNames = list of strings
                 contains student's first names
    """
    firstNames = ['Ty', 'Lourdes', 'Diana', 'Quinn',
                  'Abigail', 'Alcely', 'Richard',
                  'Alexa', 'Xenia', 'Ben', 'Shweta', 'Patrick',
                  'Jill', 'Mekha', 'Jake', 'Camilo',
                  'Scott', 'Adam', 'Danielle']
    return firstNames


def weekDates(weekNumber):
    """Compute the one and two week forecasts using model.
    ---------------------------------
    This function takes no input and returns the list of
    students' first names in the class.  This makes it easy to
    access the class list from any script.
    ---------------------------------
    Parameters:
    weekNumber = integer
                 number indicating the week of the semester
    ----------------------------------
    Outputs:
    startDate = string
                contains start date of forecast week
    stopDate = string
               contains end date of forecast week
    """

    datefile = os.path.join('..', 'Seasonal_Foercast_Dates.csv')
    forecast_dates = pd.read_csv(datefile,
                                 index_col='forecast_week')

    startDate = forecast_dates.loc[weekNumber, 'start_date']
    stopDate = forecast_dates.loc[weekNumber, 'end_date']
    return startDate, stopDate


def write_bonus(bonus_names, weeknum):
    """" This function needs week forecast (week_no) and the
    list of student's names (list_names) you want to give bonus
    points for this week """
    file_listB = glob(os.path.join('../weekly_results', 'bonus*.csv'))
    temp = pd.read_csv(file_listB[0], index_col='name')
    bonus = pd.DataFrame(data=np.zeros(len(temp)),
                         index=temp.index,
                         columns=['points'])
    del(temp)
    bonus.loc[bonus_names, 'points'] = 1
    filename = 'bonus_week' + str(weeknum) + '.csv'
    bonus_file = os.path.join('../weekly_results', filename)
    bonus.to_csv(bonus_file)
    print("Work done :)")

# Week 10 additions:


def student_csv(lastname):
    """ Reads the .cvs student file as a dataframe.
    ---------------------------------
    Parameters:
    lastname = string
               list of student's last name.
    ---------------------------------
    Returns:
    file_df = DataFrame
              contains student's forecast entries.
    """
    filename = lastname + '.csv'
    filepath = os.path.join('..', 'forecast_entries', filename)
    print(filepath)
    file_df = pd.read_csv(filepath, index_col='Forecast #')
    return file_df


def simpleRMSE(prediction, observation, decimals):
    """ Calculates the Root Mean Square Error (RMSE) of a dataset.
    ---------------------------------
    Parameters:
    prediction = DataFrame, array or list
                 A prediction dataset.
    observation = DataFrame, array or list
                 A observation dataset with the same length
                 that the prediction dataset.
    decimals = Integer
               Number of decimals in the result.
    ---------------------------------
    Returns:
    rmse = Float
    """
    rmse = (((prediction - observation) ** 2).mean()
            ** 0.5).round(decimals)
    return rmse

# %%