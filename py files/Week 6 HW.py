##Qn 1
# def binary_to_decimal(strg):
#     strg = strg[::-1]
#     counter = 0
#     total = 0
#     for number in strg:
#         bit = 2**counter
#         total += (int(number) *bit)
#         counter +=1
#     return total
##Qn 2
# def uncompress(strg):
#     newstrg = ""
#     for x in strg:
#         try:
#             current_multiple = int(x)
#         except:
#             newstrg += current_multiple*x
#     return newstrg
##Qn 3
# def get_base_counts2(x):
#     a = 0
#     c = 0
#     g = 0
#     t = 0
#     unaccepted = "BDEFHIJKLMNOPQRSUVWXYZ"
#
#     for i in x:
#         if i =="A":
#             a+=1
#         elif i =="C":
#             c += 1
#         elif i == "G":
#             g += 1
#         elif i == "T":
#             t += 1
#         elif i in unaccepted:
#             pass
#         else:
#             return "The input DNA string is invalid"
#
#     dic ={"A":a,"C":c,"G":g,"T":t,}
#
#     return dic
##Qn 4
# def get_fundamental_constants(f):
#     constants ={}
#     counter =0
#     for line in f:
#         if counter<=1:
#             counter+=1
#             pass
#         else:
#             x = line.split()
#             constants[x[0]] = float(x[1])
#     return constants
# f = open('C:/Users/Omnif/Desktop/test.txt','r')
# print(get_fundamental_constants(f))
##Qn 5
# def process_scores(f):
#     for line in f:
#         x = line.split()
#         total = 0
#         for values in range(len(x)):
#             total += float(x[values])
#         avg = total / (len(x))
#         return total, avg


