#Montana
#TriviaGame
from time import sleep
#Intro
print ("Welcome to this Fun game of Trivia!")
sleep(1)
print ("You will answer 10 Question")
sleep(1)
ready = input ("Ready to play? y or n:")
if ready == "y":
    print ("Great! Let's get started.")
else:
    exit()

#Answers
q1answer = "b"
q2answer = "c"
q3answer = "d"
q4answer = "c"
q5answer = "c"
q6answer = "a"
q7answer = "c"
q8answer = "b"
q9answer = "d"
q10answer = "c"
#Question1
print ("What day is it today")
print ("a. Yesterday\nb. Today\nc. Two days ago\nd. Tommorow")
sleep(1)
answer = input ("what is you answer (a,b,c or d)")

if answer == q1answer:
    print ("Correct")
else:
    print ("Incorrect")
sleep(1)
#Question2
print ("What SuperHero group is Wolverine in?")
print ("a. the Avengers\nb. Fantastic Four\nc. the X-men\nd. the Justise League")
sleep (1)
answer = input ("what is your answer (a,b,c or d)")

if answer == q2answer:
    print ("Correct")
else:
    print ("Incorrect")
sleep(1)
#Question3
print ("What is the name of the band who wrote EnterSandman?")
print("a. Black Sabbath\nb. ACDC\nc. Guns'n'Roses\nd. Metallica")
answer = input ("what is your answer (a,b,c or d)")

if answer ==q3answer:
    print("Correct")
else:
    print ("Wrong")
sleep(1)
#Question4
print ("What is the answer to 12 multiplied by 12")
print ("a. 120\nb. 132\nc. 144\nd. 156")
answer = input ("what is your answer (a,b,c or d)")

if answer == q4answer:
    print ("You are right!")
else:
    print ("You are wrong!")
sleep(1)
#Question5
print ("Which equation does not equal 3")
print ("a. 7-4\nb. 27/9\nc. 1.67+1.42\nd. 0.47+2.53")
answer = input ("what is your answer (a,b,c or d)")

if answer == q5answer:
    print ("Correct")
else:
    print ("Incorrect")
sleep(1)
#Question6
print ("What is a box without hinges, key, or lid, yet golden treasue inside is hid.")
print ("a. An egg\nb. A tresure chest\nc. A box\nd. A container")
answer = input ("what is your answer (a,b,c or d)")

if answer == q6answer:
    print ("Correct")
else:
    print("Incorrect")
sleep(1)
#Question7
print ("This thing all things devours: Birds,beasts,trees,flowers;Gnaws iron, bites steel;\nSlays kings, ruin town, And beats high mountain down.")
print ("a. A Monster\nb. Water\nc. Time\nd. Fire")
answer = input ("what is your answer?(a,b,c or d)")

if answer == q7answer:
    print ("Correct")
else:
    print ("Incorrect")
sleep(1)
#Question8
print("Voiceless it cries, Wingless flutters, Toothless bites, Mouthless mutters. What is it?")
print("a. A bird\nb. The wind\nc. A plane\nd. The cold.")
answer = input ("what is you answer (a,b,c or d)")

if answer == q8answer:
    print ("Correct")
else:
    print("Incorrect")
sleep(1)
#Question9
print ("Thirty white horses on a red hill\nFirst they stamp then they champ, then they stand still. What are they?")
print ("a. White horses\nb. Shoes\nc. Rocks\nd. Teeth")
answer = input ("what is your answer (a,b,c or d)")

if answer == q9answer:
    print ("Correct")
else:
    print("Incorrect")
sleep(1)
#Question10
print ("What has roots as nobody sees, is taller than trees\nUp,up it goes, and yet it never grows?")
print ("a. Trees\nb. A pole\nc. A Mountain\nd. A bird")
answer = input ("what is your answer (a,b,c or d)")

if answer == q10answer:
    print ("Correct")
else:
    print("Incorrect")
sleep(3)
print("Thankyou for playing this Trivia!")