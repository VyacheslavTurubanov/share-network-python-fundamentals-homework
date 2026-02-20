"""
Project: Gradebook
Follow the instructions to practice creating, appending, and modifying Python lists.
"""
from typing import List

# --- Create Some Lists ---

# 1. Create a list called 'subjects' and fill it with the classes you are taking:
# "physics", "calculus", "poetry", "history"
subjects = ["physics", "calculus", "poetry", "history"]


# 2. Create a list called 'grades' and fill it with your scores:
# 98, 97, 85, 88
grades = [98, 97, 85, 88]

# 3. Create a two-dimensional list to combine subjects and grades. 
# Use the table below as a reference for the associated values:
#
# Name          |  Test Score
# ---------------------------
# "physics"     |  98
# "calculus"    |  97
# "poetry"      |  85
# "history"     |  88
#
# Assign the value into a variable called gradebook.
scorebook = []
def scorebook_calc(subjects, grades):
    for i in range(len(subjects)):
        a = [subjects[i], grades[i]]
        scorebook.append(a)
    return scorebook



# 4. Print gradebook. 
print(scorebook_calc(subjects, grades))

# --- Add More Subjects ---

# 5. Your computer science grade is in! You got a 100.
# Add a list with the values ["computer science", 100] using a python list method.
# to our two-dimensional list gradebook.
def scorebook_append(subject, grade, scorebook):
    scorebook.append([subject, grade])
scorebook_append("computer science", 100, scorebook)
print(scorebook)


# 6. Your "visual arts" grade is in! You got a 93.
# Add ["visual arts", 93] to gradebook using a python list method.
scorebook_append("visual arts", 93, scorebook)
print(scorebook)



# --- Modify The Gradebook ---

# 7. Your instructor is rewarding an extra 5 points for the visual arts class.
# Access the index of the grade for visual arts and modify it to be 5 points greater.
def bonus_points(scorebook, subject, bonusgrade):
    for i in range(len(scorebook)):
        if scorebook[i][0] == subject:
            scorebook[i][1] += bonusgrade
    return scorebook

print(bonus_points(scorebook, 'visual arts', 5))

# 8. You decided to switch poetry to a Pass/Fail option.
# Find the grade value for poetry and use a python list method to delete it.
def switch_score_type(scorebook, subject, new_type):
    for item in scorebook:
        if item[0] == subject:
            item[1] = new_type
    return scorebook


# 9. Add a new "Pass" value to the poetry sublist using a python list method.
switch_score_type(scorebook, 'poetry', 'Pass')
print(scorebook)
# --- One Big Gradebook! ---

# Provided data for Step 10:
last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# 10. Create a new variable full_gradebook that combines last_semester_gradebook using a python
# list operator.
full_gradebook = scorebook + last_semester_gradebook


# Print full_gradebook to see the completed list.
print(full_gradebook)