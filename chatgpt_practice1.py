
# #  **SECTION 1 — VARIABLES & BASIC PRINTING (1–10)**

# ### **1. Print Hello**

# # **Instruction:** Print `"Hello, Python!"`
# # **Input:** —
# # **Output:**

# # ```
# # Hello, Python!

# def print_hello():
#     print("Hello, Python!")

# print_hello()

# ### **2. Print a Name**

# **Instruction:** Ask for a name and print `"Hello, <name>"`
# **Input:**

# ```
# Andres
# ```

# **Output:**

# ```
# Hello, Andres

# def print_name():
#     name = input("What is your name? ")
#     print(f"Hello, {name}")

# print_name()

# ### **3. Add Two Numbers**

# **Instruction:** Read two integers and print their sum.
# **Input:**

# 5
# 7
# ```

# **Output:**

# ```
# 12

# def two_numbers():
#     num_one = input("provide the first number ")
#     num_two = input("provide the second number ")

#     total = int(num_one) + int(num_two)
#     print(total)

# two_numbers()

# def num_sums(num_one, num_two):
#     sum_total = num_one + num_two
#     print(sum_total)

# num_sums(3,4)



# ### **4. Multiply Two Numbers**

# **Instruction:** Multiply two input numbers.
# **Input:**

# ```
# 3
# 4
# ```

# **Output:**

#  12

# def multiply_nums():
#     num_a = input("provide the first number ")
#     num_b = input("provide the second number ")

#     result = int(num_a) * int(num_b)
#     print(result)

# multiply_nums()

# ### **5. Subtract**

# **Instruction:** Subtract second number from first.
# **Input:**

# ```
# 10
# 4
# ```

# **Output:**

# ```
# 6
# ```

# def substract_numbers(a, b):
#     result = a - b
#     print(result)

# substract_numbers(8,3)

# def num_sub():
#     num_a = input("provide a number ")
#     num_b = input("provide another number ")
#     sub_result = int(num_a) - int(num_b)
#     print(sub_result)

# num_sub()


# ### **6. Square a Number**

# **Instruction:** Print the square of a number.
# **Input:**

# ```
# 6
# ```

# **Output:**

# ```
# 36
# ```

# def square_a_number():
#     num = input("provide a number ")
#     result = int(num) ** 2
#     print(result)

# square_a_number()

# ### **7. String Repeat**

# **Instruction:** Read a word and print it 3 times.
# **Input:**

# ```
# Python
# ```

# **Output:**

# ```
# PythonPythonPython
# #
# def print_3_times():
#     word = "Python"
#     print(word * 3)

# print_3_times()



# ### **8. Age in 10 Years**

# **Instruction:** Ask age; print age + 10.
# **Input:**

# ```
# 20
# ```

# **Output:**

# 30

# def ask_age():
#     age = int(input("provide the age "))
#     result = age + 10
#     print(result)

# ask_age()


# ### **9. Convert Minutes to Seconds**

# **Instruction:** Convert minutes to seconds (min * 60).
# **Input:**

# 5


# **Output:**

# ```
# 300

# def minutos_to_seconds():
#     num = int(input("insert the minutes "))
#     result = num * 60
#     print(result)

# minutos_to_seconds()

# ### **10. Simple Greeting**

# # **Instruction:** Ask for first and last name; print them together.
# # **Input:**

# # ```
# # John
# # Doe
# # ```

# # **Output:**

# # ```
# # John Doe
# # ```
# def full_name():
#     f_name = input("please provide your Fisrt Name ")
#     l_name = input("please provide your Last Name ")

#     result = f_name + " " + l_name
#     print(result)

# full_name()

# # 🔵 **SECTION 2 — IF STATEMENTS (11–25)**

# ### **11. Odd or Even**

# **Instruction:** Determine if number is odd or even.
# **Input:** `7`
# **Output:**

# ```
# Odd

# def odd_even():
#     num = input("provide a number ")
#     num_int = int(num)

#     if num_int % 2 == 0:
#         print("Even")
#     else:
#         print("Odd")

# odd_even()

# # ### **12. Positive or Negative**

# # **Input:** `-5`
# # **Output:**

# # ```
# # Negative

# def positive_negative():
#     num = int(input("provide a number "))

