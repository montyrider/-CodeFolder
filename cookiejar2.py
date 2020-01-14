#Montana
#Cookie Jar
import random

random.seed()

def StartText ():
    print (" Welcome to the Game The Cookie Jar!")
    print (" you will have to guess the number of Cookies in the Jar.")
    print (" The Cookie Jar can hold up to 100 Cookies!")

cookies = random.randint(1,100)

guesses = 6

while guesses > 0:
    print ("How many Cookies do you think there are?")
    guess = int(input())

    if guess == cookies:
        print ("Congratulations! You guessed the exact number of Cookies!")
        exit()

    elif guess > cookies:
        print (" Too High.")
        guesses = guesses-1

    elif guess < cookies:
        print ("Too Low.")
        guesses = guesses-1
    else:
        print ("Sorry, I don't undersand.")

StartText()