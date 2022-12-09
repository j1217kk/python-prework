# Question 1
# Write a function to print "hello_USERNAME!" USERNAME is the input of function. 
def hello_name(user_name):
    '''Displays a greeting with a name'''
    print(f"hello_{user_name}!")

hello_name('USERNAME')


# Question 2
# Write a python function, first_odds
# first_odds prints the odd numbers from 1-100 and returns nothing
def first_odds():
    '''Displays odd numbers 1-100'''
    for x in range(1, 101):
        if x % 2 != 0:
            print(x)

first_odds()
# check for returns nothing
print(first_odds())


# Question 3
# Please write a Python function, max_num_in_list
# max_num_in_list should return the max number of a given list.
def max_num_in_list(a_list):
    '''Returns the max number of a given list'''
    return max(a_list)

# print result of max_num_in_list(a_list) to check for accuracy
print(max_num_in_list([1, 5, 10, 3, 55, 30, 39, 100.0, 40000, 5000]))


# Question 4
# Write a function to return if the given year is a leap year. 
# A leap year is divisible by 4 & not divisible by 100, unless divisible by 400. 
# The return should be boolean Type (true/false).
def is_leap_year(a_year):
    '''Checks if given year is a leap year'''
    if (a_year % 4 == 0) and (a_year % 100 != 0):
        return True
    elif (a_year % 400 == 0):
        return True
    else:
        return False

# check for leap years, should print True True False
print(is_leap_year(2000))
print(is_leap_year(2020))
print(is_leap_year(1999))


# Question 5
# Write function to check to see if all numbers in list are consecutive numbers
# For example, [2,3,4,5,6,7] are consecutive numbers,
# but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.
def is_consecutive(a_list):
    '''Checks if all given numbers are in consecutive order'''
    if sorted(a_list) == list(range((min(a_list)), (max(a_list) + 1) )):
        return True
    else:
        return False

# check/test
print(is_consecutive([1,2,3,4,5,6,7,8,9,10]))
print(is_consecutive([1,2,3,6,7,8,9,10]))
        




