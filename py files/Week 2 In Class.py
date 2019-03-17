## problem set 2, Qn 1
# g = 9.81
# def position_velocity(v,t):
#     y = v*t -0.5*g*t**2
#     yy = v -g*t
#     return (round(y,2),round(yy,2))


## problem set 2, Qn 2
# def bmi(w,h):
#     hh = h/100
#     b = w / hh**2
#     return (round(b,1))

## problem set 2, Qn 3
from math import sqrt
class Coordinate:
    x =0.0
    y =0.0

def area_of_triangle(p1,p2,p3):
    side1 = sqrt(abs((p1.x-p2.x)**2 + (p1.y-p2.y)**2))
    side2 = sqrt(abs((p2.x-p3.x)**2 + (p2.y-p3.y)**2))
    side3 = sqrt(abs((p1.x-p3.x)**2 + (p1.y-p3.y)**2))
    s = (side1 + side2 + side3)/2
    area = sqrt(s*(s - side1) * (s-side2) * (s-side3))
    return round(area,2)
p1 = Coordinate()
p2 = Coordinate()
p3 = Coordinate()

p1.x = int(input("Enter x coordinate of the first place of a triangle:"))
p1.y = int(input("Enter y coordinate of the first place of a triangle:"))
p2.x = int(input("Enter x coordinate of the second place of a triangle:"))
p2.y = int(input("Enter x coordinate of the second place of a triangle:"))
p3.x = int(input("Enter x coordinate of the third place of a triangle:"))
p3.y = int(input("Enter x coordinate of the third place of a triangle:"))
print( area_of_triangle(p1,p2,p3))
## problem set 2, Qn 5
# def describe_bmi(x):
#     if x < 18.5:
#         print(" nutritional deficiency")
#     elif 18.5 <= x <23:
#         print("low risk")
#     elif 23 <= x <27.5:
#         print("moderate risk")
#     else:
#         print("high risk")

## problem set 2, Qn 6
# def letter_grade(mark):
#     if 90<= mark <= 100:
#         return ("A")
#     elif 80<= mark < 90:
#         return ("B")
#     elif 70<= mark < 80:
#         return ("C")
#     elif 60<= mark <70:
#         return ("D")
#     elif 0<= mark <60:
#         return ("E")
#     else:
#         return (None)

## problem set 3, Qn 7
# class Coordinate:
#     x = 0.0
#     y = 0.0
# def is_in_square(square1, side1, square2, side2):
#     if abs(square1.x - square2.x) > side1 + side2 or abs(square1.y - square2.y) > side1 + side2:
#         return False
#
#     else:
#         return True
#
# print(is_in_square(s1,10,s2,20))
