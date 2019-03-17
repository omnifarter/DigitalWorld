# ##Week 3 Qn 1
# def list_sum(x): ##Using a for loop
#     y = 0
#     for i in x:
#         y += i
#     return y

# def list_sum(lst): ##Using a while loop
#     length = len(lst)
#     counter = 0
#     sum = 0
#     while counter < length:
#         sum += lst[counter]
#         counter+=1
#     return sum

##Week 3 Qn 2
# import sys
# def minmax_in_list(lst):
#     highest = -sys.maxsize-1
#     lowest = sys.maxsize
#     if len(lst)>0:
#         for i in range(len(lst)):
#             if highest < lst[i]:
#                 highest = lst[i]
#             if lowest > lst[i]:
#                 lowest = lst[i]
#         return lowest,highest
#     else:
#         return None,None

#Week 3 Qn 3
# def is_palindrome(a):
#     string1 = str(a)
#     lst = []
#     for x in string1:
#         lst.append(int(x))
#     counter = 0
#     counter1 = len(lst) - 1
#
#     while counter<counter1:
#         x = lst[counter]
#         y = lst[counter1]
#         if x == y:
#             counter+=1
#             counter1-=1
#         else:
#             return False
#     return True

##ideal ans:
# def is_palindrome(num):
#     numstr = str(num)
#     pos = 0
#     while pos < len(numstr)/2:
#         if numstr[pos] != numstr[-1-pos]:
#             return False
#         pos += 1
#     return True

## Part 2 Qn 1
# import math
# import matplotlib.pyplot as plt
# from math import e
# x_values = list(range(-5,6))
# y_values =[]
# for i in range(-5,6):
#     y = 1/(1 + math.exp(-i))
#     y_values.append(y)
# plt.plot(x_values,y_values)
# plt.xlabel("x values")
# plt.ylabel("y values")
# plt.title("graph of f(x)")
# plt.show()

## Part 2 Qn 2 part 1
# import numpy as np
# import matplotlib.mlab as mlab
# import matplotlib.pyplot as plt
#
# daily_total_rainfall = [ 0.2, 7.8, 0.4, 3.4, 0.4, 3.8, 12, 5.4, 1.6,
# 0, 0.8, 12.4, 2.4, 2, 4.6, 0.8, 18.4, 7.4, 20.6, 4, 13.2, 2, 4, 0,
# 4.8, 14.4, 9.6, 0, 5.6, 7.6]
#
# bins = 5
# patches = plt.hist(daily_total_rainfall, bins)
# plt.show()

## Part 2 Qn 2 part 2
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

daily_total_rainfall = [ 0.2, 7.8, 0.4, 3.4, 0.4, 3.8, 12, 5.4, 1.6,
0, 0.8, 12.4, 2.4, 2, 4.6, 0.8, 18.4, 7.4, 20.6, 4, 13.2, 2, 4, 0,
4.8, 14.4, 9.6, 0, 5.6, 7.6]

bins = list(range(0,25,4))
patches = plt.hist(daily_total_rainfall, bins)
plt.show()
