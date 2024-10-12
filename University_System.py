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
        super().__init__(name, age, contact, role)
        self.departments = self.load_departments()
        self.file_name = f"{self.name.replace(' ', '_')}_teacher.json"  # Unique filename

    def set_departments_teacher(self, department):
        self.departments.append(department)
        self.save_departments()  # Save the updated list to the file
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
                courses = department.get("courses")
                return courses if isinstance(courses, list) else [courses]
        return f"No courses found for the department '{department_name}'."

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
        """Add a course and save the updated information."""
        self.courses.append(course)
        self.save_student_info()  # Save student info

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
        if course in self.courses:
            self.courses.remove(course)
            self.save_student_info()  # Save student info
            print(f"Course '{course}' removed from the course list.")
        else:
            print(f"Course '{course}' not found in courses.")

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

