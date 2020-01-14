#Montana
#HangManGame
from time import sleep
import random
random.seed()

someWords = ["monkey","wonderful","captain","oceanic","personal","magnificent","intruder"
             ,"pacific","presidential","diverse","compact","mystery","nuclear","measure","dictionary"
             ,"complete","carbine","acknowledge","knowledge","challenge","finance","terabyte","processing"
             ,"graphic","hippopotamus","rhinoceros","foundation","volcanic","zestly","pharaoh","volkswagen"
             ,"oddish","oculus","odyessey","colonel","federal","czechoslovakia","condescendant","unorthodox","puzzled","seismophobia","bibliophobia"
             ,"bufonophobia","dutchphobia","necrophobia","phobophobia","russophobia","russia","asia","lollipop","america"]
gameDisplay = []

theWord = random.choice(someWords)

answer = list(theWord)

gameDisplay.extend(answer)

#print (" ".join(gameDisplay))

for n in range(len(answer)):
    gameDisplay[n] = "_"

print (" ".join(gameDisplay))

rightGuesses = 0
wrongGuesses = 0



def drawHangmanPic (wrongGuesses):
    if wrongGuesses == 0:
        print("   +----+")
        print("        |")
        print("        |")
        print("        |")
        print("       ||")
        print("       ||")
        print("=========")
    elif wrongGuesses == 1:
        print("   +----+")
        print("   |    |")
        print("        |")
        print("        |")
        print("       ||")
        print("       ||")
        print("=========")
    elif wrongGuesses == 2:
        print("   +----+")
        print("   |    |")
        print(" (o-o)  |")
        print("        |")
        print("       ||")
        print("       ||")
        print("=========")
    elif wrongGuesses == 3:
        print("   +----+")
        print("   |    |")
        print(" (o-o)  |")
        print("   |    |")
        print("       ||")
        print("       ||")
        print("=========")
    elif wrongGuesses == 4:
        print("   +----+")
        print("   |    |")
        print(" (o-o)  |")
        print("  /|    |")
        print("       ||")
        print("       ||")
        print("=========")
    elif wrongGuesses == 5:
        print("   +----+")
        print("   |    |")
        print(" (o-o)  |")
        print("  /|\   |")
        print("       ||")
        print("       ||")
        print("=========")
    elif wrongGuesses == 6:
        print("   +----+")
        print("   |    |")
        print(" (o-o)  |")
        print("  /|\   |")
        print("  /    ||")
        print("       ||")
        print("=========")
    elif wrongGuesses == 7:
        print("   +----+")
        print("   |    |")
        print(" (o-o)  |")
        print("  /|\   |")
        print("  / \  ||")
        print("       ||")
        print("=========")
    elif wrongGuesses == 8:
        print("   +----+")
        print("   |    |")
        print(" (x-x)  |")
        print("  /|\   |")
        print("  / \  ||")
        print("       ||")
        print("=========")


while rightGuesses < len(answer):
    guess = input ("Please guess a letter: ")
    
    if guess in gameDisplay:
        print ("You already guessed that letter.")
        sleep(1)
        drawHangmanPic (wrongGuesses)
        print (" ".join(gameDisplay))
        
    elif guess not in answer:
        print ("You come a inch closer to Death.")
        sleep(1)
        wrongGuesses = wrongGuesses + 1
        drawHangmanPic(wrongGuesses)
        if wrongGuesses == 8:
            print ("R.I.P")
            print ("GAME OVER")
            print ("This was the word =>  " + theWord)
            exit()
            print (" ".join(gameDisplay))
    else:
        for n in range(len(answer)):
             if answer[n] == guess:
                 gameDisplay[n] = guess
                 rightGuesses = rightGuesses + 1
        print ("You guessed right!")
        sleep(1)
        drawHangmanPic(wrongGuesses)
        print (" ".join(gameDisplay))
        
print ("Congratulations! Your life was spared!")