# -*- coding: utf-8 -*-
"""Untitled6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Unhv3QOJ66IQxEqul2XwPSu2AAmtT0JV
"""

import numpy as np

from scipy.linalg import solve

A = np.random.random((1, 2))

A

B = np.random.random((2, 2))

C = np.random.random((2, 1))

X=A*B*C



X

X=0.35

B = [[3, -1], [-2, 3]]

C = [[0.2, 0.8]]

binv=scipy.linalg.inv(B)

binv

import scipy

btran=np.transpose(B)

ctran=np.transpose(C)

bctran=btran*ctran

import numpy as np

from scipy import linalg

B = np.random.random((2, 2))

C = np.random.random((2, 1))

linalg.inv(B).dot(C)

B.dot(linalg.inv(B).dot(C)) - C

np.linalg.solve(B, C)

B.dot(np.linalg.solve(B, C)) - C



A = [[0 for j in range(2)] for i in range(1)]

A

X = input("Enter your value: ")

import numpy as np
  
R = int(input("Enter the number of rows:"))
COL = int(input("Enter the number of columns:"))
  
  
print("Enter the entries in a single line (separated by space): ")
  
# User input of entries in a 
# single line separated by space
entries = list(map(int, input().split()))
  
# For printing the matrix
B = np.array(entries).reshape(R, COL)
print(B)

import numpy as np
  
R = int(input("Enter the number of rows:"))
COL = int(input("Enter the number of columns:"))
  
  
print("Enter the entries in a single line (separated by space): ")
  
# User input of entries in a 
# single line separated by space
entries = list(map(float, input().split()))
  
# For printing the matrix
C = np.array(entries).reshape(R, COL)
print(C)

C = [0.2, 0.8]

bc=B.dot(C)

bc