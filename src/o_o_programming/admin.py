

from src.o_o_programming.class_user import User
from src.o_o_programming.privileges import Privileges


class Admin(User):
    def __init__(self, first_name, last_name, privileges):
        super().__init__(first_name, last_name)
        self.privileges = privileges

    def show_privileges(self):
        print(f"I am your Admin. You {self.privileges}.")
print(f"\n9.7")
person1 = Admin('Nazi', 'Omonova', 'can add post')
person2 = Admin('Shahri', 'Omonova', 'can delete post')
person3 = Admin('Zizi', 'Omonova', 'can ban user')
person1.describe_user()
person1.greet_user()
person1.show_privileges()
person2.describe_user()
person2.greet_user()
person2.show_privileges()
person3.describe_user()
person3.greet_user()
person3.show_privileges()
example1 = Privileges('can use my name')
example2 = Privileges('can add my name')
example1.show_privileges()
example2.show_privileges()
example3 = Admin('Azimjon', 'Omonov','can post your name on the chat')
example3.describe_user()
example3.greet_user()
example3.show_privileges()