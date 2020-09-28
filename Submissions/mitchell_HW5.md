# Benjamin Mitchell
## `9/27/2020`
## Homework #5

___
<a name="grd"></a>
# ***Grade***
___


___
### Table of Contents:
0. [ Grade](#grd)
1. [ Questions](#qns)
2. [ Discharge Estimation](#est)
3. [ Python Code(s)](#cod)
4. [ Appendices & Graphs](#apd)
5. [ Works Cited](#cit)

___
<a name="qns"></a>
## Assignment Questions

##### The Python code used to answer the questions below can be found [here](../assignment_5/week5_questions_BM.py).

1. Provide a summary of the data frames properties.
- What are the column names?
- What is its index?
- What data types do each of the columns have?

**Ans:**
```
(a) agency_cd, site_no, datetime, flow, code, year, month, day.
(b) 0, 1, 2, 3, 4, 5, 6, 7
```

```python
# Question #1c

# type(data)
data.dtypes
```

**Output:**
```
(c)
agency_cd     object
site_no        int64
datetime      object
flow         float64
code          object
year           int32
month          int32
day            int32
dtype: object
```

2. Provide a summary of the flow column including the min, mean, max, standard deviation and quartiles.

```python
#Question #2

# data
# print(data)
# print(data[['datetime']])
flow = data["flow"]
# print(flow)
print('min:', '\n', flow.min())
print('mean:', '\n', flow.mean())
print('max:', '\n', flow.max())
print('std:', '\n', flow.std())
print('quantile:', '\n', flow.quantile())
# print(mean_data)

data['flow'].describe()
```

**Output:**
```
count    11592.000000
mean       345.630461
std       1410.832968
min         19.000000
25%         93.700000
50%        158.000000
75%        216.000000
max      63400.000000
Name: flow, dtype: float64
```

3. Provide the same information but on a monthly basis. (Note: you should be able to do this with one or two lines of code)

```python
# Question #3

# print(data)
# mon_flow = data[["month","flow"]]
# print(mon_flow)
# data["datetime":[2]]
# print('min:', '\n', data.min())
# data_test = data[(datetime[:,1]==9), 3]
# data["datetime"]
i=0
# print(range(len(data)))
# print(data.flow[data.month == (12)].describe())
for i in range(1, 13):
        # print(data['flow'])
        print(i)
        print(data.flow[data.month == (i)].describe())
```

**Output:**
```
1
count      992.000000
mean       706.320565
std       2749.153983
min        158.000000
25%        202.000000
50%        219.500000
75%        292.000000
max      63400.000000
Name: flow, dtype: float64
2
count      904.000000
mean       925.252212
std       3348.821197
min        136.000000
25%        201.000000
50%        244.000000
75%        631.000000
max      61000.000000
Name: flow, dtype: float64
3
count      992.000000
mean       941.731855
std       1645.803872
min         97.000000
25%        179.000000
50%        387.500000
75%       1060.000000
max      30500.000000
Name: flow, dtype: float64
4
count     960.000000
mean      301.240000
std       548.140912
min        64.900000
25%       112.000000
50%       142.000000
75%       214.500000
max      4690.000000
Name: flow, dtype: float64
5
count    992.000000
mean     105.442339
std       50.774743
min       46.000000
25%       77.975000
50%       92.950000
75%      118.000000
max      546.000000
Name: flow, dtype: float64
6
count    960.000000
mean      65.998958
std       28.966451
min       22.100000
25%       49.225000
50%       60.500000
75%       77.000000
max      481.000000
Name: flow, dtype: float64
7
count     992.000000
mean       95.571472
std        83.512343
min        19.000000
25%        53.000000
50%        70.900000
75%       110.000000
max      1040.000000
Name: flow, dtype: float64
8
count     992.000000
mean      164.354133
std       274.464099
min        29.600000
25%        76.075000
50%       114.000000
75%       170.250000
max      5360.000000
Name: flow, dtype: float64
9
count     956.000000
mean      172.688808
std       286.776478
min        36.600000
25%        88.075000
50%       120.000000
75%       171.250000
max      5590.000000
Name: flow, dtype: float64
10
count     961.000000
mean      146.168991
std       111.779072
min        69.900000
25%       107.000000
50%       125.000000
75%       153.000000
max      1910.000000
Name: flow, dtype: float64
11
count     930.000000
mean      205.105376
std       235.673534
min       117.000000
25%       156.000000
50%       175.000000
75%       199.000000
max      4600.000000
Name: flow, dtype: float64
12
count      961.000000
mean       337.097815
std       1097.280926
min        155.000000
25%        191.000000
50%        204.000000
75%        228.000000
max      28700.000000
Name: flow, dtype: float64
```

4. Provide a table with the 5 highest and 5 lowest flow values for the period of record. Include the date, month and flow values in your summary.

```python
# Question 4

data['flow'].nlargest(5)
data['flow'].nsmallest(5)
```

**Output:**
```
1468    63400.0
1511    61000.0
2236    45500.0
5886    35600.0
2255    30500.0
Name: flow, dtype: float64
8582    19.0
8583    20.1
8581    22.1
8580    22.5
8584    23.4
Name: flow, dtype: float64
```

5. Find the highest and lowest flow values for every month of the year (i.e. you will find 12 maxes and 12 mins) and report back what year these occurred in.

**Ans:**
`
`

![flow_data9_lst.png](../assignment_4/graphs/flow_data9_1st.png "All September Data 1st half")

![flow_data9_lst.png](../assignment_4/graphs/flow_data9_2nd.png "All September Data 2nd half")

`Some weird stuff right?  The first half is nothing, but that second half is fascinating.  It seems that on the 30th of September, the value center around 90 and 120, generally.  Interesting for future guesses is all.  I made some graphs just about this September too.  Not sure what you wanted here:
`

![flow_data92020_lst.png](../assignment_4/graphs/flow_data92020_1st.png "All September Data 1st half")

![flow_data92020_lst.png](../assignment_4/graphs/flow_data92020_2nd.png "All September Data 2nd half")

`It depends on how to slice the 1st and 2nd half, but at the beginning of September there was a trend downwards and then on the 9th there was a strong shift upwards do to a rainstorm.  This was followed by a trend back downwards and we seem to remain it in for now.
`

6. Provide a list of historical dates with flows that are within 10% of your week 1 forecast value. If there are none than increase the %10 window until you have at least one other value and report the date and the new window you used.

**Ans:**
`
`
___
<a name="est"></a>
## Estimation4 Explanation

For this weeks estimate (4), I decided to use and transform a prewritten python code using Visual Studio Code.  The python code section I wrote, allowed me to create serval histograms for all data under the flow of 400 and in the months September, October, November, and December.  By isolating this part of the total data ('flow_data'), I was able to run computations to make my predictions.  For my estimate, I took the mean of all the data in each month and also took the lowest value I could find in each months given histogram.  For example look at the chart below:

![g9](../assignment_4/graphs/g9.png "All September Data")

As you can see, in September, the smallest "bin" filled in with data is from 0 to 40.  I took the flow 40 as the first guess in the month of September, took 40 and averaged it with the mean for this month, 132.6.  This gives 86.3 and I used this for the two "middle" weeks of the month.  The final September guess was the mean or 132.6.  I did this for all months after this.  I thought since there is an average trend to be dry for a bit and then shoot up because of snowmelt, why not guess in a similar patter.  I am hopeful!

The graph below was used for my weekl1 and week2 guesses:

![flow_202009](../assignment_4/graphs/flow_202009.png "flow from 9/5/2020 to 9/19/2020")

I was able to do some simple liner interpolation with the first three points trending downwards.

___
<a name="cod"></a>
## My Python Code(s)4:

The Python Code, created in Visual Studio Code (VSC), can be found [here](../assignment_4/week4_numpy_starter_BM.py).  This python code was crafted from the original Starter code given [here](../Orig_Starter_Codes_BM/week4_numpy_starter.py).

___
<a name="apd"></a>
## Appendices & Graphs
Here are all the charts created with my code:

![flow_202009](../assignment_4/graphs/flow_202009.png "flow from 9/5/2020 to 9/19/2020")

![g9](../assignment_4/graphs/g9.png "All September Data")

![g10](../assignment_4/graphs/g10.png "All October Data")

![g11](../assignment_4/graphs/g11.png "All November Data")

![g12](../assignment_4/graphs/g12.png "All December Data")

___
<a name="cit"></a>
## Works Cited:

[My estimate,](https://github.com/HAS-Tools-Fall2020/forecasting/blob/master/forecast_entries/mitchell.csv) given in row 5 of *mitchell.csv*, was estimated by the creation and application of the python code presented above.  The data used for this estimate was obtained via the USGS NWIS [mapper](https://maps.waterdata.usgs.gov/mapper/) for the gage number 09506000.
###### ~Thank you!
