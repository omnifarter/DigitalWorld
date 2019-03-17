## Qn 2
# def compound_value_months(savings,rate,n):
#     monthly_rate = rate/12
#     account = 0
#     for i in range(n):
#         account = (account + savings) * (1 + monthly_rate)
#     return round(account,2)

## Qn 3
# def find_average(x):
#     averages = []
#     total_length = 0
#     total = 0
#
#     for sublist in x:
#         subtotal = 0
#         for element in sublist:
#             subtotal += element
#             total += element
#
#         total_length += len(sublist)
#         if len(sublist) == 0:
#             averages.append(0)
#         else:
#             averages.append(subtotal/len(sublist))
#
#     return averages, (total/total_length)

##Qn 4
# def transpose_matrix(a):
#     t_a =[] ##create a new matrix
#     for col in range(len(a[0])):
#         new_row = [] ## add in new row
#         for row1 in range(len(a)):
#             print (a[row1][col])
#             new_row.append(a[row1][col]) ##append elements into new row
#             print(new_row)
#         t_a.append(new_row)
#     return t_a

##Qn 5
# def get_details(name,key,list):
#     for i in list:
#         if name in i.values():
#             return i[key]

##Qn 6
# def get_base_counts(x):
#     a = 0
#     c = 0
#     g = 0
#     t = 0
#     for i in x:
#         print (i)
#         if i =="A":
#             a+=1
#         elif i =="C":
#             c += 1
#         elif i == "G":
#             g += 1
#         elif i == "T":
#             t += 1
#         else:
#             return "The input DNA string is invalid"
#     dic ={"A":a,"C":c,"G":g,"T":t,}
#
#     return dic

