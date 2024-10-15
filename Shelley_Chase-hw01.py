# Chase Shelley
# UWYO COSC 1010
# Submission Date Oct 15, 2024
# HW 01
# Lab Section: 16
# Sources, people worked with, help given to: 
# your
# comments
# here

# Homework Question:
# 
# You are given a list of dictionaries where each dictionary represents a student and their scores 
# in different subjects.
# 
# Student Data:
students = [
     {"name": "Alice", "scores": {"Math": 85, "Science": 90, "English": 78}},
     {"name": "Bob", "scores": {"Math": 70, "Science": 88, "English": 82}},
     {"name": "Charlie", "scores": {"Math": 92, "Science": 81, "English": 89}},
     {"name": "David", "scores": {"Math": 60, "Science": 75, "English": 80}}
]

#Write a Python program that:
# 1. Calculates the average score for each student.
# 2. Stores these averages in a new dictionary where the student’s name is the key and their average score is the value.
# 3. Prints the names of students whose average score is greater than 80.

# Your task is to calculate the average scores for each student and print the names of students
# whose average score is greater than 80.

#Solution

avg_scoresa = sum(students[0]["scores"].values()) / len(students[0]["scores"].values())

avg_scoresb = sum(students[1]["scores"].values()) / len(students[1]["scores"].values())

avg_scoresc = sum(students[2]["scores"].values()) / len(students[2]["scores"].values())

avg_scoresd = sum(students[3]["scores"].values()) / len(students[3]["scores"].values())

new_dict = [
    {"Alice": avg_scoresa},
    {"Bob": avg_scoresb},
    {"Charlie": avg_scoresc},
    {"David": avg_scoresd}
]

for key, value in new_dict[0].items():
    if value > 80:
        for key in new_dict[0]:
            print(key)

for key, value in new_dict[1].items():
    if value > 80:
        for key in new_dict[1]:
            print(key)

for key, value in new_dict[2].items():
    if value > 80:
        for key in new_dict[2]:
            print(key)

for key, value in new_dict[3].items():
    if value > 80:
        for key in new_dict[3]:
            print(key)

# this was the way that it made sense to me, I couldnt figure out if there was a way to have every dict checked and printed correctly within 1 "for if for" statement. 
# So instead I wrote each of them out, which still yeilds the correct aswnser.