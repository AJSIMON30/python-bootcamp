student_names = ("Juan", "Maria", "Joseph")
student_scores = (70, 90, 81)

# TODO: Print the student scores and names in the following format
""" 
    Student Records:
    Student: Juan scored 70 in the exam.
    Student: Maria scored 90 in the exam.
    Student: Joseph scored 81 in the exam.
"""
highest_score = None
highest_scorer = None

for name, score in zip(student_names, student_scores):
    if highest_score is None or score > highest_score:
        highest_score = score
        highest_scorer = name
    print(f"Student:, {highest_scorer} ,scored,{highest_score},in the exam")

