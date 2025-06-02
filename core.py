import random
from config import *
def game():
        number = random.randint(NUM1,NUM2)
        user_input = int(input("ENTER -> "))
        while( number != user_input ):
                print("Неверно!")
                user_input = int(input("ENTER ->"))

        return True
