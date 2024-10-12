import json
import os
from Person import Person

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