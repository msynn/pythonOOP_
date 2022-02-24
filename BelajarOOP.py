class User:
    total = 0

    def __init__(self, name, damage, role):
        self.name = name   # zilong, aurora, argus, etc.
        self.damage = damage   # 100, 200, 300, etc.
        self.role = role   # assassin, mage, warrior, etc.
        User.total += 1

    def info(self):
        return f"{self.name} - {self.role} - {self.damage}"

# instance variable VS class variable

zilong = User("zilong", 100, "assassin")
aurora = User("aurora", 200, "mage")
argus = User("argus", 300, "warrior")

print(zilong.info())