#     if num < 0:
#         print("Negative")
#     else:
#         print("Positive")

# positive_negative()

# # ### **13. Grade Check**

# # **Instruction:** If score ≥ 60 print `"Pass"`, else `"Fail"`.
# # **Input:** `45`
# # **Output:**

# # ```
# # Fail

# def grade_check():
#     score = int(input("provide your score "))
#     if  score >= 60:
#         print("Pass")
#     else:
#         print("Fail")

# grade_check()

# ### **14. Compare Two Numbers**

# Input:

# ```
# 8
# 3
# ```

# Output:

# 8 is greater

# def compare_two_numbers():
#     num_a = int(input("insert a number "))
#     num_b = int(input("insert another number "))

#     if num_a > num_b:
#         print(f"{num_a} is greater")
#     else:
#         print(f"{num_b} is greater")

# compare_two_numbers()

# # ### **15. Max of Three** terminar este ejercicio

# # Input:

# # ```
# # 2
# # 9
# # 5
# def max_of_three():
#     num_a = 2
#     num_b = 9
#     num_c = 5

#     result = max(num_a, num_b, num_c)
#     print(result)

# max_of_three()



# ### **16. Divisible by 5**

# Input: `20`
# Output:

# ```
# Divisible

# def divisible_by_5():
#     num = int(input("insert a number "))
#     if num % 5 == 0:
#         print("Divisible")
#     else:
#         print("Not divisible")
    
# divisible_by_5()

# # ### **17. Teenager Check**

# # Input: `14`
# # Output:

# # Teenager

# def teen_ager_check():
#     age = int(input("please insert the age "))
#     if 10 <= age <= 19:
#         print("Teenager")
#     else:
#         print("Not a Teenager")

# teen_ager_check()

# # ### **18. Number Category**

# # Instruction: Print `"small"` if <10, `"medium"` if <50, `"large"` otherwise.
# # Input: `34`
# # Output:
# # medium

# def num_category():
#     num = int(input("insert a number "))
#     if num < 10:
#         print("small")
#     elif num < 50:
#         print("medium")
#     else:
#         print("large")

# num_category()

# # ### **19. Letter Grade**

# # Instruction: Convert score to A/B/C/D/F.
# # Input: `88`
# # Output:
# # B

# def letter_grade():
#     score = int(input("provide the score "))
    
#     if 90 <= score <= 100:
#         print("A")
#     elif 80 <= score <= 89:
#         print("B")
#     elif 70 <= score <= 79:
#         print("C")
#     elif 60 <= score <= 69:
#         print("D")
#     else:
#         print("F")

# letter_grade()

# ### **20. Leap Year**

# Input: `2024`
# Output:
# Leap year





# ### **21. Temperature Check**

# Input: `100`
# Output:

# ```
# Hot

# def temp_check():
#     temp = int(input("insert the temperature "))

#     if temp >= 100:
#         print("Hot")
    

# temp_check()

# ### **22. Login Simple**

# Instruction: Username=admin, password=1234
# Input:

# # ```
# # admin
# # 1234
# # Output:
# # Access granted

# def login_simple():
#     username = "admin"
#     password = "1234"

#     user_n = input("insert your username ")
#     p_word = input("insert your password ")

#     if user_n == username and p_word == password:
#         print("Access granted")
#     else:
#         print("Access declined")

# login_simple()


# # ### **23. Absolute Value**

# # Input: `-9`
# # Output:

# # ```
# # 9
# # ```

# def absolute_value():
#     num = int(input("insert a number "))

#     if num < 0:
#         print(num * (-1))
#     else:
#         print(num)

# absolute_value()

# # ### **24. Multiple of 3**

# # Input: `7`
# # Output:

# # ```
# # No
# # ```

# def mult_of_3():
#     num = int(input("insert a number "))
#     if num % 3 == 0:
#         print("Yes")
#     else:
#         print("No")

# mult_of_3()


# # ### **25. Check Word Length**

# # Input: `hello`
# # Output:

# # ```
# # 5

# def check_word_length():
#     word = input("insert a word ")
#     l_word = len(word)
#     print(l_word)

# check_word_length()

# # 🔵 **SECTION 3 — LOOPS (26–50)**

# ### **26. Print 1–10** 

# Output:

# ```
# 1 2 3 4 5 6 7 8 9 10


