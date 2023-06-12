print(f"\n9.8")
class Privileges:
    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        print(f"I am your Admin. You {self.privileges}.")

example1 = Privileges('can use my name')
example2 = Privileges('can add my name')
example1.show_privileges()
example2.show_privileges()

