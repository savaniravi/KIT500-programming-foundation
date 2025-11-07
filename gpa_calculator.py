"""
    6.2CR Dictionaries (Student GPA Calculator)
"""

__author__ = "Ravikumar Savani"

def add_student(stud_results, sid):
    """
    Adds a new student ID.
    """
    if sid in stud_results:
        print("A record for the student already exists.")
    else:
        stud_results[sid] = []
        print(f"Student with ID {sid} added successfully.")

def add_result_for_student(stud_results, sid, result):
    """
    Adds a result to the results on record for an existing student.
    """
    if sid not in stud_results:
        print("No student with id", sid, "exists.")
    elif not 0 <= result <= 100:
        print("Invalid result! Result must be between 0 and 100.")
    else:
        stud_results[sid].append(result)
        print("Result", result, "added for student with ID", sid)

def calculate_average(stud_results, sid):
    """
    Calculates the average of all results on record for a given student.
    """
    if sid not in stud_results:
        print("No student with id", sid, "exists.")
        return 0.0
    results = stud_results[sid]
    if not results:
        print("No results for student with id", sid)
        return 0.0
    total = sum(results)
    count = len(results)
    average = total / count
    return average

def calculate_gpa(stud_results, sid):
    """
    Calculates the GPA for the given student's results.
    """
    if sid not in stud_results:
        print("No student with id", sid, "exists.")
        return 0.0

    results = stud_results[sid]
    if not results:
        print("No results for student with id", sid)
        return 0.0

    total_grade_points = 0
    total_units = 0

    for result in results:
        total_units += 1
        if result >= 80:
            total_grade_points += 7
        elif 70 <= result < 80:
            total_grade_points += 6
        elif 60 <= result < 70:
            total_grade_points += 5
        elif 50 <= result < 60:
            total_grade_points += 4
        else:
            total_grade_points += 0

    gpa = total_grade_points / total_units
    return gpa

def main():
    """
    Main function to manage unit results for a collection of students.
    """
    student_results = {}

    while True:
        print("\nMenu:")
        print("1. Add a student")
        print("2. Add a result for an existing student")
        print("3. Calculate the average of a student's results")
        print("4. Calculate a student's cumulative GPA")
        print("5. Display all students and their results")
        print("6. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            sid = input("Enter student ID: ")
            add_student(student_results, sid)
        elif choice == "2":
            sid = input("Enter student ID: ")
            result = int(input("Enter result: "))
            add_result_for_student(student_results, sid, result)
        elif choice == "3":
            sid = input("Enter student ID: ")
            average = calculate_average(student_results, sid)
            print(f"Average for student {sid} is {average:.2f}")
        elif choice == "4":
            sid = input("Enter student ID: ")
            gpa = calculate_gpa(student_results, sid)
            print(f"Cumulative GPA for student {sid} is {gpa:.1f}")
        elif choice == "5":
            print("Student Results:")
            for sid, results in student_results.items():
                print(f"Student ID: {sid}, Results: {results}")
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()