# print_one_to_ten()

# def print_one_to_ten():
    
#     for i in range(1, 11):
#         print(i, end=" ")
    
    # print_one_to_ten()

# # ### **27. Print Even Numbers 1–20**

# # Output:

# # ```
# # 2 4 6 8 10 12 14 16 18 20
# # ```
# def even_numbers():
#     for i in range(1 ,21):
#         if i % 2 == 0:
#             print(i, end=" ")

# even_numbers()


# ### **28. Sum 1–100**

# Output:

# ```
# 5050
# ```
# def sum_one_to_hundred():
#     nums = []
#     for i in range(1, 101):
#         nums.append(i)
#     result = sum(nums)
#     print(result)

# sum_one_to_hundred()

# # ### **29. Countdown** n

# # Input: `5`
# # Output:

# # 5 4 3 2 1

# def countdown():
#     num = 5
#     for i in range(num,0,-1):
#         print(i, end = " ")

# countdown()


# ### **30. Multiplication Table of N**

# # Input: `3`
# # Output:

# # ```
# # 3 6 9 12 15 18 21 24 27 30
# def mutl_table():
#     n = int(input("insert a number "))
#     for i in range(1,11):
#         result = n * i
#         print(result, end=" ")

# mutl_table()

# ### **31. Word 5 Times**  

# # Input: `Hi`
# # Output:

# # ```
# # Hi
# # Hi
# # Hi
# # Hi
# # Hi

# def word_five_times():
#     word = "Hi"
#     for i in range(5):
#         print(word)

# word_five_times()


# ### **32. Factorial** me falto

# Input: `5`
# Output:
# 120

# # ### **33. Characters of String**

# # Input:

# # ```
# # cat
# # ```

# # Output:

# # ```
# # c
# # a
# # t
# # ```
# #
# def char_str():
#     word = input("insert a word ")
#     for i in word:
#         print(i)

# char_str()






# # ### **34. 10 Random Numbers (don't generate—just loop)** no lo pude resolver

# # Output:

# # ```
# # 0
# # 1
# # 2
# # 3
# # ...
# # 9
# # 



# ### **35. Sum of Digits**

# Input: `1234`
# Output:

# ```
# 10
# def sum_of_digits():
#     num = input("insert a number ")
#     result = 0
#     for i in num:
#         result += int(i)

#     print(result)

# sum_of_digits()





# # ### **36. Reverse a String Using Loop** no lo pude resolver

# # Input: `hello`
# # Output:

# # ```
# # olleh


# ### **37. Count Vowels**

# Input: `banana`
# Output:
# 3

        



# ### **38. Print Squares 1–10** 

# Output:

# ```
# 1 4 9 16 25 36 49 64 81 100

# def print_square():
#     for i in range(1, 11):
#         print(i ** 2, end = " ")
        

# print_square()

# ### **39. 

# Output:

# ```
# 1 2 3 4

# def break_on_num():
#     i = 1
#     while i < 10:
#         print(i, end = " ")
#         if (i == 5):
#             break
#         i +=1

# break_on_num()

# ### **40. Continue on Number 5**

# Output:

# ```
# 1 2 3 4 6 7 8 9 10

# def cont_on_num():
#     i = 0
#     while i < 10:
#         i +=1
#         if i == 5:
#             continue
#         print(i, end = " ")

# cont_on_num()

# ### **41. Print Range of Numbers**

# Input:

# ```
# 3
# 8
# ```

# Output:

# ```
# 3 4 5 6 7 8
# def rang_of_nums():
#     for i in range(3,8):
#         print(i, end=" ")

# rang_of_nums()



# ### **42. Count Down by 2**

# Input: `10`
# Output:

# ```
# 10 8 6 4 2

# def count_down():
#     for i in range(10,1,-2):
#         print(i, end =" ")

# count_down()

# # ### **43. Multiply All Numbers in List** no lo pude resolver ----

# # Input: `[2,3,4]`
# # Output:

# # 24
# def mult_nums():
#     num = [2, 3, 4]
#     total = 1

#     for i in num:
#         total *= i
#     print(total)

# mult_nums()

# ### **44. Sum All Even Numbers in List** me costo no pude 

# Input: `[1,2,3,4,5,6]`
# Output:

