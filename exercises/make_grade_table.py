"""
Template - Create a function make_grade_table(name_list, grades_list)
whose keys are the names in names and whose values are the
lists of grades in grades
"""


# Add code here

def make_grade_table(name_list, grades_list):
    """
    Given a list of name_list (as strings) and a list of grades
    for each name, return a dictionary whose keys are
    the names and whose associated values are the lists of grades
    """

    # pass
    grade_dict = {}

    for name, grades in zip(name_list, grades_list):
        grade_dict[name] = grades
    return grade_dict


def make_grade_table_simple(name_list, grades_list):
    grade_dict = {name : grades for name, grades in zip(name_list, grades_list)}
    return grade_dict


# Tests
print(make_grade_table([], []))

name_list = ["Bryant", "Aiden", "Emma"]
grades_list = [100, 98, 100, 100], [100, 100, 99, 100], [100, 100, 100, 100]
print(make_grade_table(name_list, grades_list))

print(make_grade_table_simple([], []))
print(make_grade_table_simple(name_list, grades_list))
# Output
# {}
# {'Bryant': [100, 98, 100, 100], 'Aiden': [100, 100, 99, 100], 'Emma': [100, 100, 100, 100]}

