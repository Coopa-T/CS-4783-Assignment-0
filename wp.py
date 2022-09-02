#Assignment 0, Question 3
import numpy as np

"""
Problem statement:  
You and a friend go to buy tacos. You get three soft tacos 
and  three  burritos  and  your  total  bill  is  $11.25.  Your 
friend's  bill  is  $10.00  for  four  soft  tacos  and  two 
burritos. How much do soft tacos cost? How much do burritos 
cost?

Solve the equation:
3x + 3y = 11.25
4x + 2y = 10

Converting into a matrix equation gives us
  [3, 3]  =  [11.25]
  [4, 2]  =    [10]

So let's solve the equation this way,
to do that we can use the following formulas:
AX = B
A^-1 * AX = A^-1 * B
X = A^-1 * B

Solving using the inverse of matrix A.
"""

Food = np.matrix([[3, 3], [4, 2]])
Bill = np.matrix([[11.25], [10]])

#Inverse of the Food matrix
Food_Inverse = np.linalg.inv(Food)

Answer = Food_Inverse * Bill
print(Answer)