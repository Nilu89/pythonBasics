
class User:
    pass

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print(f"My name is {self.first_name}. My last name is {self.last_name}.")

    def greet_user(self):
        print(f"Hello {self.first_name}!")
        print(f"Nice to meet you!")

name = User('Lily', 'Shodieva')
name.describe_user()
name.greet_user()

class Admin(User):

    def __init__(self, first_name, last_name, privileges):
        super.__init__(first_name, last_name)

    def show_priviliges(self):
        print()
