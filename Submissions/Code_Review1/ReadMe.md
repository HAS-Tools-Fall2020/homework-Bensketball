# Benjamin Mitchell's Code (Bensketball)
## `10/9/2020`
## Code review #1

### *Hello Camillo! (unless I am confused on how the GitHub chart works! XD)  So... Hello Partner!

___
### Table of Contents:
0. [ Instructions](#ins)
1. [ Your Code Review](#rev)
2. [ My Python Code(s)](#cod)

___
<a name="ins"></a>
## How to run my code:
`Run my code! Done!
`
Just kidding, I can walk you through what I have created here.

First off, the folder you copied to your computer should be the folder titled 'Code_Review1' found in my 'Submissions' folder of GitHub Repo.  Contained in this folder is my python code title 'mitchell_HW7.py' via the instructions on GitHub.  There should also be an empty folder called graphs and an empty The website to this GitHub can be found [here](https://github.com/HAS-Tools-Fall2020/homework-Bensketball/tree/master/Submissions/Code_Review1).  If you go to this website, you will find many helpful links to run my code.  The steps are below:

###### Step #1:
Download the daily streamflow data for station *09506000 Verde River Near Camp Verde* from the USGS NWIS [mapper](https://maps.waterdata.usgs.gov/mapper/).  Make sure your click the 'Daily Data' link after selecting the gage number so that the model is up to date with the latest data to help make the short term forecasts.
   - Parameter 00060 Discharge (mean)
   - Start date = 1989-01-01
   - End date = 2020-10-10 (Saturday this week)
   - Select 'tab separated'

Save a text file in the folder titled 'data' and title this text file 'streamflow_week7.txt'.  The name chosen is critical to my code.

P.S. There is already a text file titled 'streamflow_week7_temp.txt' in the 'data' folder.  This text file is missing this Friday and Saturday.  This is why you are updating the data. :)

###### Step #2:
Run my code.  Make sure that the filename in the beginning reads like this:
```python
filename = 'streamflow_week7.txt'
filepath = os.path.join('data', filename)
print(os.getcwd())
print(filepath)
```

Also, there is something weird about my code that I should warn you about.  You may get an error that reads like the output below:
```python
~\miniconda3\envs\hastools\lib\site-packages\scipy\linalg\basic.py in lstsq(a, b, cond, overwrite_a, overwrite_b, check_finite, lapack_driver)
   1221             raise LinAlgError("SVD did not converge in Linear Least Squares")
   1222         if info < 0:
-> 1223             raise ValueError('illegal value in %d-th argument of internal %s'
   1224                              % (-info, lapack_driver))
   1225         resids = np.asarray([], dtype=x.dtype)

ValueError: illegal value in 4-th argument of internal None
```
If you get this type of error, just run the code a second time.  I have been getting this error every other time I run my code, but it seems to fix itself every time I run it a second time.  I hope it does not effect your ability to use the code.

~ Thank you!  Please grade my code in the section below:
___
<a name="rev"></a>
### Your Code Review
##### Fill in the question(s) below from GitHub assignment.
##### *Feel free to change up this space for your review of my code!  You do not need to follow my formatting.

1. First check below to see who your partner is.

2. Clone their repo to your computer. You can find their repo by going to the [main GitHub organization page](https://github.com/HAS-Tools-Fall2020) for this class.

3. Review their code following the code_review_rubric.md instructions in the starter_codes folder. You should provide your comments and scores in the spaces they have provided for you in their ReadMe.md file in the Code_Review1 folder of their GitHub submissions folder.

  This is the space provided.  Feel free to change up this space for your review of my code!  You do not need to follow my formatting.

  **Code Review by Camilo Salcedo**

  Hi Ben. Thank you for your straightforward and complete instructions. You can find my review for your code below, and the forecasted values in the section you defined also below. It was a very nice to review your code :) .

  *General Comments*

  - The instructions you sent me were pretty straightforward and complete. Moreover, they included the solution to every possible error that would come out when running the code.

  - Your code runned easily, and the forecast values were given explicitely through a print statement.

  - Your approach of analyzing the log of data rather than the raw data seems very promising.

  - The resulting graphs gave additional information to the forecast results, and they were nice.

  - PEP8 standards were respected along the code.

  - You created a function to perform the forecasts, using the use of a loop, which was really good. However, you didn't use the corresponding doc-strings to documentate the function.

  - In your code, I changed your datafile name to ''streamflow_week7.txt' in line 22 according to your instructions. In addition, I created the folder _graphs_ because it didn't exist in your Submissions folder. 

  *Additional Ideas and Improvement Opportunities in Coding*
  Some ideas and tips that could help you to improve your code are described below:

  -  The comments you used in your code were very helpful. However, be careful with the spelling. You can find below a list of some spelling mistakes I found on your comments.

  Line 3: Perdiction
  Line 100: altrenatievely
  Line 100: calcualte
  Line 168: follwed
  Line 172: useing
  Line 172: fuction
  Line 184: becuase

  - Most of your variables were expressive, and followed PEP8 standards in the use of lower cases and underscores. Be careful with using short names like _pred_ (line 178), because out of context it should not be as expressive as required.

  In addition, when you use variables in a loop, you could use more expressive varibles.

  As an example, in line 170 you defined the variable _week_before_ to represent the mean flow of the previous week. Then, when you started the loop, you used the variable _week_bef_ to save the temporal values along the cycle. My recommendation is to use a name that tells the reader that this will be a temporal variable to be used within a loop. A good example could be _week_before_iter_ or _week_before_i_.

  - When creating a function, don't forget to use the doc-strings to documentate the function. As an extra benefit for your code-users, if they are lost with the use of your function, they could use _help_ to display your doc-strings and understand it better.

  - Be careful with white spaced recommended by PEP8 standards. For example, when you used a comment of one single line, you should leave a white space before it. This didn't occur in line 172.

  - When using Auto Regressive models, it is important to let the user know how many shifts did you use. As a recommendation, this could be a nice print to add to your code.

  - *Suggestion*: In the code block between lines 69 and 75, you could extract the training period by using directly the start date and the end date of your period as strings rather than indexes.

  To achieve this, you could use the format 'YYYY-MM-DD', and the loc function of dataframes. As an example, you could use either of the following lines:

  train = flow_weekly.loc['2013-12-01':'2019-08-25']
  train = flow_weekly['2013-12-01':'2019-08-25']

  In this way, you don't have to spend time looking for the indexes that correspond to the dates you want to use as training period.

  - *Suggestion*: In your function to make the predictions, you could save the forecasted values to use them in further postprocessing exercises such as graphs. In this sense, you could save them either within a new array of forecasted values, or as part of your dataframe.

  If you want to save them as part of your dataframe, the first thing you could do is to create a list of dates as strings, corresponding to the weeks you are going to include in your forecast. As an example:

  forecast_week=['2020-10-19','2020-10-26','2020-11-02']

  Then, using the _append_ function, you can add the most recent forecast to your dataframe. The code should look as follows:

  flow_weekly.append(pd.Series({'flow':pred},index=flow_weekly.columns, name=forecast_week[i]))

  Where _i_ corresponds to the index you used in the loop, and _pred_ to the variable in which you perform the forecast.

  *Review Rubric*

  | *Criteria*  | *Points* | *Comments* |
  | *Readability* | 2  |You didn't use any Doc-strings. For the rest, your code was very readable.|
  | *Style*| 3 |You used PEP8 Standards. Please take a look on some minor situations in which PEP8 were not used accurately described above.|
  | *Code Awesome*| 3 |Your code was succint, clean and pretty easy to understand and execute.  |

4. Follow the instructions they have provided in their ReadMe.md file to run their script and generate their 4 forecast values.

5. Enter all four values (the two regression forecasts and the two forecast values into the ReadMe.md file of your partners repo.

  My regression forecasts are the same as my forecast values!  Please just right each number twice. :)

  ***Regression Forecasts:***

  |  | Regression Forecasts | Forecast Values|
  |  Week # 1 | 70.38075136717578|70.38|
  |  Week # 2 | 77.9522111429154 |77.95|

##### Ben: I rounded your forecast to two decimal places.

6. Enter the two forecast values into the lastname.csv file for your partner. Remember you are entering their forecast for them this week, not your own!

My excel is titled *'mitchell.csv'*.  It can be found [here](https://github.com/HAS-Tools-Fall2020/forecasting/tree/master/forecast_entries) or [here](https://github.com/HAS-Tools-Fall2020/forecasting/blob/master/forecast_entries/mitchell.csv) for your convenience.

___
<a name="cod"></a>
## My Python Code(s):

##### The Python code can be found [here](../Code_Review1/mitchell_HW7.py).  It can also be found the folder you downloaded.  It was derived from this code [here](../../Orig_Starter_Codes_BM/week6_matplotlib_starter.py).


Finally, if the code works there should be a graph below:

![g-AR](../Code_Review1/graphs/AR.png "AR")

###### ~Thank you!
