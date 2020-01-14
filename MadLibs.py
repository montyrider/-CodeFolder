#Montana
#MasLibs
from time import sleep
#IntroSection
print ("Welcome to MadLibs")
sleep(1)
ready = input ("Ready to play? y or n:")
if ready == "y":
    print ("Great! Let's get started.")
else:
    exit()

#Variables
setting0 = input ("Setting for your story:")
noun0 = input ("Thing:")
noun1 = input ("Things Plural:")
setting1 = input ("LivingPlace Plural:")
adjective0 = input ("Adjective:")
adjective1 = input ("Adjective:")
setting2 = input ("A Place:")
chrctr = input ("Character from a Book:")
noun2 = input ("Person/Place/Thing Plural:")
name0 = input ("Name of person in room:")
name1 = input ("Your Name:")
setting3 = input ("A Place:")
noun3 = input ("Person/Place/Thing Plural:")
noun4 = input ("Person/Place/Thing Plural:")
noun5 = input ("Person/Place/Thing:")
setting4 = input("A place:")
#StorySection
print("     ")
print(" ")
print ("Once upon a time in", setting0,"there was a", noun0 + ".""That",noun0,"was one of many", noun1,"that lived in",setting1, ".")
print ("All the", setting1,"that they lived in where", adjective0,"and", adjective1, ".")
print ("they all went on a trip to", setting2," for", chrctr, "Day. There they ran.")
print ("During the run a", noun2,"fell out of the sky and hit", name0," on the head")
print ("The next day", name0, "was still knowcked out!",name1," was hoping no more", noun2,"where falling out of the sky.")
print ("It's weird being in",setting3,".""then everyone saw",noun3,"knocking down bulidings and eating gigantic",noun4,".")
print ("Luckly a flying",noun5,"rescued everyone and took them to",setting4,",""The End.")