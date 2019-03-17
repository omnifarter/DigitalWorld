# ##Qn 1
# import random
# craps = set([2,3,12])
# naturals = set([7,11])
# def roll_two_dices():
#     dice1= random.randrange(1,7)
#     dice2 = random.randrange(1,7)
#     return dice1, dice2
# def print_lose():
#     return print("You lose")
# def print_win():
#     return print("You win")
# def print_point(p):
#     return print("Your points are {}".format(p))
# def is_craps(n):
#     if n in craps:
#         return True
#     else:
#         return False
# def is_naturals(n):
#     if n in naturals:
#         return True
#     else:
#         return False
#
# def play_craps():
#     point = -1
#     while True:
#         n1,n2 = roll_two_dices()
#         sumn = n1 + n2
#         print("You rolled {} + {} = {}".format(n1,n2,sumn))
#         if point == -1:
#             if is_craps(sumn):
#                 print_lose()
#                 return 0
#             elif is_naturals(sumn):
#                 print_win()
#                 return 1
#             point = sumn
#             print_point(point)
#         else:
#             if sumn == 7:
#                 print_lose()
#                 return 0
#             elif sumn == point:
#                 print_win()
#                 return 1


## Qn2
def leap_year(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

def day_of_week_jan1(year):
    A = year
    def R(y,m):
        result = y%m
        return result
    d = R(1 + 5 *R(A-1,4) + 4*R(A-1,100) + 6*R(A-1,400), 7)
    return d

def num_days_in_month(month_num,leap_year):
    if month_num == 2:
        if leap_year == True:
            return 29
        else:
            return 28
    elif month_num == 1 or month_num == 3 or month_num == 5 or month_num == 7 or month_num == 8 or month_num == 10 or month_num == 12:
        return 31
    elif month_num == 4 or month_num == 6 or month_num == 9 or month_num == 11:
        return 30
    else:
        return "ERROR, month is not valid"

def construct_cal_month(month_num,first_day_of_month,num_days_in_month):
    month_calander = []
    month_name={1:"January",2:"February",3:"March",4:"April",5:"May",6:"June",7:"July",8:"August",9:"September",10:"October",11:"November",12:"December"}
    current_month_name = month_name[month_num]
    month_calander.append(current_month_name)
    n = 1
    while n <= num_days_in_month:
        week=[]
        while n == 1:

            if len(week) == first_day_of_month:
                week.append("  1")
                n+=1
                break
            week.append("   ")
        while len(week)<7:
            if n<10:
                week.append("  " + str(n))
                n +=1
            elif n>=10:
                week.append(" " + str(n))
                n+=1
            if n == num_days_in_month+1:
                break
        week1=""
        for i in week:
            week1 += str(i)
        month_calander.append(week1)
    return month_calander

def construct_cal_year(year):
    if year <1800 or year > 2099:
        return "ERROR, year out of range"
    calender = []
    calender.append(year)
    is_leap_year = leap_year(year)
    first_jan = day_of_week_jan1(year)
    first_day = first_jan
    for x in range(12):
        days_in_month = num_days_in_month(x+1,is_leap_year)
        month = construct_cal_month(x+1,first_day,days_in_month)
        calender.append(month)
        first_day = (first_day + (num_days_in_month(x+1,is_leap_year)))%7
    return calender

def display_calendar(year):
    cal_year = construct_cal_year(year)
    cal_year.pop(0)
    print (cal_year)
    disp = ""
    for i in cal_year:
        for x in i:
            disp += str(x) +"\n"
            if x == i[0]:
                disp += "  S  M  T  W  T  F  S" +"\n"
        if i!= cal_year[-1]:
            disp+= "\n"
    disp = disp[:-1]
    return disp
##Qn3
# def fact_rec(n):
#     if n == 0:
#         return 1
#     num = n
#     num = n * fact_rec(n-1)
#     return num
