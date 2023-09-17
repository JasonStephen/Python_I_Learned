# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 13:25:46 2023

@author: Jason_Stephen
"""


##>>-------------------------<<##

# year, month = map(int, input().split(','))

# if month in [1, 3, 5, 7, 8, 10, 12]:
#     days = 31
# elif month in [4, 6, 9, 11]:
#     days = 30
# elif month == 2:
#     if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#         days = 29
#     else:
#         days = 28
# else:
#     days = -1

# if days != -1:
#     print(days)
# else:
#     print("无效的月份")

##>>-------------------------<<##

# year, month, day = map(int, input().split(','))
# from datetime import datetime
# date = datetime(year, month, day)
# year_start = datetime(year, 1, 1)
# days_passed = (date - year_start).days
# print(days_passed)

##>>-------------------------<<##

# numbers = input().split(',')
# numbers = [int(x) for x in numbers]
# largest_number = max(numbers)
# print(largest_number)

##>>-------------------------<<##

# import math
# a, b, c = map(float, input().split(','))
# if a + b > c and a + c > b and b + c > a:
#     s = (a + b + c) / 2
#     area = math.sqrt(s * (s - a) * (s - b) * (s - c))
#     print(f"{area:.2f}")
# else:
#     print("No.")

##>>-------------------------<<##

# numbers = input().split(',')
# numbers = [int(x) for x in numbers]
# num1, num2, num3 = numbers
# if num1 % num3 == 0 and num2 % num3 == 0:
#     print("Yes.")
# else:
#     print("No.")

##>>-------------------------<<##

# numbers = input().split(',')
# numbers = [int(x) for x in numbers]
# num1, num2, num3 = numbers
# if num3 % num1 == 0 and num3 % num2 == 0:
#     print("Yes.")
# else:
#     print("No.")
    
##>>-------------------------<<##

# weight, height = map(float, input().split(','))

# bmi = weight / (height * height)

# if bmi < 18.5:
#     result = "Underweight"
# elif 18.5 <= bmi < 23:
#     result = "Normal"
# elif 23 <= bmi < 25:
#     result = "Overweight"
# else:
#     result = "Obese"

# print(result)

##>>-------------------------<<##

# import math
# a, b, c = map(float, input().split(','))
# discriminant = b**2 - 4*a*c
# if discriminant > 0:
#     root1 = (-b - math.sqrt(discriminant)) / (2*a)
#     root2 = (-b + math.sqrt(discriminant)) / (2*a)
#     print(f"{root1:.2f} {root2:.2f}")
# elif discriminant == 0:
#     root = -b / (2*a)
#     print(f"{root:.2f}")
# else:
#     print("No Root.")

##>>-------------------------<<##

# x = float(input())
# if x < -5:
#     fx = -5 * x + 1
# elif -5 <= x <= 4:
#     fx = x**2 + 1
# else:
#     fx = 3 * x + 5
# print(f"{fx:.1f}")

##>>-------------------------<<##

numbers = input().split(',')
numbers = [int(x) for x in numbers]
numbers.sort()
print(','.join(map(str, numbers)))