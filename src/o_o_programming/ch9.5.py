print(f"9.5. Login Attempts")
class User:
    pass

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        print(f"My name is {self.first_name}. My last name is {self.last_name}.")

    def greet_user(self):
        print(f"Hello {self.first_name}!")
        print(f"Nice to meet you!")

    def increment_login_attempts(self, login_attempts):
        self.login_attempts = login_attempts
        print(f"I tried to login {self.login_attempts} times to chrome browser, but I cannot do it.")

    def reset_login_attempts(self, login):
        self.login_attempts += login
        print(f"We reset value of login attempts to {self.login_attempts}.")

        if login >= self.login_attempts:
            print(f"It is too much.")
        else:
            print(f"You can't enter this browser.")

class User:
    name = User('Lily', 'Shodieva')
    name.describe_user()
    name.greet_user()
    name.increment_login_attempts(6)
    name.reset_login_attempts(2)
    name.reset_login_attempts(10)
    name.increment_login_attempts(0)

