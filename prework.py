# Question 1:
# Write a function to print "hello_USERNAME!" USERNAME is the input  of the
# function. The first line of the code has been defined as below.

def hello_name(username):
    """This will display 'hello_USERNAME!'"""
    print("hello_" + username.upper() + "!")

hello_name('username')

# Question 2:
# Write a python function, first_odds that prints the odd numbers from 1-100 and
# returns nothing.

def first_odds(numbers):
    """This displays odd numbers."""
    for number in range(numbers):
        if number % 2 != 0:
            print(number)

first_odds(100)

# Question 3: 
# Please write a Python function, max_num_in_list to return the max number of a
# given list. The first line of the code has been defined as below.

def max_num_in_list(a_list):
    """This will display the max number of a list."""
    print(max(a_list))

numbers = [4, 32, 3, 63, 11, 48]
max_num_in_list(numbers)

# Question 4:
# Write a function to return if the given year is a leap year. A leap year is
# divisible by 4, but not divisible by 100, unless it is also divisible by 400.
# The return should be boolean Type (true/false).

def is_leap_year(a_year):
    """This will determine if input is a leap year."""
    if a_year % 4 == 0 and a_year % 100 != 0:
        return True
    elif a_year % 100 and a_year % 400 == 0:
        return True
    else:
        return False

print(is_leap_year(1900))

# Question 5:
# Write a function to check to see if all numbers in list are consecutive
# numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but[1,2,4,5] are
# not consecutive numbers. The return should be boolean Type.

def is_consecutive(a_list):
    """This will determine if a list has consecutive numbers."""
    if a_list == list(range(min(a_list), max(a_list)+1)):
        return True
    else:
        return False

nums = [21, 22, 23, 25, 26]
print(is_consecutive(nums))