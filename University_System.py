import json
import os

class University:
    def __init__(self, name):
        self.name = name
        self.departments = self.load_departments()
    def add_department(self, department):
        if department not in self.departments:
            self.departments.append(department)
            self.save_departments()
            print(f"Department '{department}' added successfully.")
        else:
            print(f"Department '{department}' already exists.")

    def load_departments(self):
        """Load departments from a JSON file."""
        if os.path.exists("Uni_Departments.json"):
            with open("Uni_Departments.json", "r") as f:
                return json.load(f)
        return []

    def save_departments(self):
        """Save the current departments to the JSON file."""
        with open("Uni_Departments.json", "w") as f:
            json.dump(self.departments, f, indent=4)

    def remove_department(self, department):
        if department in self.departments:
            self.departments.remove(department)
            self.save_departments()
            print(f"Department '{department}' removed successfully.")
        else:
            print(f"Department '{department}' not found.")

    def get_departments(self):
        return self.departments

    def search_department(self, department):
        return department in self.departments

    def clear_departments(self):
        self.departments.clear()
        self.save_departments()
        print("All departments cleared.")

    def edit_department(self, department, new_department):
        if department in self.departments:
            index = self.departments.index(department)
            self.departments[index] = new_department
            self.save_departments()
            print(f"Department '{department}' renamed to '{new_department}'.")
        else:
            print(f"Department '{department}' not found.")


class Person:
    def __init__(self, name, age, contact, role):
        self.name = name
        self.age = age
        self.contact = contact
        self.role = role


class Teacher(Person):
    def __init__(self, name, age, contact, role):
        self.departments = self.load_departments()
        super().__init__(name, age, contact, role)
        self.file_name = f"{self.name.replace(' ', '_')}_teacher.json"  # Unique filename

    def set_departments_teacher(self, department):
        """Add a department if it doesn't already exist."""
        existing_department = next(
            (d for d in self.departments if d["department"] == department["department"]),
            None,
        )

        if existing_department:
            print(f"Department '{department['department']}' already exists.")
        else:
            self.departments.append(department)
            self.save_departments()  # Save the updated list
            self.save_teacher_info()  # Save teacher info
            print(f"Department '{department['department']}' added successfully.")

    def get_departments_teacher(self):
        return self.departments

    def load_departments(self):
        """Load departments from a JSON file."""
        if os.path.exists("departments.json"):
            with open("departments.json", "r") as f:
                return json.load(f)
        return []
    

    def save_departments(self):
        """Save the current departments to the JSON file."""
        with open("departments.json", "w") as f:
            json.dump(self.departments, f, indent=4)

    def save_teacher_info(self):
        """Save the teacher's information to a JSON file."""
        teacher_info = {
            "name": self.name,
            "age": self.age,
            "contact": self.contact,
            "role": self.role,
            "departments": self.departments
        }
        with open(self.file_name, "w") as f:
            json.dump(teacher_info, f, indent=4)
            print(f"Teacher information saved to '{self.file_name}'.")

    def get_particular_departments(self, department_name):
        for department in self.departments:
            if department.get("department").lower() == department_name.lower():
                courses = department.get("courses", [])
                return courses if courses else "No courses found for this department."
        return f"Department '{department_name}' not found."               
    def update_department_courses(self, department_name, new_course):
        for department in self.departments:
            if department.get("department").lower() == department_name.lower():
                courses = department.get("courses")
                if isinstance(courses, list):
                    if new_course not in courses:
                        courses.append(new_course)
                        department["courses"] = courses
                        self.save_departments()
                        self.save_teacher_info()  # Save teacher info
                        print(f"Course '{new_course}' added to '{department_name}' department.")
                    else:
                        print(f"Course '{new_course}' already exists.")
                else:
                    department["courses"] = [courses, new_course]
                self.save_departments()
                self.save_teacher_info()  # Save teacher info
                return
        print(f"Department '{department_name}' not found.")

    def remove_department_courses(self, department_name, course_name):
        for department in self.departments:
            if department.get("department").lower() == department_name.lower():
                courses = department.get("courses")
                if isinstance(courses, list):
                    if course_name in courses:
                        courses.remove(course_name)
                        department["courses"] = courses
                        self.save_departments()
                        self.save_teacher_info()  # Save teacher info
                        print(f"Course '{course_name}' removed from '{department_name}' department.")
                    else:
                        print(f"Course '{course_name}' not found in '{department_name}' department.")
                else:
                    print(f"Department '{department_name}' does not have courses.")
                return
        print(f"Department '{department_name}' not found.")

    def clear_departments_teacher(self):
        self.departments.clear()
        self.save_departments()
        self.save_teacher_info()  # Save teacher info
        print("All teacher departments cleared.")


