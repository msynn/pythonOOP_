# Property

class User :
    total = 0
    def __init__(self, name, damage, role) :
        self.name = name  # zilong, aurora, argus, etc.
        self.damage = damage # 100, 200, 300, etc.
        self.__role = role  # assassin, mage, warrior, etc.
        User.total += 1 
    def info(self) : 
        return f"{self.name} - {self.__role} - {self.damage}"

    @property #
    def role(self) :
        return self.__role

    @role.setter
    def role(self, new_role = "fighter") :
        if self.__role == "assassin" :
            self.__role = new_role
        else :
            print("Role anda tidak bisa diubah")



zilong = User("zilong", 100, "assassin")
# print(zilong.info())
# zilong.role 
zilong.role = "mage"
print(zilong.info())
print(zilong.role)
# zilong.role = "role baru"