# Benjamin Mitchell
## `11/30/2020`
## Homework #14

___
<a name="grd"></a>
### ***Grade***


___
### Table of Contents:
0. [ Grade](#grd)
1. [ Questions](#qns)
2. [ Discharge Estimation](#est)
3. [ Python Code(s)](#cod)
4. [ Works Cited](#cit)

___
<a name="qns"></a>
## Assignment Questions

1. What is the paper or project you picked? Include a title, a link the the paper and a 1-2 sentence summary of what its about.

  **Ans:**
`I found on the U of A Library Website a really interesting article about a study on gravity waves.  This dissertation, titled "Gravitational Waves Research at TOROS UTRGV" was about the studies that Pamela Ivonne Lara has been doing at TOROS UTRGV using GitHub and python.  I choose this article because it looked promising to replicate her results.  Oh man was I in for a ride!
`

  Dissertation: [here](https://search-proquest-com.ezproxy1.library.arizona.edu/docview/2111273900?pq-origsite=summon)
OR [here](Gravitational_Waves_Research_a.pdf)

  Repo: [here](https://github.com/toros-astro)

2. What codes and/or data are associated with this paper? Provide any link to the codes and datasets and a 1-2 sentence summary of what was included with the paper (i.e. was it a github repo? A python package? A database? Where was it stored and how?)

  **Ans:**
`This dissertation had a GitHub Repo associated with the research and it even was able to set up my environment for me, sorta...
`
You can find the repository [here](https://github.com/toros-astro)

  `I quickly set up a new conda environment for testing but the code had other plans.  It made its own environment after running the code titled 'setup.py' and this code in turn ran its own codes titled, 'ez_setup.py' and 'use_setuptools.py'.  What I would later find out after it had finished running is the code went past the environment I set up for it and started installing things outside in the base environment.  After that I tried to fix it by going back to the environment I set up and running the code again.  After that, I couldn't get back to the environment the code set up.  I do not think it broke anything though, since the code's environment was a PyPI based environment.  I think this is why it created its own environment.  It was unhappy with Conda.
`

3. Summarize your experience trying to understand the repo: Was their readme helpful? How was their organization? What about documentation within the code itself?

  **Ans:**
`I was able to explain my troubles with this repository above.  To speak on it more, I feel that these codes were very well documented and explained to be honest.  I feel it was just my lack of reading ability and comprehension that made this so difficult.  I think coding is just really hard to boil down for someone else who did not work on the project.  It almost another project entirely to understand a code this in depth and would take a lot of dedication.  After working with a repo like this, I can see how difficult it can be to explain something this complicated.  On the other hand, I have worked with other much more simplified GitHub Repos to do simple tasks, such as downloading a YouTube video for a zoom background.  These have great instructions to learn from, but this is no dissertation, but a small "for fun" project.
`

4. Summarize your experience trying to work with their repo: What happened? Where you successful? Why or why not?

  **Ans:**
`I unfortunately was unsuccessful because as soon as I left the environment that the code created for itself, I could not find it again.  The code would not run any codes after the initial setup part.  I believe this is because the setup had a big plan that I got in the way of.  I tried to delete and download the Repo again, but this did not fix the problem.  I went through a couple more fixes, but I did not want to go to far in risk of messing up my other environments.  Some forums online (stack overflow for example) said to reinstall python and conda which would go beyond the set time limit.  It is a bummer to because I wanted to see how they were measuring the gravity waves.
`

5. Summarize your experience working with the data associated with this research. Could you access the data? Where was it? Did it have a DOI? What format was it in?

  **Ans:**
`Because of the way there repositories were set up, I did not dive to far into one of there Repos titled, "obs_base".  I believe this is where most of there data for the dissertation was held and organized.  There were 16 other Repos assosated with this project for a total of 18 repositories.  I tried to work with the first one titled, "astroalign".
`

6. Did this experience teach you anything about your own repo or projects? Things you might start or stop doing?

  **Ans:**
`I learned a lot actually!  Really how complicated it is to describe a code is just like being able to teach.  I think the biggest struggle is the loss of the human element when trying to explain a code, repository or database.  There are many ways to explain the same ideas and, complimentary, there are may way to interpret one same idea.  This is the task to overcome when explaining a python code because your explanation can be taken in many different ways.  The language you use is important, and like I said above, I think this person did a great job.  I think it was a detailed enough explanation for someone who understood python environments, of which I have much to learn still.
`


___
<a name="est"></a>
## Estimation14 Explanation

I used the same code I have been improving upon for my estimation this week.


___
<a name="cod"></a>
## My Python Code(s)6:

The Python Code for the estimation, created in Visual Studio Code (VSC), can be found [here](Mitchell_week14.py).


___
<a name="cit"></a>
## Works Cited:

[My estimate,](https://github.com/HAS-Tools-Fall2020/forecasting/blob/master/forecast_entries/mitchell.csv) given in row 5 of *mitchell.csv*, was estimated by the creation and application of the python code presented above.  The data used for this estimate was obtained via the USGS NWIS [mapper](https://maps.waterdata.usgs.gov/mapper/) for the gage number 09506000.
###### ~Thank you!
