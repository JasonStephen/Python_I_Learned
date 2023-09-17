# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 11:44:49 2023

@author: Jason_Stephen
"""

# input_string = input()
# title_case_string = input_string.title()
# print(title_case_string)

##>>-------------------------<<##

# country1 = input()
# country2 = input()
# sorted_countries = sorted([country1, country2])
# output_string = ','.join(sorted_countries)
# print(output_string)

##>>-------------------------<<##

# name = input()
# result = '*'.join(name)
# print(result)

##>>-------------------------<<##

# sentence1 = input()
# sentence2 = input()
# combined_string = sentence1.strip() + sentence2.strip()
# print(combined_string)

##>>-------------------------<<##

# input_string = input()
# output_string = input_string.strip('*')
# print(output_string)

##>>-------------------------<<##

# input_string = input()
# output_string = input_string.replace('*','')
# print(output_string)

##>>-------------------------<<##

# lower_case_char = input()

# if lower_case_char.islower() and len(lower_case_char) == 1:
#     upper_case_char = chr(ord(lower_case_char) - 32)
    
#     print(upper_case_char)

##>>-------------------------<<##

# sentence = input()
# sentence = sentence.strip()
# words = sentence.split()
# word_count = len(words)
# print(word_count)

##>>-------------------------<<##

sentence = input()

word = input()

if word in sentence:
    print("Yes.")
else:
    print("No.")