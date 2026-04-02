# Parent class
class User:
    def __init__(self, name, id):
        self.name = name
        self.id = id

# Child class: Student
class Student(User):
    def __init__(self, name, id, dept, fees):
        super().__init__(name, id)
        self.dept = dept
        self.fees = fees

# Child class: Faculty
class Faculty(User):
    def __init__(self, name, id, salary):
        super().__init__(name, id)
        self.salary = salary

# Child class: TempFaculty (inherits from Faculty)
class TempFaculty(Faculty):
    def __init__(self, name, id, salary, duration):
        super().__init__(name, id, salary)
        self.duration = duration

# Example usage
s = Student("Alice", 101, "Physics", 5000)
f = Faculty("Dr. Bob", 201, 80000)
t = TempFaculty("Dr. Carol", 301, 50000, "6 months")

print(s.__dict__)
print(f.__dict__)
print(t.__dict__)