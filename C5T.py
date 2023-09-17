# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 08:29:22 2023

@author: Jason_Stephen
"""


# word = input()
# if word == word[::-1]:
#     print("Yes.")
# else:
#     print("No.")

##>>-------------------------<<##

# fs,income = map(int, input().split(','))
# tax_rate = 0
# if income >= 500000:
#     tax_rate = 0.30
# elif 100000 <= income < 500000:
#     if fs > 3:
#         tax_rate = 0.15
#     else:
#         tax_rate = 0.2
# elif 30000 <= income < 100000:
#     if fs >= 5:
#         tax_rate = 0.05
#     elif fs >= 3:
#         tax_rate = 0.07
#     else:
#         tax_rate = 0.1
# else:
#     tax_rate = 0
# tax =income * tax_rate
# print("%.2f" % tax)

##>>-------------------------<<##

# operand1 = int(input())
# operator = input()
# operand2 = int(input())

# if operator == '+':
#     result = operand1 + operand2
# elif operator == '-':
#     result = operand1 - operand2
# elif operator == '*':
#     result = operand1 * operand2
# elif operator == '/':
#     result = operand1 // operand2
# elif operator == '%':
#     result = operand1 % operand2
# elif operator == '**':
#     result = operand1 ** operand2
# else:
#     print("无效的运算符")

# result = int(result)

# print(result)

##>>-------------------------<<##

# number = int(input())
# if 100 <= number <= 999:
#     digit1 = number // 100
#     digit2 = (number % 100) // 10
#     digit3 = number % 10
#     sum_of_cubes = digit1**3 + digit2**3 + digit3**3

#     if sum_of_cubes == number:
#         print("Yes.")
#     else:
#         print("No.")
# else:
#     print("请输入一个3位数。")

##>>-------------------------<<##

# n = int(input())
# if n % 2 == 0:
#     min_heads = n // 4
#     if n % 4 > 0:
#         min_heads += 1
#     max_heads = n // 2
#     print(f"{min_heads} {max_heads}")

##>>-------------------------<<##

# year = int(input())
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print("Yes.")
# else:
#     print("No.")

##>>-------------------------<<##

# x = input()
# y = int(input())

# char_to_value = {'A': 1, 'a': -1, 'B': 2, 'b': -2, 'C': 3, 'c': -3, 'D': 4, 'd': -4, 'E': 5, 'e': -5,
#                  'F': 6, 'f': -6, 'G': 7, 'g': -7, 'H': 8, 'h': -8, 'I': 9, 'i': -9, 'J': 10, 'j': -10,
#                  'K': 11, 'k': -11, 'L': 12, 'l': -12, 'M': 13, 'm': -13, 'N': 14, 'n': -14, 'O': 15,
#                  'o': -15, 'P': 16, 'p': -16, 'Q': 17, 'q': -17, 'R': 18, 'r': -18, 'S': 19, 's': -19,
#                  'T': 20, 't': -20, 'U': 21, 'u': -21, 'V': 22, 'v': -22, 'W': 23, 'w': -23, 'X': 24,
#                  'x': -24, 'Y': 25, 'y': -25, 'Z': 26, 'z': -26}

# if x in char_to_value:
#     result = char_to_value[x] + y
# else:
#     result = y
# print(result)

##>>-------------------------<<##

# year, month, day = map(int, input().split(','))
# if month < 1 or month > 12 or day < 1:
#     print("日期不合法。")
# else:
#     if month == 2:
#         if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#             max_day = 29
#         else:
#             max_day = 28
#     elif month in (4, 6, 9, 11):
#         max_day = 30
#     else:
#         max_day = 31

#     if day < max_day:
#         next_day = day + 1
#         next_month = month
#         next_year = year
#     else:
#         next_day = 1
#         if month < 12:
#             next_month = month + 1
#             next_year = year
#         else:
#             next_month = 1
#             next_year = year + 1

#     print(f"{next_year},{next_month},{next_day}")




# year, month, day = map(int, input().split(','))
# if month < 1 or month > 12 or day < 1:
#     print("日期不合法。")
# else:
#     if day > 1:
#         prev_day = day - 1
#         prev_month = month
#         prev_year = year
#     else:
#         if month > 1:
#             prev_month = month - 1
#             prev_year = year
#             if prev_month in (4, 6, 9, 11):
#                 prev_day = 30
#             elif prev_month == 2:
#                 if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#                     prev_day = 29
#                 else:
#                     prev_day = 28
#             else:
#                 prev_day = 31
#         else:
#             prev_year = year - 1
#             prev_month = 12
#             prev_day = 31

#     print(f"{prev_year},{prev_month},{prev_day}")

##>>-------------------------<<##

date1 = input().split(',')
date2 = input().split(',')

date1 = [int(x) for x in date1]
date2 = [int(x) for x in date2]

if date1[0] < date2[0]:
    result = 1
elif date1[0] > date2[0]:
    result = -1
else:
    if date1[1] < date2[1]:
        result = 1
    elif date1[1] > date2[1]:
        result = -1
    else:
        if date1[2] < date2[2]:
            result = 1
        elif date1[2] > date2[2]:
            result = -1
        else:
            result = 0

print(result)






