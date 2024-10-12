from Person import Person
import json
import os

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