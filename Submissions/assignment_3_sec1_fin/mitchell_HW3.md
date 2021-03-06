# Benjamin Mitchell
## `9/13/2020`
## Homework #3

___
# ***Grade***

2/3 - Great job on the forecast but you didn't answer the assignment questions. Make sure you get those answered next time.

In answer to your question the link is fine or you can also just make a copy of the script and put it in your submissions folder. I'm not going to run it I just want to be able to look at them easily.

___
### Table of Contents:
1. [ Questions](#qns)
2. [ Discharge Estimation](#est)
3. [ Python Code](#cod)
4. [ Works Cited](#cit)

___
<a name="qns"></a>
## Assignment Questions

1. Describe the variables flow, year, month, and day. What type of objects are they, what are they composed of, and how long are they?

**Ans:**
`'flow', 'year', 'month', and 'day' are all lists, "cut up" from the downloaded USGS NWIS data titled 'streamflow_week3.txt'.
`

2. How many times was the daily flow greater than your prediction in the month of September (express your answer in terms of the total number of times and as a percentage)?

**Ans:**
`
`

3. How would your answer to the previous question change if you considered only daily flows in or before 2000? Same question for the flows in or after the year 2010? (again report total number of times and percentage)

**Ans:**
`
`

4. How does the daily flow generally change from the first half of September to the second?

**Ans:**
`
`

___
<a name="est"></a>
## Estimation3 Explanation

For my third estimate, I decided to use and transform a prewritten python code using Visual Studio Code.  The python code, I wrote, allowed me to compare different years (2017, 2018, 2019, and 2020) in the week leading up to the 14th of September (09-06-year through 09-12-year).  I also took the week flow data described and calculated the min, max, mean, and STDV of the flow lists I created.  I eventually want to create a linear regression on the data, but I will have to wait until we are allowed to do so.  I was trying to create a 'For' loop that involved the year part of the dates as well, but this turned out to be too ambitious for the time I had to work on it.  Sorry for the late submission of the markdown file.  I spent too much time on the coding part of this assignment.

___
<a name="cod"></a>
## My Python Code3:

The Python Code, created in Visual Studio Code (VSC), can be found [here](https://github.com/HAS-Tools-Fall2020/homework-Bensketball/blob/master/assignment_3/week3_lists_starter_BM.py).  Let me know if you would like me to put it in the "Submissions" folder instead of using a link.  Trying to get a better way to organize my files for future HW assignments.


    test1: [code](../assignment_3/week3_lists_starter_BM.py "my_code")

test2:
```python
# week3_lists_starter_BM.py
import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(week3_lists_starter_BM.py, '../assignment_3/')

import week3_lists_starter_BM.py

print "Hello World"
print(../assignment_3/week3_lists_starter_BM.py)
```

___
test3:

[source](http://web.simmons.edu/~grabiner/comm244/weekfour/code-test.html)

open(../assignment_3/week3_lists_starter_BM.py)

<pre><code>
open(../assignment_3/week3_lists_starter_BM.py)
</code></pre>

___
test4:

<p><code>
Output some text from Python in <strong>Markdown</strong>:
<code>python
from sklearn.datasets import load_iris
from sklearn import tree
iris = load_iris()
clf = tree.DecisionTreeClassifier()
clf = clf.fit(iris.data, iris.target)
clf.predict_proba(iris.data[:1, :])
</code></p>

___
<a name="cit"></a>
## Works Cited:

[My estimate,](https://github.com/HAS-Tools-Fall2020/forecasting/blob/master/forecast_entries/mitchell.csv) given in row 4 of *mitchell.csv*, was estimated by the creation and application of the python code presented above.  The data used for this estimate was obtained via the USGS NWIS [mapper](https://maps.waterdata.usgs.gov/mapper/) for the gage number 09506000.
###### ~Thank you!
