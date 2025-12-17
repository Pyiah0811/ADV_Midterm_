print("Pyiah Dyonne Cruz_ADT_Final_Exam")
name = input("Full Name: ")
address = input("Address: ")
age = input("Age: ")

courses = ["1 BSCS", "2 BSIT", "3 BSCPE"]
subjects = ["ADT", "FRE", "AFL", "FOS"]

print("\nAvailable Courses: ")
for i, course in enumerate(courses, 1):
	print(f"{i}. {course}")

course_choice = int(input("Select a course (1-3):"))
selected_course = courses[course_choice - 1]

print("\nSubjects: ")
for i, subject in enumerate(subjects, 1):
        print(f"{i}. {subject}")

num_subjects = int(input("How many subjects will you enroll?"))
rate_per_subject = 1000
total_payment = num_subjects * rate_per_subject

print("\n Formatted Enrollment Summary")
print("Name:",  name)
print("Address:",  address)
print("Age:",  age)
print("Name:",  name)
print("Course:",  selected_course)
print("Number of Subjects:",  num_subjects)
print("Total Payment", total_payment)
