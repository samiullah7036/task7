from abc import ABC, abstractmethod

# Abstract Base Class
class AbstractUser(ABC):
    @abstractmethod
    def get_details(self):
        pass

# Concrete User class
class User(AbstractUser):
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def get_details(self):
        return f"User Name: {self.name}, ID: {self.id}"

# Student class
class Student(User):
    def __init__(self, name, id, dept, fees):
        super().__init__(name, id)
        self.dept = dept
        self.fees = fees

    def get_details(self):
        return f"Student Name: {self.name}, ID: {self.id}, Dept: {self.dept}, Fees: {self.fees}"

# Faculty class
class Faculty(User):
    def __init__(self, name, id, salary):
        super().__init__(name, id)
        self.salary = salary

    def get_details(self):
        return f"Faculty Name: {self.name}, ID: {self.id}, Salary: {self.salary}"

# TempFaculty class
class TempFaculty(Faculty):
    def __init__(self, name, id, salary, duration):
        super().__init__(name, id, salary)
        self.duration = duration

    def get_details(self):
        return f"TempFaculty Name: {self.name}, ID: {self.id}, Salary: {self.salary}, Duration: {self.duration}"

# Example usage
s = Student("Alice", 101, "Physics", 5000)
f = Faculty("Dr. Bob", 201, 80000)
t = TempFaculty("Dr. Carol", 301, 50000, "6 months")

print(s.get_details())
print(f.get_details())
print(t.get_details())

#Task 3: Sorting example
students = [
    Student("Alice", 101, "CS", 5000),
    Student("Bob", 102, "EE", 4500),
    Student("Charlie", 103, "ME", 6000)
]

faculty = [
    Faculty("Dr. Smith", 201, 70000),
    TempFaculty("Dr. John", 202, 50000, "6 months"),
    Faculty("Dr. Jane", 203, 80000)
]

# Sort students by fees
students.sort(key=lambda x: x.fees)
# Sort faculty by salary
faculty.sort(key=lambda x: x.salary)

# Display sorted details
print("Sorted Students:")
for s in students:
    print(s.get_details())

print("\nSorted Faculty:")
for f in faculty:
    print(f.get_details())
    # Assuming 'students' list already exists
student_names = list(map(lambda s: s.name, students))
print("Student Names:", student_names)
# Filter students with fees > 50000
high_fee_students = list(filter(lambda s: s.fees > 50000, students))

# Filter faculty with salary > 30000
high_salary_faculty = list(filter(lambda f: f.salary > 30000, faculty))

# Display results
print("Students with Fees > 50000:")
for s in high_fee_students:
    print(s.get_details())

print("\nFaculty with Salary > 30000:")
for f in high_salary_faculty:
    print(f.get_details())
    from functools import reduce

# Total fees collected from students
total_fees = reduce(lambda acc, s: acc + s.fees, students, 0)

# Total salary of all faculty
total_salary = reduce(lambda acc, f: acc + f.salary, faculty, 0)

# Display results
print("Total Fees Collected:", total_fees)
print("Total Faculty Salary:", total_salary)
# Higher-order function
def process_users(users, func):
    """
    users: list of User/Student/Faculty objects
    func: function to apply to each user
    Returns a list of results after applying func
    """
    return list(map(func, users))

# Example usage with students
students = [
    Student("Alice", 101, "Physics", 5000),
    Student("Bob", 102, "Chemistry", 4500),
    Student("Charlie", 103, "Math", 5500)
]

# Example: get names of all students using process_users
student_names = process_users(students, lambda x: x.name)
print("Student Names:", student_names)

# Example: filter students with fees > 4800
high_fee_students = list(filter(lambda x: x.fees > 4800, students))
print("High Fee Students:", [s.get_details() for s in high_fee_students])

# Example usage with faculty
faculty = [
    Faculty("Dr. Smith", 201, 75000),
    Faculty("Dr. Jones", 202, 80000),
    TempFaculty("Dr. Carol", 203, 50000, "6 months")
]

# Get salaries using process_users
faculty_salaries = process_users(faculty, lambda x: x.salary)
print("Faculty Salaries:", faculty_salaries)