# 12
# def sum_even_nums():
#     f_list = [1, 2, 3, 4, 5, 6]
#     n_list = []

#     for i in f_list:
#         if i % 2 == 0:
#             n_list.append(i)
#             result = sum(n_list)


#     print(n_list) 

# sum_even_nums() / este es mi codigo esta mal

# def sum_even_nums():
#     f_list = [1, 2, 3, 4, 5, 6]
#     n_list = []

#     for i in f_list:
#         if i % 2 == 0:
#             n_list.append(i)

#     result = sum(n_list)
#     print(result)

# sum_even_nums() codigo corregido



# ### **45. Find Minimum in List**

# Input: `[5,1,9,2]`
# Output:

# 1

# def find_min():
#     nums = [5, 1, 9, 2]
#     nums.sort()
#     print(nums[0])



# find_min()





# ### **46. Count Words**

# Input: `"I love Python"`
# Output:

# ```
# 3
# ```

# ### **47. Print Indexes of List**

# Input: `[10,20,30]`
# Output:

# ```
# 0 1 2
# ```

# ### **48. Reverse List Manually**

# Input: `[1,2,3]`
# Output:

# ```
# [3,2,1]
# ```

# ### **49. Find First Negative Number**

# Input: `[3,5,-2,8]`
# Output:

# ```
# -2





# ### **50. Largest Word in Sentence**

# Input: `"Python is amazing"`
# Output:

# ```
# amazing
# ```

# ---

# # 🔵 **SECTION 4 — LISTS (51–70)**

# ### **51. Append to List**

# Input:

# ```
# [1,2,3]
# 4
# ```

# Output:


# [1,2,3,4]

# def a_to_list():
#     a = [1,2,3]
#     a.append(4)
#     return a 

# print(a_to_list())

# ### **52. Remove from List**

# Input:

# ```
# [1,2,3,2]
# 2
# ```

# Output:

# ```
# [1,3,2]

# def remove_from_list():
#     a = [1,2,3,2]
#     a.remove(2)
#     return a

# print(remove_from_list())

# ### **53. List Length**

# Input: `[10,20,30,40]`
# Output:

# ```
# 4

# def l_length():
#     a = [10 ,20, 30, 40]
#     return len(a)

# print(l_length())

# ### **54. Check if Item Exists**

# Input:

# [1,2,3]
# 2
#  Output:

# Yes
# ```
# def i_exist():
#     item = [1,2,3]
#     for i in item:
#         if i == 2:
#             print("Yes")

# i_exist()

# ### **55. Replace an Element**

# Input:

# ```
# [5,6,7]
# index:1
# value:99
# def replace_an_item():

#     item = [5, 6, 7]
#     item.pop(1)
#     item.insert(1,99)
#     print(item)

# replace_an_item()


# # ### **56. List Slice 2–5**

# # Input: `[0,1,2,3,4,5,6]`
# # Output:

# # ```
# # [2,3,4,5]

# def slice_list():
#     list_a =[0, 1, 2, 3, 4, 5, 6]
#     print(list_a[2:6])
    

# slice_list()



# # ### **57. Count Occurrences**

# # Input: `[1,2,2,3]`
# # Output:

# # ```
# # 2
# # ```

# def count_occurrence():
#     num_list = [1, 2, 2, 3]
#     occurrence = num_list.count(2)
#     print(occurrence)

# count_occurrence()

# # ### **58. Sort List**

# # Input: `[3,1,4,2]`
# # Output:

# # ```
# # [1,2,3,4]

# def sort_list():
#     o_list = [3, 1, 4, 2]
#     o_list.sort()
#     print(o_list)

# sort_list()

# # ### **59. Reverse List**

# # Input: `[1,2,3]`
# # Output:

# # [3,2,1]

# def rev_list():
#     orig_list = [1, 2, 3]
#     orig_list.reverse()
#     print(orig_list)

# rev_list()

# # ### **60. Merge Two Lists**

# # Input:

# # ```
# # [1,2]
# # [3,4]
# # ```

# # Output:
# # [1,2,3,4]

# def merge_two_lists():
#     list_a = [1, 2]
#     list_b = [3, 4]

#     merged_list = list_a + list_b
#     print(merged_list)

# merge_two_lists()

# ### **61. Remove Duplicates**

# Input: `[1,1,2,2,3]`
# Output:

