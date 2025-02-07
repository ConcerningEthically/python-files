from random import randint

number = "cat"

def greeting():
    name = input("what is your name? : ")
    print("Greetings, ", name)

def numberinput():
    number = int("Please type an integer from 1-10 : ")

def numbervalidation(number):
    if number >= 1 and number <= 10:
        return number
    else:
        number = input("You did not type an integer from 1-10, please type a number from 1-10 : ")
        numbervalidation(number)

def guessinggame(number):
    
    chances = input("How many chances would you like? : ")
    random_number = randint(1, 10)
    while chances >= 0:
        numberinput()
        numbervalidation()
        
        if number == random_number:
            print("Congrats, You win ")
            break

        else:
            print("Nice try, you guessed incorrectly")
            chances -= 1

greeting()
game()