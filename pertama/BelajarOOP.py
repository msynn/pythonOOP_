class User:
    total = 0

    def __init__(self, name, damage, role):
        self.name = name   # zilong, aurora, argus, etc.
        self.damage = damage   # 100, 200, 300, etc.
        self.role = role   # assassin, mage, warrior, etc.
        User.total += 1

    def info(self):
        return f"{self.name} - {self.role} - {self.damage}"

    def update_role(self, new_role = "fighter"):
        if self.role == "assassin": # Jika role anda adalah assassin, maka anda bisa berubah role fighter.  
            self.role = new_role
        else: # role selain assasin tidak bisa berubah.  
            print("Role anda tidak bisa diubah")
        

zilong = User("zilong", 100, "assassin")
aurora = User("aurora", 200, "mage")
argus = User("argus", 300, "warrior")


print(zilong.info())     
zilong.update_role()
print(zilong.info())

print(aurora.info())
aurora.update_role("assassin")
print(aurora.info())