from University import University
from Teacher import Teacher
from Student import Student


if __name__ == "__main__":
    Uni = University("University of Sahiwal")
    uni_departments = ["Psychology", "English", "Mathematics", "Chemistry", "Physics", "Computer Science", "Software Engineering", "Urdu", "BBA"]
    for dprt in uni_departments:
        Uni.add_department(dprt)

    print(Uni.get_departments())

    teacher = Teacher("Dr. Shafiq Hussain", 40, 673287239832, "HOD of CS Department")
    teacher_departments = [{"department": "Computer Science", "courses": ["Programming Fundamentals"], "credit_hours": 4},
                           {"department": "Software Engineering", "courses": ["Programming Fundamentals"], "credit_hours": 4}]
    for department in teacher_departments:
        teacher.set_departments_teacher(department)

    print(teacher.get_departments_teacher())
    teacher.update_department_courses("Software Engineering", "OOP")
    print(teacher.get_particular_departments("Software Engineering"))

    student1 = Student("Abdul Rehman", 20, 69242983, "Student", "Psychology", "3rd")
    st1_courses = [
        {"course": "Psychology 101", "Instructor": "Dr. Rehman", "credit_hours": 3},
        {"course": "Psychology 201", "Instructor": "Dr. Hussain", "credit_hours": 3},
        {"course": "Psychology 301", "Instructor": "Dr. Qadir", "credit_hours": 3},
    ]
    for course in st1_courses:
        student1.set_courses(course)

    print(student1.get_courses())
    student1.update_course("Psychology 101", "Psychology 101: Introduction to Psychology")
    student1.update_instructor(" Psychology 101: Introduction to Psychology", "Dr. Shafiq Hussain")
    student1.remove_course("Psychology 201")
    print(student1.get_courses())
    student1.clear_courses()
    