# [1,2,3]
# ```




# ### **62. Middle Element**

# Input: `[5,6,7]`
# Output:

# ```
# 6
# ```

# ### **63. Rotate Right by One**

# Input: `[1,2,3]`
# Output:

# ```
# [3,1,2]
# ```

# ### **64. Sum of List**

# Input: `[4,5,6]`
# Output:

# ```
# 15
# ```

# ### **65. Product of List**

# Input: `[1,2,3,4]`
# Output:

# ```
# 24
# ```

# ### **66. Convert String to List**

# Input: `"abc"`
# Output:

# ```
# ['a','b','c']

# def str_to_list():
#     word = "abc"
#     new_list = []
    
#     for i in word:
#         new_list.append(i)

#     print(new_list)

# str_to_list()



# ### **67. Convert List to String**

# Input: `['a','b','c']`
# Output:

# abc
# def list_to_string():
#     a = ["a", "b", "c"]
#     str_a = "".join(a)
#     print(str_a)

# list_to_string()

# # ### **68. Find Second Largest**

# # Input: `[3,5,1,8]`
# # Output:

# # 5
# def second_largest():
#     nums = [3, 5, 1, 8]
#     nums.sort()
#     print(nums[-2])
    

# second_largest()


# ### **69. Pair Elements (zip manually)**

# Input: `[1,2],[3,4]`
# Output:

# ```
# (1,3)
# (2,4)
# ```

# ### **70. Remove All Negative Numbers**

# Input: `[3,-1,4,-2]`
# Output:

# ```
# [3,4]

# def remove_negatives():
#     orig_list = [3, -1, 4, -2]
#     new_list = []

#     for i in orig_list:
#         if i >= 0:
#             new_list.append(i)
#     print(new_list)

# remove_negatives()


# # 🔵 **SECTION 5 — STRINGS (71–85)**

# # ### **71. Lowercase**

# # Input: `"HELLO"`
# # Output:

# # ```
# # hello

# def lower_case():
#     wrd = input("insert a word ")
#     result = wrd.lower()

#     print(result)

# lower_case()


# # ### **72. Uppercase**

# # Input: `"hi"`
# # Output:

# # ```
# # HI
# def upper_case():
#     wrd = input("insert a word ")
#     l_word = wrd.upper()
#     print(l_word)

# upper_case()



# # ### **73. Title Case**

# # Input: `"hello world"`
# # Output:

# # Hello World
# def title_case():
#     word = "hello world"
#     result = word.title()
#     print(result)

# title_case()


# # ### **74. Reverse String**

# # Input: `"Python"`
# # Output:

# # nohtyP
# def reverse_str():
#     wrd = "Python"
#     result = wrd[::-1]
#     print(result)

# reverse_str()



# # ### **75. Count Letter**

# # Input: `"banana", "a"`
# # Output:

# # 3
# def count_letter():
#     str_a = "banana"
#     result = str_a.count("a")
#     print(result)

# count_letter()

# # ### **76. Replace Letter**

# # Input: `"hello", "l", "*" `
# # Output:

# # he**o
# def replace_letter():
#     orig_str = "hello"
#     final_str = orig_str.replace("l","*")
#     print(final_str)

# replace_letter()

# # ### **77. Remove Spaces**

# # Input: `"a b c"`
# # Output:

# # abc

# def remove_spaces():
#     original_str = "a b c"
#     result = original_str.replace(" ","")
#     print(result)

# remove_spaces()    


# ### **78. Check Palindrome**

# Input: `"level"`
# Output:

# Yes

# def pal_word():
#     word = "level"
#     reverse_word = word[::-1]
#     print(reverse_word)

#     if word == reverse_word:
#         print("Yes")
#     else:
#         print("No")

# pal_word()


# # ### **79. First and Last Character**

# # Input: `"Python"`
# # Output:

# # P n
# def first_and_last():
#     original_word = "Python"
#     word_one = original_word[0]
#     word_two = original_word[-1]
#     print(word_one, word_two)

# first_and_last()


# # # ### **80. Find Index of Letter**

# # # Input: `"hello", "e"`
# # # Output:

# # # 1


# def find_index():
#    word = "hello"
#    result = word.find("e")
#    print(result)

# find_index()


# # ### **81. Split Sentence**

