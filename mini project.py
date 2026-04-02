from abc import ABC, abstractmethod
from functools import reduce

# ===== Abstract Base Class =====
class AbstractUser(ABC):
    @abstractmethod
    def get_details(self):
        pass

# ===== Base User Class =====
class User(AbstractUser):
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def get_details(self):
        return f"User Name: {self.name}, ID: {self.id}"

# ===== Student Class =====
class Student(User):
    def __init__(self, name, id, dept, fees):
        super().__init__(name, id)
        self.dept = dept
        self.fees = fees

    def get_details(self):
        return f"Student Name: {self.name}, ID: {self.id}, Dept: {self.dept}, Fees: {self.fees}"

# ===== Faculty Class =====
class Faculty(User):
    def __init__(self, name, id, salary):
        super().__init__(name, id)
        self.salary = salary

    def get_details(self):
        return f"Faculty Name: {self.name}, ID: {self.id}, Salary: {self.salary}"

# ===== TempFaculty Class =====
class TempFaculty(Faculty):
    def __init__(self, name, id, salary, duration):
        super().__init__(name, id, salary)
        self.duration = duration

    def get_details(self):
        return f"TempFaculty Name: {self.name}, ID: {self.id}, Salary: {self.salary}, Duration: {self.duration}"

# ===== Higher-Order Function =====
def process_users(users, func):
    return list(map(func, users))

# ===== Data =====
students = [
    Student("Alice", 101, "Physics", 5000),
    Student("Bob", 102, "Chemistry", 4500),
    Student("Charlie", 103, "Math", 5500)
]

faculty = [
    Faculty("Dr. Smith", 201, 75000),
    Faculty("Dr. Jones", 202, 80000),
    TempFaculty("Dr. Carol", 203, 50000, "6 months")
]

# ===== 1. Print All Details =====
print("=== All Students ===")
for s in students:
    print(s.get_details())

print("\n=== All Faculty ===")
for f in faculty:
    print(f.get_details())

# ===== 2. Sorted Data =====
students_sorted = sorted(students, key=lambda x: x.fees)
faculty_sorted = sorted(faculty, key=lambda x: x.salary)

print("\n=== Students Sorted by Fees ===")
for s in students_sorted:
    print(s.get_details())

print("\n=== Faculty Sorted by Salary ===")
for f in faculty_sorted:
    print(f.get_details())

# ===== 3. Filtered Data =====
high_fee_students = list(filter(lambda x: x.fees > 4800, students))
high_salary_faculty = list(filter(lambda x: x.salary >= 75000, faculty))

print("\n=== Students with Fees > 4800 ===")
for s in high_fee_students:
    print(s.get_details())

print("\n=== Faculty with Salary >= 75000 ===")
for f in high_salary_faculty:
    print(f.get_details())

# ===== 4. Total Fees & Salary using reduce =====
total_fees = reduce(lambda acc, s: acc + s.fees, students, 0)
total_salary = reduce(lambda acc, f: acc + f.salary, faculty, 0)

print(f"\nTotal Fees Collected from Students: {total_fees}")
print(f"Total Salary of Faculty: {total_salary}")

# ===== 5. Functional Programming Example =====
# Map: get student names
student_names = process_users(students, lambda x: x.name)
# Filter: students with fees > 4800
students_over_4800 = list(filter(lambda x: x.fees > 4800, students))
# Reduce: sum of fees
sum_fees = reduce(lambda acc, s: acc + s.fees, students, 0)

print("\n=== Functional Programming Concepts Used ===")
print("Student Names (map):", student_names)
print("Students with Fees > 4800 (filter):", [s.name for s in students_over_4800])
print("Total Fees (reduce):", sum_fees)