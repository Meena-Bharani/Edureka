# Module 5:Introduction to NumPy

# 1.Convert the given list in to a numpy array and replace the odd elements with-2.
# Lst=[[1,2,3],
#      [4,5,6],
#      [7,8,9]]

import numpy as np
def convert_odd_nums():
    Lst=[[1,2,3],
         [4,5,6],
         [7,8,9]]
    arr = np.array(Lst)
    arr[arr%2!=0] = -2
    return arr
print(convert_odd_nums())

# 2.In the numpy array given below print all the elements ranging from 8 to 15.
# arr = [1,2,3,4,5,8,9,10,12,22,32,54,99,6,7]

def range_8_to_15():
    arr = [1, 2, 3, 4, 5, 8, 9, 10, 12, 22, 32, 54, 99, 6, 7]
    a = np.array(arr)
    btw = np.where((a>=8) & (a<=15)) #a.[a>=8 and a <=15].all()
    # print(a)
    # print(a[btw])
    return a[btw]
print(range_8_to_15())

# 3.Create a 3*3 narray that includes numbers from 1 to 9 and swap columns 1 and2.
#

# 4.In the given numpy array replace the NaN values with the average of columns
# arr= np.array([[1.3, 2.5, 3.6, np.nan],
#                [2.6, 3.3, np.nan, 5.5],
#                [2.1, 3.2, 5.4, 6.5]])
#
# 5.For the numpy array given below perform the following operation:
# i.Convert the numpy array into a numpy matrix
# ii.Sort the values in a matrix
#       arr = [[2,4,6],
#              [1,3,5]]
