# ''' Write a function named as String_length(arg1) that takes a string as input argument and returns
# the length of the string. (Use built-in function len())'''
# print("Task 1")
# def String_length(arg1):
#     return(len(arg1))
# string = input("Please enter a string:")
# var = String_length(string)
# print(var)

# ''' Write a function named Concatenate (arg1, arg2) that takes two strings as input arguments and
# returns the concatenated string.'''
# print("Task 2 ")
# def concatinate(arg1,arg2):
#     add = arg1+" "+arg2
#     return(add)
# string1 = input("Please enter first string:")
# string2 = input("Please enter second string:")
# var = concatinate(string1,string2)
# print(var)

''' Write a function named first_last (arg1) that takes a string as input argument and returns the
first and last character of the string.'''
# print("Task 3")
# def first_last(arg1):
#     first = arg1[0]
#     last = arg1[-1]
#     return(f"first = {first} and last = {last}")
# string = input("Please enter a string:")
# print(first_last(string))

# '''Write a function named sliced (arg1, arg2) that takes two input argument. First is the string and
# second is an integer. The integer represents the number of characters from the 0th index to that index.
# You need to return the sliced string from the 0th to that integer.'''
# print("Task 4")
# def sliced(arg1,arg2):
#     sliced_string = arg1[0:arg2]
#     return(sliced_string)
# string = input("Please enter a string:")
# integer = int(input("Please enter an integer"))
# print(sliced(string,integer))

# ''' Write a function named palindrome(arg1) that takes an input argument. The function returns True
# if the word is a palindrome and False if the word is not palindrome. A palindrome is a word that is read
# the same as the original. Observe the following example:'''
# print("Task 5")
# def palindrome(arg1):
    
#     if arg1 == arg1[::-1]:
#         return True
#     else:
#        return  False
# var = input("Please enter a string:")
# print(palindrome(var))

