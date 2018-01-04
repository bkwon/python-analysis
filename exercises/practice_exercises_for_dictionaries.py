'''
Write an expression that initializes the dictionary my_dict to be an empty dictionary.
'''

"""
Solution - Initialize a dictionary my_dict to be empty
"""

# Add code here
my_dict = {}

# Tests
print(type(my_dict))
print(my_dict)

# Output
#<class 'dict'>
#{}


'''
Write an expression that initializes the dictionary 𝚖𝚢_𝚍𝚒𝚌𝚝 to contain two key/value pairs: 
"Bryant" : 𝟷 and "Tiberius" : 𝟸
'''
# Add code here
my_dict = {"Bryant" : 1, "Tiberius" : 2}

# Tests
print(type(my_dict))
print(my_dict["Bryant"])
print(my_dict["Tiberius"])
print(my_dict)

# Output - note that order of key/values pairs in output is unimportant
#<class 'dict'>
#1
#2
#{'Tiberius': 2, 'Bryant': 1}


'''
Given the dictionary 𝚖𝚢_𝚍𝚒𝚌𝚝 from the previous question, write a Python statement 
that adds the key/value pair "𝙹𝚘𝚑𝚗" : 𝟹 to this dictionary
'''
my_dict["John"] = 3
print(my_dict)


'''
Given the dictionary 𝚖𝚢_𝚍𝚒𝚌𝚝 from the previous question, write three expressions that return 
𝚃𝚛𝚞𝚎 if the dictionary 𝚖𝚢_𝚍𝚒𝚌𝚝 whether the keys "𝙹𝚘𝚎" , "𝚂𝚌𝚘𝚝𝚝" , and "𝙹𝚘𝚑𝚗", respectively, and 𝙵𝚊𝚕𝚜𝚎 otherwise
'''
names = {"Bryant": False, "Tiberius": False, "John": False}
for name in names:
    if name in my_dict:
        print(name in my_dict)
    else:
        print("False: " + name)


'''
Write a function 𝚒𝚜_𝚎𝚖𝚙𝚝𝚢(𝚖𝚢_𝚍𝚒𝚌𝚝) that takes a dictionary 𝚖𝚢_𝚍𝚒𝚌𝚝 and returns 𝚃𝚛𝚞𝚎 if 
𝚖𝚢_𝚍𝚒𝚌𝚝 is empty and 𝙵𝚊𝚕𝚜𝚎 otherwise
'''
# def is_empty(my_dict):
#     if my_dict == {}:
#         return True
#     else:
#         return False

# This can alternatively be written more simply/effectively as:
def is_empty(my_dict):
    return len(my_dict) == 0

# Testing code
print()
print("True or False:")
print(is_empty({}))
print(is_empty({0 : 1}))
print(is_empty(my_dict))


'''
Write a function 𝚟𝚊𝚕𝚞𝚎_𝚜𝚞𝚖(𝚖𝚢_𝚍𝚒𝚌𝚝) that returns the sum of the values in the dictionary 𝚖𝚢_𝚍𝚒𝚌𝚝. 
(You may assume that the values in the dictionary are numbers).
'''
def value_sum(my_dict):
    sum_value = 0
    for key in my_dict:      # for item in my_dict
        sum_value += my_dict[key]
    return sum_value

# Testing code
print(value_sum({}))
print(value_sum({0 : 1}))
print(value_sum(my_dict))

# Output
#0
#1
#6


'''
Write a function 𝚖𝚊𝚔𝚎_𝚍𝚒𝚌𝚝(𝚔𝚎𝚢_𝚟𝚊𝚕𝚞𝚎_𝚕𝚒𝚜𝚝)  that takes a list of tuples 𝚔𝚎𝚢_𝚟𝚊𝚕𝚞𝚎_𝚕𝚒𝚜𝚝 where each 
tuple is of the form (key, value) and returns a dictionary with these keys and corresponding values.
'''
def make_dict(key_value_list):
    """
    Given a list of tuples of the form (key, value),
    return a dictionary with the corresponding keys and values
    """

    # Enter code here
    answer = {}
    for key, value in key_value_list:
        answer[key] = value
    return answer

# Testing code
print(make_dict([]))
print(make_dict([(0, 1)]))
print(make_dict([('Bryant', 1), ('Tiberius', 2), ('John', 3)]))

