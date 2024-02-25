'''Write a program that asks the user for his first name and last name. Concatenate both of the
strings and print the full name of the user.'''
print("Task 1")
first_name = input("Please enter your first name:")
last_name = input("Please enter your last name:")
concatinate = first_name.capitalize() +" "+ last_name.capitalize()
print(concatinate)


# '''Your system only accepts the names having odd number of characters and the length more than
# 3 character, so take a name from the user as input and check if it is an even number or odd number of
# characters in it and the required character length. Print the result as “Accepted” if the input meets the
# requirement and “Rejected” if otherwise.'''
# print("Task 2")
# name = input("Please enter your name:")
# if len(name)>3 and len(name)%2!=0:
#     print("Accepted")
# else:
#     print("Rejected")

# '''You are required to make a modern machine that takes the input from the user in lower case and
# prints the same input to the upper case. Write a code that takes the input from the user in lower case and
# prints in the upper case.'''
# print("Task 3")
# string = input("Please enter a string in lowercase:")
# print(string.upper())

# '''A Client has asked you to make an analytical App that take a sentence from the user as input and
# prints how many times the vowels occurred in the sentence:'''
# print("Task 4")
# string = input("Please enter a string:")
# lower_string = string.lower()
# print("Number of a",lower_string.count("a"))
# print("Number of e",lower_string.count("e"))
# print("Number of i",lower_string.count("i"))
# print("Number of o",lower_string.count("o"))
# print("Number of u",lower_string.count("u"))

# '''Write a program that takes a sentence from the user as input. And split the sentence and print all
# of the words available in the input.'''
# print("Task 5")
# string = input("Please enter a string:")
# split_string = string.split()
# print(split_string)

# '''Let's make an abuse filter machine. Write a program that takes a sentence from the user as input.
# check if there is any abusive word in it. The filter will accept the sentence if there is no abuse in the
# sentence and reject the sentence otherwise. Consider that following list of abuse:'''
# print('Task 6')
# string = input("Please enter a string sentence:").lower()
# abusive_words =["sad,kill,die"]
# if string.count("sad"):
#     print("Rejected")
# elif string.count("kill"):
#     print("Rejected")
# elif string.count("die"):
#     print("Rejected")
# else:
#     print("Accepted")