class Student(Person):
    def __init__(self, name, age, contact, role, department, semester, courses=None):
        super().__init__(name, age, contact, role)
        self.department = department
        self.semester = semester
        self.courses = courses if courses is not None else []
        self.file_name = f"{self.name.replace(' ', '_')}_student.json"  # Unique filename
        self.load_student_info()  # Load student info from file if it exists

    def set_courses(self, course):
        existing_course = next((c for c in self.courses if c["course"] == course["course"]), None)

        if existing_course:
            print(f"Course '{course['course']}' already exists.")
        else:
            self.courses.append(course)
            self.save_student_info()  # Save student info after adding the course
            print(f"Course '{course['course']}' added successfully.")

    def update_course(self, old_course, new_course):
        """Update a course name and save the updated information."""
        for course in self.courses:
            if course.get("course") == old_course:
                course["course"] = new_course
                self.save_student_info()  # Save student info
                print(f"Course '{old_course}' updated to '{new_course}'.")
                return
        print(f"Course '{old_course}' not found in courses.")

    def update_instructor(self, course_name, new_instructor):
        """Update the instructor of a course and save the updated information."""
        for course in self.courses:
            if course.get("course") == course_name:
                course["Instructor"] = new_instructor
                self.save_student_info()  # Save student info
                print(f"Instructor of course '{course_name}' updated to '{new_instructor}'.")
                return
        print(f"Course '{course_name}' not found in courses.")

    def remove_course(self, course):
        """Remove a course and save the updated information."""
        for cour in self.courses:
            if cour.get("course") == course:
                self.courses.remove(cour)
                self.save_student_info()  # Save student info
                print(f"Course '{course}' removed from the course list.")
                return
        print(f"Department '{course}' not found.")

    def clear_courses(self):
        """Clear all courses and save the updated information."""
        self.courses.clear()
        self.save_student_info()  # Save student info
        print("All courses cleared.")

    def get_courses(self):
        return self.courses

    def save_student_info(self):
        """Save the student's information to a JSON file."""
        student_info = {
            "name": self.name,
            "age": self.age,
            "contact": self.contact,
            "role": self.role,
            "department": self.department,
            "semester": self.semester,
            "courses": self.courses,
        }
        with open(self.file_name, "w") as f:
            json.dump(student_info, f, indent=4)
        print(f"Student information saved to '{self.file_name}'.")

    def load_student_info(self):
        """Load the student's information from a JSON file."""
        try:
            with open(self.file_name, "r") as f:
                student_info = json.load(f)
                self.name = student_info["name"]
                self.age = student_info["age"]
                self.contact = student_info["contact"]
                self.role = student_info["role"]
                self.department = student_info["department"]
                self.semester = student_info["semester"]
                self.courses = student_info["courses"]
                print(f"Student information loaded from '{self.file_name}'.")
        except FileNotFoundError:
            print(f"No existing student data found for '{self.file_name}'. Starting fresh.")
        except json.JSONDecodeError:
            print(f"Error decoding JSON from '{self.file_name}'. Starting fresh.")

if __name__ == "__main__":
    # Uni = University("University of Sahiwal")
    # uni_departments = ["Psychology", "English", "Mathematics", "Chemistry", "Physics", "Computer Science", "Software Engineering", "Urdu", "BBA"]
    # for dprt in uni_departments:
    #     Uni.add_department(dprt)

    # print(Uni.get_departments())

    # teacher = Teacher("Dr. Shafiq Hussain", 40, 673287239832, "HOD of CS Department")
    # teacher_departments = [{"department": "Computer Science", "courses": ["Programming Fundamentals"], "credit_hours": 4},
    #                        {"department": "Software Engineering", "courses": ["Programming Fundamentals"], "credit_hours": 4}]
    # for department in teacher_departments:
    #     teacher.set_departments_teacher(department)

    # print(teacher.get_departments_teacher())
    # teacher.update_department_courses("Software Engineering", "OOP")
    # print(teacher.get_particular_departments("Software Engineering"))

    # student1 = Student("Abdul Rehman", 20, 69242983, "Student", "Psychology", "3rd")
    # st1_courses = [
    #     {"course": "Psychology 101", "Instructor": "Dr. Rehman", "credit_hours": 3},
    #     {"course": "Psychology 201", "Instructor": "Dr. Hussain", "credit_hours": 3},
    #     {"course": "Psychology 301", "Instructor": "Dr. Qadir", "credit_hours": 3},
    # ]
    # for course in st1_courses:
    #     student1.set_courses(course)

    # print(student1.get_courses())
    # student1.update_course("Psychology 101", "Psychology 101: Introduction to Psychology")
    # student1.update_instructor(" Psychology 101: Introduction to Psychology", "Dr. Shafiq Hussain")
    # student1.remove_course("Psychology 201")
    # print(student1.get_courses())
    # student1.clear_courses()
