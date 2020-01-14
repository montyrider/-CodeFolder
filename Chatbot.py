#ChatBot
#Montana
#coding101

print("Hello my name is Montana")
print ("I am a simple question and answer chatbot")


name = input ("what is you name?")
print ("Hello %s!" %name)


animal = input("what is your favorite animal?")
print("%ss are my favortite animal too!" %animal)


print("I am 12 years old.")
age = int(input ("how old are you?"))

if age == 12:
    print("Cool we're the same age!")

elif age > 12:
    print(" You're older than me.")
    
elif age < 12:
    print("You're younger than me.")


number = input("what is the biggest number you can think of? ")
print ("%s is a big number." %number)

instrament = input("Do you play a instrament? ")
if instrament == "yes" or instrament == "Yes":
    print ("Cool I play electric guitar!")
else:
    print ("its fun to play instrament you should try to learn one.")

color = input ("what is you favorite color? ")
print ("%s is my favorite color too!" %color)

superhero = input("who's your favorite SuperHero?")
if superhero == "wolverine" or superhero == "Wolverine":
    print("Wolverine is my favorite SuperHero too!")
else:
    print ("%s is a cool Superhero." %superhero)

villan = input ("Speaking of Heros who's your favorite Villan?")
if villan == "joker" or villan == "Joker" or villan == "the joker" or villan == "The joker" or villan == "The Joker" or villan == "the Joker":
    print ("The Joker is my favorite Villan too!")
else:
    print ("%s is a great Villan." %villan)
    

music = input ("what kind off music do you like?")
if music == "rock" or music == "Rock" or music == "rock music" or music == "Rock music" or music == "Rock Music" or music == "rock Music" or music == "metal" or music =="Metal" or music == "heavy metal" or music == "Heavy metal" or music == "Heavy Metal" or music == "heavy Metal":
    print("Cool thats my favorite type of music!")
else:
    print ("Cool I like %s." %music)