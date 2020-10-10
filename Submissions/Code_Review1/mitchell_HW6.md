# Benjamin Mitchell's Code (Bensketball)
## `10/9/2020`
## Code review #1

## Hello Camillo! (unless I am confused XD)

___
### Table of Contents:
0. [ Instructions](#inst)
1. [ Your Code Review](#rev)
2. [ Python Code(s)](#cod)

4. [ Appendices & Graphs](#apd)
5. [ Works Cited](#cit)

___
<a name="inst"></a>
## How to run my code:
`Run my code!
`
Just kidding, I can walk you though what I have created here.

First off, the folder you copied to your computer should be the folder titled 'Code_Review1'.  Contained in this folder is my python code title 'mitchell_HW7.py' via the instruction of GitHub.  The website to this GitHub can be found [here](https://github.com/HAS-Tools-Fall2020/homework-Bensketball/tree/master/Submissions/Code_Review1)
___
<a name="rev"></a>
### Your Code Review
##### Fill in the question below from GitHub assignment:

1. First check below to see who your partner is.

  **Ans:**
  `
  `

2. Clone their repo to your computer. You can find their repo by going to the main GitHub organization page for this class.

  **Ans:**
  `
  `

3. Review their code following the code_review_rubric.md instructions in the starter_codes folder. You should provide your comments and scores in the spaces they have provided for you in their ReadMe.md file in the Code_Review1 folder of their GitHub submissions folder.

  **Ans:**
  `
  `

4. Follow the instructions they have provided in their ReadMe.md file to run their script and generate their 4 forecast values.

  **Ans:**
  `
  `

5. Enter all four values (the two regression forecasts and the two forecast values into the ReadMe.md file of your partners repo.

  **Ans:**
  `
  `

6. Enter the two forecast values into the lastname.csv file for your partner. Remember you are entering their forecast for them this week, not your own!

  **Ans:**
  `
  `




___
<a name="cod"></a>
## My Python Code(s):

##### The Python code can be found [here](../Code_Review1/mitchell_HW7.py).  It can also be found the folder you downloaded.

###### Review the starter code I provided to see how to build an autoregressive(AR) model. Then build your own model, you can modify my model in any way for example changing the number of time steps used for prediction or changing the testing and training data periods. The only rule is that you must make some modifications to make the model your own.

###### For your written assignment provide the following. Your submission should include at least 3 different types of plots (see the note at the end of the previous section for how to add these into your markdown file if you are not sure how to do that):

1. A summary of the AR model that you ended up building, including (1) what you are using as your prediction variables, (2) the final equation for your model and (3) what you used as your testing and training periods. In your discussion please include graphical outputs that support why you made the decisions you did with your model.

**Ans:**


`(2) "y = m * x + b" OR "y = 0.96 * x + 5.56" with an R_squared value of 0.91.
`

`(3) I choose to use every other day because I was cutting of a huge chunk of data when I restricted all flows to be under 200.  I made this choice because we seem to be in a drought right now.  The graphs below show my training period for my model and my full flow period:
`

![g-all](../assignment_6/graphs/Observed_Flow_All.png "Observed_Flow_All")

![g-train](../assignment_6/graphs/Observed_Flow_Train.png "Observed_Flow_Train")


2. Provide an analysis of your final model performance. This should include at least one graph that shows the historical vs predicted streamflow and some discussion of qualitatively how you think your model is good or bad.

**Ans:**
`I think this model can be greatly improved upon.  I think next time I want to use week's average flows instead of days but I will need to write a more complicated code for this.  I found that if I cut data off at 200 CFS that I got "NaN" values because I cut rows out of my data.  I do not think this model type is good for predicting flow because of how flow data seems rather random.  I suspect that this model is only good for no more than a week in advance.  I will say that because I cut my data off at 200 CFS that I ended up with a rather nice R_squared value of 0.91 (on its way to 1.00).  My graph(s) below show my model at work:
`

![g-sim](../assignment_6/graphs/Observed_Flow_Sim.png "Observed_Flow_Sim")

![g-AR_Log](../assignment_6/graphs/AR_Log.png "AR_Log")

![g-AR](../assignment_6/graphs/AR.png "AR")


3. Finally, provide discussion on what you actually used for your forecast. Did you use your AR model, why or why not? If not how did you generate your forecast this week?

**Ans:**
`I went ahead and used the model to make my predictions.  However, I do not think that my current model is super accurate given the data I used.  Because I used a difference period of one day, using this model to predict weeks flows is inaccurate.  I generated my forecast by taking the formula spit out be the model "y = 0.96 * x + 5.56" and plugged in the flow over and over filling out my perditions until the end of the semester.  I used a "For" loop to do this.  The slope is positive so my predictions increase throughout the year.  Same goes for this weeks and next weeks predictions.  However, I used a different starting flow.  Using the week from 8-15-2020 to 8-21-2020, the average flow was calculated and used for my long term predictions.  This value was found to be 33.84285714285714.  For this weeks prediction, Saturday's (10/03/2020) flow was used for my iteration.
`

___
<a name="est"></a>
## Estimation6 Explanation

Explanation is highlighted above in the questions this week. ^^^

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

[My estimate,](https://github.com/HAS-Tools-Fall2020/forecasting/blob/master/forecast_entries/mitchell.csv) given in row 5 of *mitchell.csv*, was estimated by the creation and application of the python code presented above.  The data used for this estimate was obtained via the USGS NWIS [mapper](https://maps.waterdata.usgs.gov/mapper/) for the gage number 09506000.
###### ~Thank you!
