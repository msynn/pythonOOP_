# Polymorphism

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

    def work(self): # override = menimpa method yang ada di class parent
        return f"{self.name}, is writing code"

class UiDesigner(Employee):
    def __init__(self, name, email, level, tools):
        super().__init__(name, email)
        self.level = level
        self.tools = tools

    def work(self):
        return f"{self.name}, is designing some new cool products"


employee = Employee("Fyan", "fyanramadhan1@gmail.com")
programmer = Programmer("sakina", "nursakina@gmail.com", "Beginner")
ui_designer = UiDesigner("Ikhsan", "ikhsan@gmail.com", "Senior", "Photoshop")

def working(system):
    print(system.work())

class Manager:
    def __init__(self, name):
        self.name = name

    def work (self):
        return f"{self.name}, is Tiduran"

manager = Manager("Hendra")
working(manager)