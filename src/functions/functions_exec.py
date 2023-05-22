# Functions execution file
# Module, package, import
# ./src/functions/functions1.py -> greet_user_by_name()


# from src.functions.function1 import greet_user_by_name, greet_user, thank_you_by_name
from src.functions.function1 import *


# EXECUTION:
greet_user_by_name('john')
greet_user()
greet_user_by_name('jane')
greet_user()
greet_user_by_name('britney')
thank_you_by_name('john', 10)
thank_you_by_name('jane', 5)
thank_you_by_name('britney', 20)
thank_you_by_name('mark', 1)

from src.exercises.fuzz_buzz import *

