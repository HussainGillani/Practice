# '''Write a program that asks the user for a number, and then reports whether the number is a
# multiple of 10 or not.'''
# print("Task 1")
# num = int(input("Please enter a number:"))
# if num%10==0:
#     print("The number is multiple of 10")
# else:
#     print("The number is not multiple of 10")
# '''Your system only accepts the odd number, So take a number from the user as input and
# check if it is an even number or odd. Print the result as “Accepted” if the input is odd and “Rejected”
# if the input is even.'''
# print("Task 2")
# num = int(input("Please enter a  number:"))
# if num%2== 0:
#     print("Rejected")
# else:
#     print("Accepted")

# '''Write a program that asks the user how many people are in their dinner group. If the answer
# is more than eight, print a message saying they'll have to wait for a table. Otherwise, report that
# their table is ready.'''
# print('Task 3')
# people =int(input("Please enter thr number of persons:"))
# if people>8:
#     print("You'll have to wait!")
# else:
#     print("Your table is ready") 

# '''A movie theater charges different ticket prices depending on a person's age. If a person is
# under the age of 3, the ticket is free; if they are between 3 and 12, the ticket is $10; and if they are
# over age 12, the ticket is $15. (Age should not be less than 1)'''
# print("Task 4")
# age = int(input("Please enter your age:"))
# if age<3:
#     print("The ticket is free")
# elif age>3 and age<12:
#     print("The ticket is $10")
# else:
#     print("The ticket is $15")

# print("Task5")
# var1 = int(input("Please enter thge first number:"))
# var2 = int(input("Please enter thge second number:"))
# var3 = int(input("Please enter thge third number:"))
# var4 = int(input("Please enter thge fourth number:"))
# var5 = int(input("Please enter thge fifth number:"))
# list = [var1,var2,var3,var4,var5]

# if list%2==0:
    # print("The sum of all variables is ",)
# '''Write a program that takes a students score (0-100) and attendance status (yes/no). If the
# score is greater than or equal to 70 and the attendance is &quot;yes,&quot; print &quot;Pass.&quot; Otherwise, print &quot;Fail.&quot;'''
# print('Task 6')
# score = int(input("Please enter your scorefrom 1-100 :"))
# attendence = input('Please answer yes/no if were present in your exam: ')
# if score>=70 and attendence=="yes":
#     print("Pass")
# else:
#     print("Fail")

# '''Write a program that asks a user for their credit score (a number between 300 and 850) and
# their income. Determine if they are eligible for a credit card based on the following criteria:
#  Credit score must be at least 700.
#  Income must be at least $30,000.
# Print &quot;Approved&quot; if they meet both criteria; otherwise, print &quot;Not approved.&quot;'''

# print("Task 7")
# score = int(input("Please enter your credit score from  300-850:"))
# income = int(input("Please enter your income :"))
# if score>=700 and income>=30000:
#     print("Approved")
# else:
    # print("Denied")

# '''Build a program that asks the user to enter the price of a product and whether they have a
# discount coupon (yes/no). If the price is greater than $100 or they have a coupon, apply a 15%
# discount; otherwise, apply no discount. Print the final amount they need to pay.'''
# print("Task8")
# price = int(input("Please enter the price of the item:"))
# coupen = input("Answer yes/no if you have discount coupen:")
# if price>100 or coupen== "yes":
#     discount = 0.15*price
#     discounted_price= price-discount
#     print("you'll have discount of 15 percent and now your bill is:", discounted_price)
# else:
#     print("your bill is:", price)

