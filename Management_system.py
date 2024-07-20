import random

class Student:
    def __init__(self, student_id, name, semester, gpa, courses, degree):
        self.student_id = student_id
        self.name = name
        self.semester = semester
        self.gpa = gpa
        self.courses = courses
        self.degree = degree

    def register_course(self, course):
        if course in self.courses:
            print("You are already registered in this course.")
        else:
            self.courses.append(course)
            print(f"Course {course} successfully registered.")

    def withdraw_course(self, course):
        if course in self.courses:
            self.courses.remove(course)
            print(f"Course {course} successfully withdrawn.")
        else:
            print("You are not registered in this course.")

    def detailed_info(self):
        print("Detailed Result:")
        print(f"Name: {self.name}")
        print(f"Semester: {self.semester}")
        print(f"GPA: {self.gpa}")
        print(f"Courses Registered: {', '.join(self.courses)}")
        print(f"Degree: {self.degree}")

    def fee_challan(self):
        print("Fee Challan:")
        print(f"Name: {self.name}")
        print(f"Courses Registered: {', '.join(self.courses)}")
        fee = len(self.courses) * 500  # Assuming each course costs 500
        print(f"Total Fee: Rs{fee}")

    def calculate_gpa(self):
        print("Enter Grades for Courses:")
        total_points = 0
        for course in self.courses:
            grade = int(input(f"Enter marks for {course}: "))
            if grade < 50:
                points = 0
            elif grade < 54:
                points = 1
            elif grade < 58:
                points = 1.33
            elif grade < 62:
                points = 1.66
            elif grade < 66:
                points = 2
            elif grade < 70:
                points = 2.33
            elif grade < 74:
                points = 2.66
            elif grade < 78:
                points = 3
            elif grade < 82:
                points = 3.33
            elif grade < 86:
                points = 3.66
            elif grade < 90:
                points = 4
            else:
                points = 4
            total_points += points
        new_gpa = total_points / len(self.courses)
        self.gpa = round(new_gpa, 2)
        print(f"New GPA calculated: {self.gpa}")

class StudentManagementSystem:
    def __init__(self):
      #dict
        self.students = {}

    def load_initial_data(self):
        initial_data = {
            "101": {"name": "Rida Zubair", "semester": 1, "gpa": 3.5, "courses": ["Math", "Physics"], "degree": "B.S Data Science"},
            "102": {"name": "Rameen Zubair", "semester": 2, "gpa": 3.7, "courses": ["COAL", "DSA"], "degree": "B.S Computer Science"},
            "103": {"name": "Mahnoor Zubair", "semester": 3, "gpa": 3.8, "courses": ["Computer Science", "PF"], "degree": "B.S Data Science"},
            "104": {"name": "Ali Haider", "semester": 4, "gpa": 3.6, "courses": ["English", "History"], "degree": "BBA"},
            "105": {"name": "Zain ul Abideen", "semester": 7, "gpa": 2.9, "courses": ["Discrete Structures", "COAL"], "degree": "BSCS"}
        }
        for student_id, info in initial_data.items():
            self.students[student_id] = Student(student_id, info["name"], info["semester"], info["gpa"], info["courses"], info["degree"])

    def list_students(self):
        print("List Students\n")
        for student in self.students.values():
            print(f"=> {student.name} (ID: {student.student_id})")

    def add_student(self):
        new_name = input("Enter New Student Name: ")
        for student in self.students.values():
            if new_name == student.name:
                print(f"\nThis Student {new_name} Already In The Database")
                return
        new_id = str(random.randint(106, 999))
        new_semester = int(input("Enter Semester: "))
        new_gpa = float(input("Enter GPA: "))
        new_courses = input("Enter Courses (comma separated): ").split(", ")
        new_degree = input("Enter Degree: ")
        self.students[new_id] = Student(new_id, new_name, new_semester, new_gpa, new_courses, new_degree)
        print(f"\n=> New Student {new_name} Successfully Added with ID {new_id}\n")
        self.list_students()

    def search_student(self):
        search_name = input("Enter Student Name To Search: ")
        for student in self.students.values():
            if search_name == student.name:
                print(f"\n=> Record Found Of Student {search_name} (ID: {student.student_id})")
                return
        print(f"\n=> No Record Found Of Student {search_name}")

    def remove_student(self):
        remove_name = input("Enter Student Name To Remove: ")
        for student_id, student in self.students.items():
            if remove_name == student.name:
                del self.students[student_id]
                print(f"\n=> Student {remove_name} Successfully Deleted\n")
                return
        print(f"\n=> No Record Found of This Student {remove_name}")

    def student_details(self):
        student_id = input("Enter Your Student ID: ")
        if student_id in self.students:
            student = self.students[student_id]
            student.detailed_info()

            while True:
                print("""
Enter 1 : Register Courses
Enter 2 : Withdraw Courses
Enter 3 : Detailed Information
Enter 4 : Fee Challan
Enter 5 : GPA Calculation
Enter 6 : Logout
                """)
                try:
                    sub_option = int(input("Please Select An Above Option: "))
                except ValueError:
                    print("\nHy! That's Not A Number")
                    continue
                else:
                    print("\n")

                if sub_option == 1:
                    new_course = input("Enter Course To Register: ")
                    student.register_course(new_course)
                elif sub_option == 2:
                    withdraw_course = input("Enter Course To Withdraw: ")
                    student.withdraw_course(withdraw_course)
                elif sub_option == 3:
                    student.detailed_info()
                elif sub_option == 4:
                    student.fee_challan()
                elif sub_option == 5:
                    student.calculate_gpa()
                elif sub_option == 6:
                    print("Logging out...")
                    break
                else:
                    print("Invalid Option Selected.")
        else:
            print("Student ID not found. Please register as a new student.")

    def manage_student(self):
        print("""
  ------------------------------------------------------
 |======================================================|
 |======== Welcome To Student Management System ========|
 |======================================================|
  ------------------------------------------------------

Enter 1 : Student's List
Enter 2 : New Student
Enter 3 : Search Student
Enter 4 : Remove Student
Enter 5 : Registered Student
        """)

        try:
            user_input = int(input("Please Select An Above Option: "))
        except ValueError:
            print("\nHy! That's Not A Number")
            return
        else:
            print("\n")

        if user_input == 1:
            self.list_students()
        elif user_input == 2:
            self.add_student()
        elif user_input == 3:
            self.search_student()
        elif user_input == 4:
            self.remove_student()
        elif user_input == 5:
            self.student_details()
        else:
            print("Please Enter Valid Option")

    def run(self):
        self.load_initial_data()
        while True:
            self.manage_student()
            run_again = input("\nWant To Run Again Y/n: ")
            if run_again.lower() != 'y':
                break


sms = StudentManagementSystem()
sms.run()
