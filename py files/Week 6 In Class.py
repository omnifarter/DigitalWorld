##Qn1
# def reverse(s):
#     ans = ""
#     for i in range(len(s)):
#         ans += str(s[-i-1])
#     return ans
##Qn2
# def check_password(pw):
#     if len(pw) <8:
#         return False
#     if pw.isalnum() == False:
#         return False
#     counter =0
#     for i in pw:
#         if i.isnumeric()== True:
#             counter += 1
#     if counter >1:
#         return True
#     else:
#         return False
##Qn3
# def longest_common_prefix(s1,s2):
#     common = ""
#     for i in range(len(s1)):
#         if len(s1)==len(common) or len(s2)==len(common):
#             break
#         if s1[i] == s2[i]:
#             common+= s1[i]
#         else:
#             break
#     return common
# print ( longest_common_prefix ( ' distance ',' disinfection '))

#You can use the zip function
##Qn4
import numpy as np
class Coordinate :
    x =0
    y =0
def get_maxmin_mag(f):
    lst=[]
    for line in f:
        a = Coordinate()
        values = line.split()
        a.x = float(values[0])
        a.y = float(values[1])
        lst.append(a)
    lst2=[]
    for items in lst:
        mod = np.sqrt((items.x)**2 + (items.y)**2)
        lst2.append(mod)
    max_value =max(lst2)
    min_value =min(lst2)
    max_index = lst2.index(max_value)
    min_index = lst2.index(min_value)
    coord_max = lst[max_index]
    coord_min = lst[min_index]
    f.close()
    return coord_max,coord_min

f = open('C:/Users/Omnif/Desktop/SUTD/Digital World/text_files/xy.dat','r')
get_maxmin_mag(f)
