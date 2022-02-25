# Private Attribute

class User:
    total = 0

    def __init__(self, name, damage, role):
        self.name = name   # zilong, aurora, argus, etc.
        self.damage = damage   # 100, 200, 300, etc.
        self.__role = role   # assassin, mage, warrior, etc.
        User.total += 1

    def info(self):
        return f"{self.name} - {self.__role} - {self.damage}"

    def update_role(self, new_role = "fighter"):
        if self.__role == "assassin": # Jika role anda adalah assassin, maka anda bisa berubah role fighter.  
            self.__role = new_role
        else: # role selain assasin tidak bisa berubah.  
            print("Role anda tidak bisa diubah")
    
    def getRole(self):
        return self.__role

zilong = User("zilong", 100, "assassin")

# print(zilong.__dict__)
# print(zilong._User__role) cara mengakses private attribute
# print(zilong.info())
# zilong._User__role = "fighter"
print(zilong.info())
print(zilong.getRole())