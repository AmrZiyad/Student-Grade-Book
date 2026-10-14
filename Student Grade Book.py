grades = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "Diana": 95,
    "Ethan": 88,
}

total_score = 0
for student, score in grades.items():
    total_score += score

class_average = total_score / len(grades)  
print(f"Class Average: {class_average:.2f}")

topstudent = max(grades, key=grades.get)
bottomstudent = min(grades, key=grades.get)

print(f"Top Scorer: {topstudent} with a score of {grades[topstudent]}")
print(f"Bottom Scorer: {bottomstudent} with a score of {grades[bottomstudent]}")

search_name = input("\nEnter a student's name to search for their grade: ")

score = grades.get(search_name, "Not found")
if score != "Not found":
    print(f"{search_name}'s grade: {score}")
else:
    print(f"{search_name} is not in the grade book.")