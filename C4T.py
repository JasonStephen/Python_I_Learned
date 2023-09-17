# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 16:53:57 2023

@author: Jason_Stephen
"""

# import math
# a, b, c = map(float, input().split(','))
# y = math.sqrt(a * b + b * c + a * c) / (a**2 + b**2 + c**2)
# print(f"{y:.5f}")

##>>-------------------------<<##

# import math
# a, b, c = map(float, input().split(','))
# L = (a+b+c)/2
# area=math.sqrt(L*(L-a)*(L-b)*(L-c))
# print(f"{area:.2f}")

##>>-------------------------<<##

# a, b = map(float, input().split(','))
# y = (a**2+b**2)/(a-b)/(a+b)
# print(f"{y:.2f}")

##>>-------------------------<<##

# hour, minute, second = map(int, input().split(','))

# elapsed_time = int(input())

# total_seconds = hour * 3600 + minute * 60 + second + elapsed_time
# new_seconds = total_seconds % (24 * 3600)
# new_hour = new_seconds // 3600
# new_minute = (new_seconds % 3600) // 60
# new_second = new_seconds % 60

# print(new_hour, new_minute, new_second)

##>>-------------------------<<##

# m = int(input())
# apple1 = m % 3
# apple4 = (m // 3) * 4
# total_apple = apple1 + apple4
# print(total_apple)


##>>-------------------------<<##

# start_hour, start_minute, start_second = map(int, input().split(','))
# end_hour, end_minute, end_second = map(int, input().split(','))
# duration_seconds = (end_hour - start_hour) * 3600 + (end_minute - start_minute) * 60 + (end_second - start_second)
# print(duration_seconds)

##>>-------------------------<<##

# a0=float(input())
# r=int(input())
# n=float(input())
# total=a0*pow((1+n),r)
# print("{:.2f}".format(total))

##>>-------------------------<<##

# num = int(input())
# binary_num = f"0b{bin(num)[2:]}"
# hexadecimal_num = f"0x{hex(num)[2:]}"
# octal_num = f"0o{oct(num)[2:]}"
# print(f"{num} {binary_num} {hexadecimal_num} {octal_num}")

##>>-------------------------<<##

# from fractions import Fraction
# num1, den1 = map(int, input().split(','))
# fraction1 = Fraction(num1, den1)
# num2, den2 = map(int, input().split(','))
# fraction2 = Fraction(num2, den2)
# result1 = fraction1 + fraction2
# result2 = fraction1 - fraction2
# result3 = fraction1 * fraction2
# result4 = fraction1 / fraction2
# print(str(result1), str(result2), str(result3), str(result4), sep=',')

##>>-------------------------<<##

x, n = map(float, input().split(','))
y = 5 * x**(n+1) + (7/9) * x**n - 8 * x**(n-1)
print(f"{y:.5f}")