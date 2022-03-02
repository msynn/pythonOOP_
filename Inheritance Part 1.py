# Inheritance, extend, override, polymophism
class Employee:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def work(self):
        return f"{self.name}, is working"

class Programmer(Employee):
    def __init__(self, name, email, level):
        super().__init__(name, email)
        self.level = level

    def debug(self):
        return "debugging"

employee = Employee("Fyan", "fyanramadhan1@gmail.com")
print(employee.work())


programmer = Programmer("sakina", "nursakina@gmail.com", "Beginner")
print(programmer.work())
print(programmer.debug())