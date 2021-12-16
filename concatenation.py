# first_name = input("Enter your first name : ")
# # middle_name = input("Enter your middle_name : ")
# last_name = input("Enter your last name : ")
# #
# age = int(input("Enter your age : "))
# # # age = input("Enter your age : ")
# #
# full_name = first_name.upper() + ' ' + last_name.lower()
# #
# # print("Your name is ", full_name)
# # print(full_name, ", your age is ", age)
# #
# if age == 18:
#     print(full_name, "you are going to be a genius")
# elif age < 18:
#     print(full_name, "go to collage")
# else:
#     print(full_name, "you are a genius")
# print(first_name.find('u'))
# print(first_name.replace("k", "q"))
# print("q" in first_name)
# print("k" in first_name)

# number = int(input("enter number :"))
#
# print(not number > 10)

# number = 1
#
# while number <= 10:
#     print(number * '*')
#     number = number + 1

# from math import sqrt
#
# print(sqrt(225))

# number = 1
# pyramidRange = int(input("enter range : "))
#
# while number in range(pyramidRange):
#     print(number * '*')
#
#     number = number + 1


# def triangle(pyramidRange):
#     # number of spaces
#     k = pyramidRange - 1
#
#     # outer loop to handle number of rows
#     for i in range(0, pyramidRange):
#
#         # inner loop to handle number spaces
#         # values changing acc. to requirement
#         for j in range(0, k):
#             print(end=" ")
#
#         # decrementing k after each loop
#         k = k - 1
#
#         # inner loop to handle number of columns
#         # values changing acc. to outer loop
#         for j in range(0, i + 1):
#             # printing stars
#             print("* ", end="")
#
#         # ending line after each row
#         print("\r")
#
#
# # Driver Code
#
# pyramidRange = int(input("enter range : "))
# triangle(pyramidRange)


# def contalpha(n):
#     # initializing value corresponding to 'A'
#     # ASCII value
#     num = 65
#
#     # outer loop to handle number of rows
#
#     for i in range(0, n):
#
#         # inner loop to handle number of columns
#         # values changing acc. to outer loop
#         for j in range(0, i + 1):
#             # explicitely converting to char
#             ch = chr(num)
#
#             # printing char value
#             print(ch, end=" ")
#
#             # incrementing at each column
#             num = num + 1
#
#         # ending line after each row
#         print("\r")
#
# # Driver code
# n = 7
# contalpha(n)


# def contnum(n):
#     # initializing starting number
#     num = 1
#
#     # outer loop to handle number of rows
#     for i in range(0, n):
#
#         # not re assigning num
#         # num = 1
#
#         # inner loop to handle number of columns
#         # values changing acc. to outer loop
#         for j in range(0, i + 1):
#             # printing number
#             print(num, end=" ")
#
#             # incrementing number at each column
#             num = num + 1
#
#         # ending line after each row
#         print("\r")
#
#
# n = 10
#
# # sending 5 as argument
# # calling Function
# contnum(n)


rows = int(input("Enter number of rows: "))

for i in range(rows, 1, -1):
    for space in range(0, rows-i):
        print("  ", end="")
    for j in range(i, 2*i-1):
        print("* ", end="")
    for j in range(1, i-1):
        print("* ", end="")
    print()