# # Input: `"I love coding"`
# # Output:

# # ```
# # ['I','love','coding']

# def split_sentence():
#     word = "I love coding"
#     result = word.split()
#     print(result)

# split_sentence()




# ### **82. Join List into String**

# Input: `['I','love','Python']`
# Output:

# ```
# I love Python
# ```

# ### **83. Remove Vowels**

# Input: `"hello"`
# Output:

# ```
# hll
# ```

# ### **84. Count Consonants**

# Input: `"abcde"`
# Output:

# 3




# ### **85. Replace Word**

# Input: `"I like apples", replace 'apples' with 'bananas'`
# Output:

# ```
# I like bananas

# def replace_word():
#     word = "I like apples"
#     result = word.replace("apples", "bananas")
#     print(result)

# replace_word()

# # 🔵 **SECTION 6 — FUNCTIONS (86–100)**

# # ### **86. Function: Add Numbers**

# # Input: `3,7`
# # Output:

# # ```
# # 10
# # ```
# def add_nums():
#     num_a = int(input("insert the first number "))
#     num_b = int(input("insert the second number "))

#     total =num_a + num_b
#     print(total)

# add_nums()



# # ### **87. Function: Square**

# # Input: `5`
# # Output:

# # ```
# # 25
# # ```

# def n_sqr():
#     num = int(input("insert a number "))
#     result = num ** 2
#     print(result)

# n_sqr()

# # ### **88. Function: Max of List**

# # Input: `[3,9,1]`
# # Output:

# # 9
# def max_of_list():
#     list_a = [3, 9, 1]
#     print(max(list_a))
    

# max_of_list()



# ### **89. Function: Count Vowels**

# Input: `"python"`
# Output:

# ```
# 1

    



# # # ### **90. Function: Reverse List**

# # # Input: `[1,2,3]`
# # # Output:

# # # [3,2,1]

# def reverse_list():
#     list_a = [1, 2, 3]
#     list_a.reverse()
#     print(list_a)

# reverse_list()

# def rev_list():
#     orig_list = [1, 2, 3]
#     orig_list.reverse()
#     print(orig_list)

# rev_list()

# ### **91. Function: Multiply All Numbers**

# Input: `[2,3,4]`
# Output:

# 24
# def mult_nums():
#     nums = [2, 3, 4]
#     result = 1

#     for i in nums:
#         result *= i
#     print(result)

# mult_nums()




# ### **92. Function: Check Prime**

# Input: `7`
# Output:
# Prime



# ### **93. Function: BMI Calculator**

# Input:

# ```
# weight: 70
# height: 1.75
# ```

# Output:
# 22.86
# def bmi_calculator():
#     weight = float(input("Insert your weight "))
#     height = float(input("insert your height "))

#     bmi = weight / (height **2)
#     f_result = round(bmi,2)

#     print(f_result)

# bmi_calculator()

# ### **94. Function: Greeting**

# Input: `"Andres"`
# Output:

# ```
# Hello Andres!
# def greeting():
#     name = input("What is your name? ")
#     return f"Hello {name}!"

# print(greeting())

# ### **95. Function: Remove Duplicates**

# Input: `[1,1,2,3]`
# Output:

# ```
# [1,2,3]
# ```

# ### **96. Function: Average**

# Input: `[10,20,30]`
# Output:

# ```
# 20
# ```

# ### **97. Function: Celsius to Fahrenheit**

# Input: `0`
# Output:

# ```
# 32
# def c_to_f():
#     raw_tmp = input("insert the temperature value ")
#     tmp = int(raw_tmp)

#     t_in_f = (tmp * 1.8) + 32
#     print(int(t_in_f))

# c_to_f()

# ### **98. Function: Count Words**

# Input: `"Hello world test"`
# Output:

# 3



# # ### **99. Function: Even Numbers Only**

# # Input: `[1,2,3,4]`
# # Output:

# # ```
# # [2,4]

# def even_nums_only():
#     items = [1, 2, 3, 4]
#     new_items = []

#     for i in items:
#         if i % 2 == 0:
#             new_items.append(i)
    
#     print(new_items)

# even_nums_only()





# ### **100. Function: Fibonacci Nth Number**

# Input: `7`
# Output:

# ```
# 13
# ```

# ---


