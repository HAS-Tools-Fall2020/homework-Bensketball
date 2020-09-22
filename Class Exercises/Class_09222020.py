# Class Exercises

# %%
# Import the modules we will use
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# %%
# EXERCISE 1: 
#1a.  Create a 3X3 matrix with values ranging from 2-10

# Laura
# x = np.arange(2,11)
# np.reshape(x)
# print(x)

# Richard
print((np.array(range(2,11,1)).reshape(3,3)))

# Diana
Ex_1= np.array([(2,3,4),(5,6,7),(8,9,10)])
print(Ex_1)


#1.b  Make a matrix with all of the even values from 2-32

# Ben
print((np.array(range(1,17,1)).reshape(4,4))*2)


# 1.c Make a matrix with all of the even values from 2-32
# But this time have the values arrange along columns rather than rows

# Ben
print(np.transpose((np.array(range(1,17,1)).reshape(4,4))*2))


# BONUS:
# Create the same 3x3 matrix with value ranging from 2-10 as you did 
# in part a but this time do so by combining one 3X1 matrix and one 1X3 matrix



# %%
# Notes:
# This class explains how to Evaluate! (09222020)
