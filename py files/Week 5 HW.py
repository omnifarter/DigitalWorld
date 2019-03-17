##Qn1
# def extract_values(n):
#     x = int((len(n)-1)/2)
#     print (n[:x])
#     lst = []
#     lst.append( int(n[:x]))
#     lst.append(int(n[x+1:]))
#     return tuple(lst)
#
# def calc_ratios(t):
#     if t[1] == 0:
#         return False
#     ratio = t[0]/t[1]
#     return ratio
# print(extract_values('123 325'))
#
# def get_data():
#     ans = input("Enter integer pair (hit Enter to quit):")
#     t = extract_values(ans)
#     ratio = calc_ratios(t)
#     return ratio

##Qn2
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

def display_calendar_modified(year,month):
    if month == None:
        return display_calendar(year)
    calander = construct_cal_year(year)
    new_month = calander.pop(month)
    disp = ""
    for x in new_month:
        disp += str(x) + "\n"
        if x == new_month[0]:
            disp += "  S  M  T  W  T  F  S" +"\n"
    disp = disp[:-1]
    return disp

print(display_calendar_modified(2019,3))
