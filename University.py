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