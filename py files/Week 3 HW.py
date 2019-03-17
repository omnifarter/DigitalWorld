##HW Qn 1
# def temp_convert(unit,degree):
#     if unit == "C":
#         c = (degree - 32)/9*5
#         return c
#     elif unit == "F":
#         f = degree*9/5 + 32
#         return f
#     else:
#         return None

##HW Qn 2
# def get_even_list(a):
#     even_number = []
#     for i in a:
#         if (i%2) == 0:
#             even_number.append(i)
#     return even_number

# ##HW Qn 3
# def is_prime(a):
#     for i in range(2,a-1):
#         if a%i == 0 :
#             return False
#     return True

##HW Qn 4
# import math
# def approx_ode(h,t0,y0,tn):
#     # Inputs - h  : step size
#     #          t0 : initial t value (at step 0)
#     #          y0 : initial y value (at step 0)
#     #          tn : t value at step n
#     # Add your code below!
#     counter = 0
#     y = y0
#     t = t0
#     while t < tn:
#         y = y + h*(3 + math.exp(-t) - 0.5*y)
#         t = round(t + h,2)
#     return y

def print_interations(n):
    counter = 0
    while counter <= n:
        counter += 1
        print("PRINT ME")
    return "PRINT ME NOW"
print_interations(3)
