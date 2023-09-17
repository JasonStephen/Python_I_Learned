# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# def print_pattern(n):
#     for i in range(n):
#         spaces = " " * (n - i - 1)
#         if i == 0:
#             print(spaces + "*")
#         else:
#             stars = "*" + " " * (2 * i - 1) + "*"
#             print(spaces + stars)
    
#     for i in range(n - 2, -1, -1):
#         spaces = " " * (n - i - 1)
#         if i == 0:
#             print(spaces + "*")
#         else:
#             stars = "*" + " " * (2 * i - 1) + "*"
#             print(spaces + stars)

# print_pattern(6)

##>>-------------------------<<##

# def print_pattern(n):
#     for i in range(1, n + 1):
#         line = "A" * i
#         print(line)

# print_pattern(6)

##>>-------------------------<<##

# num = input()
# num = float(num)

# result = num * 1.6
# print(result)

##>>-------------------------<<##

# a = input()
# a = int(a)
# b = input()
# b = int(b)

# result = a + b
# print(result)

##>>-------------------------<<##

# width = input()
# width = int(width)
# length = input()
# length = int(length)

# area = width * length
# circum = 2 * (width + length)
# print(width,length,area,circum,sep=",",end="")

##>>-------------------------<<##

# dividend = int(input())
# divisor = int(input())


# quotient = dividend // divisor
# remainder = dividend % divisor


# print(quotient,remainder,sep=" ",end="")

##>>-------------------------<<##

# import math

# radius = float(input())

# area = round(math.pi * radius ** 2, 2)
# circumference = round(2 * math.pi * radius, 2)

# print(f"{radius:.2f} {area:.2f} {circumference:.2f}")

##>>-------------------------<<##

# y,m,d = eval(input())
# h,minute,second = eval(input())

# print(y,m,d,sep="/",end =" ")
# print(h,minute,second,sep=":")

##>>-------------------------<<##

# name  = input().strip()
# count = int(input())
# rname = name * count
# print(rname)

##>>-------------------------<<##

tax_rate = 0.05

for _ in range(3):
    name = input()
    income = float(input())

    tax = income * tax_rate

    print(f"{name:<25} {income:>15.2f} {tax:>15.2f}")


