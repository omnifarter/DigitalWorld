##Qn 1
# def f_to_c(f):
#     c = (f-32)*5/9
#     return round(c,1)
# def f_to_c_approx(f):
#     c_approx = (f-30)/2
#     return round(c_approx,1)
# def get_conversion_table_a():
#     result =[]
#     for values in range(0,110,10):
#         result.append([values,f_to_c(values),f_to_c_approx(values)])
#     return result
#
# def get_conversion_table_b():
#     result =[]
#     l =[]
#     l2=[]
#     l3=[]
#     for values in range(0,110,10):
#         l.append(values)
#     result.append(l)
#     for values in range(0,110,10):
#         l2.append(f_to_c(values))
#     result.append(l2)
#     for values in range(0,110,10):
#         l3.append(f_to_c_approx(values))
#     result.append(l3)
#
#     return result

##Qn2
# def max_list(inlist):
#     new_list = []
#     for i in range(len(inlist)):
#         max = inlist[i][0]
#         for elements in range(len(inlist[i])):
#             if max < inlist[i][elements]:
#                 max = inlist[i][elements]
#         new_list.append(max)
#     return new_list
# print(max_list([[1 ,2 ,3] ,[4 ,5]]))

##Qn3
# def multiplication_table(n):
#     if n > 0:
#         table = []
#         for x in range(n):
#             row = []
#             for y in range(n):
#                 row.append((x+1) * (y+1))
#             table.append(row)
#         return table
#     else:
#         return None

## Qn4
# def most_frequent(l):
#     new_dict = {}
#     new_list = []
#     for values in l:
#         if values not in new_dict.keys():
#             new_dict[values] = 1
#         elif values in new_dict:
#             new_dict[values] += 1
#     max = 0
#     for keys, values in new_dict.items():
#         if values > max:
#             max = values
#     for keys, values in new_dict.items():
#         if max == values:
#             new_list.append(keys)
#
#     return new_list

# ##Qn 5
# def diff(poly):
#     dp ={}
#     for keys,values in poly.items():
#         if keys != 0:
#             dp[keys-1] = values * keys
#     return dp
#






