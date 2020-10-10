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

First off, the folder you copied to your computer should be the folder titled 'Code_Review1' found in my 'Submissions' folder of GitHub Repo.  Contained in this folder is my python code title 'mitchell_HW7.py' via the instructions on GitHub.  There should also be an empty folder called graphs and an empty The website to this GitHub can be found [here](https://github.com/HAS-Tools-Fall2020/homework-Bensketball/tree/master/Submissions/Code_Review1) or [here]().  If you go to this website, you will find many helpful links to run my code.  The steps are below:

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

  **Ans**
  `
  `

4. Follow the instructions they have provided in their ReadMe.md file to run their script and generate their 4 forecast values.

5. Enter all four values (the two regression forecasts and the two forecast values into the ReadMe.md file of your partners repo.

  My regression forecasts are the same as my forecast values!  Please just right each number twice. :)

  ***Regression Forecasts:***

  **Ans1**
  `
  `

  **Ans2**
  `
  `

  ***Forecast Values:***

  **Ans3**
  `
  `

  **Ans4**
  `
  `

6. Enter the two forecast values into the lastname.csv file for your partner. Remember you are entering their forecast for them this week, not your own!

My excel is titled *'mitchell.csv'*.  It can be found [here](https://github.com/HAS-Tools-Fall2020/forecasting/tree/master/forecast_entries) or [here](https://github.com/HAS-Tools-Fall2020/forecasting/blob/master/forecast_entries/mitchell.csv) for your convenience.

___
<a name="cod"></a>
## My Python Code(s):

##### The Python code can be found [here](../Code_Review1/mitchell_HW7.py).  It can also be found the folder you downloaded.  It was derived from this code [here](../../Orig_Starter_Codes_BM/week6_matplotlib_starter.py).


Finally, if the code works there should be a graph below:

![g-AR](../Code_Review1/graphs/AR.png "AR")

###### ~Thank you!
