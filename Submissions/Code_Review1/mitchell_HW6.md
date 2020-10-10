# Benjamin Mitchell's Code (Bensketball)
## `10/9/2020`
## Code review #1

### *Hello Camillo! (unless I am confused on how the GitHub chart works! XD)

___
### Table of Contents:
0. [ Instructions](#inst)
1. [ Your Code Review](#rev)
2. [ My Python Code(s)](#cod)

___
<a name="inst"></a>
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

P.S. There is already a text file titled 'streamflow_week7_temp.txt' in the 'data' folder.  This text file is missing this Saturday.  This is why you are updating the data. :)

###### Step #2:
Run my code.  Make sure that the filename in the beginning reads like this:
```python
filename = 'streamflow_week7.txt'
filepath = os.path.join('data', filename)
print(os.getcwd())
print(filepath)
```

You will get

ValueError: illegal value in 4-th argument of internal None


~ Thank you!
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

  **Ans1**
  `
  `

  **Ans2**
  `
  `

  **Ans3**
  `
  `

  **Ans4**
  `
  `

6. Enter the two forecast values into the lastname.csv file for your partner. Remember you are entering their forecast for them this week, not your own!

___
<a name="cod"></a>
## My Python Code(s):

##### The Python code can be found [here](../Code_Review1/mitchell_HW7.py).  It can also be found the folder you downloaded.




___
<a name="cod"></a>
## My Python Code(s)6:

The Python Code, created in Visual Studio Code (VSC), can be found [here](../assignment_6/week6_matplotlib_starter_BM.py).  This python code was crafted from the original Starter code given [here](../Orig_Starter_Codes_BM/week6_matplotlib_starter.py).

___
<a name="apd"></a>
## Appendices & Graphs
Here are all the charts created with my code (there are a lot of them):

![g-all](../assignment_6/graphs/Observed_Flow_All.png "Observed_Flow_All")

![g-train](../assignment_6/graphs/Observed_Flow_Train.png "Observed_Flow_Train")

![g-sim](../assignment_6/graphs/Observed_Flow_Sim.png "Observed_Flow_Sim")

![g-AR_Log](../assignment_6/graphs/AR_Log.png "AR_Log")

![g-AR](../assignment_6/graphs/AR.png "AR")

___
<a name="cit"></a>
## Works Cited:

[My estimate,](https://github.com/HAS-Tools-Fall2020/forecasting/blob/master/forecast_entries/mitchell.csv) given in row 5 of *mitchell.csv*, was estimated by the creation and application of the python code presented above.  
###### ~Thank you!
