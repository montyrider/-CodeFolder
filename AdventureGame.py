#Montana
#AdventureGame
from time import sleep

#Global Booleen
torch = False
key = False
paper = False
orcrus = False
#StartingMenu
def MainMenu():
    global name
    print ("Welcome The Obsidian Castle! An adventure game.")
    #imputName
    name = input ("Enter a Name for your Character! choose wisley:")
    sleep(1)
    ready = input ("Ready to play? y or n:")
    if ready == "y":
        print ("Great! Let Your Adventure Begin!")
        Intro()
    else:
        exit()
        
                
#Intro    
def Intro ():
    global name
    print("It was a foggy night, and at The Obsidian Castle",name,"traveled deep into the castle's keep to discover unknown secrets.")
    sleep(1)
    print("The Obsidian Castle has many stories. Many courageous adventurers have traveled to this legend of a castle.")
    sleep(2)
    print("But none have returned...")
    MainRoom()
    
    
#Epilogue
def Epilogue ():
    if orcrus == True:
        print ("After",name," slayed the Dragon",name," found and took the treasures from the Dragon's lair.")
        print ("The treasures consisted of gold, silver, and bronze coins by the millions!")
        print ("There was also all types of jewels some never seen")
        print (name,"Becomes a legend for finding the legendary obsidian sword Orcrus!")
        print ("and now our journey has come to a end")
        print ("Thankyou for playing my game and congtulations on winning!")
        exit()
    if orcrus == False:    
        print ("After",name," slayed the Dragon",name," found and took the treasures from the Dragon's lair.")
        print ("The treasures consisted of gold, silver, and bronze coins by the millions!")
        print ("There was also all types of jewels some never seen")
        print ("and now our journey has come to a end")
        print ("Thankyou for playing my game and congtulations on winning!")
        exit()


#EasterEggRoom
def EasterEgg ():
    print ("You see a bright room with black walls and green letters and numbers running down it")
    print ("But on one walls you see text spelling")
    sleep(1)
    print ("GAME CREATED BY MONTANA R SANCHEZ HELP FROM ZOGI!")
    print ("You exit the room of WitchCraft!")
    sleep(2)
    GoldenDoor ()
    
    
#EndRoom
def EndRoom ():
    global orcrus
    if orcrus == True:
        print ("You burst through the door to find a red scaled monsterous Dragon!\nIt's  claws like spears, teeth like swords, and wings like hurricanes!")
        sleep(1)
        print ("You pull out Orcrus and run at the Dragon!")
        pick = input ("do you want to stab the Dragon in the (h)eart or (t)hroat?!")
        if pick == "h":
            print ("You stab the Dragon through the heart!")
            print ("It claws at you through the agony! It cuts your arm, then the Dragon falls dead")
            sleep(1)
            Epilogue()
        elif pick == "t":
            print ("You slit the Dragon's throat fire streams out of the cut scorching the stone floor")
            sleep(1)
            print ("Then the Dragon falls on the ground dead.")
            sleep(1)
            Epilogue()
            
    print("This Dragon lays in mountains of  shining bright treasure!\nYou see a pile of bones from many past Travelers the Dragon devoured!")
    if orcrus == False:
        print ("You burst through the door to find a red scaled monsterous Dragon!\nIt's  claws like spears, teeth like swords, and wings like hurricanes!")
        sleep(1)
        print("This Dragon lays in mountains of  shining bright treasure!\nYou see a pile of bones from many past Travelers the Dragon devoured!")
        sleep(2)
        print ("you look around for a weapon! You spot a Longsword and a Bow with only 14 arrows")
        sleep(1)
        pick = input ("Which will you pick to kill this foul beast, the (s)word or the (b)ow?!")
        if pick == "s":
            print ("You pick up the Longsword")
            sleep(1)
            print ("The Dragon spits fiery ball of flames at you")
            move = input ("which way will you go to avoid the scorching fire\n (l)eft of (r)ight")
            if move == "l":
                print ("You avoid the flames slash at the Dragon")
                sleep(1)
                print ("you cut the Dragon's chest severly wounding it")
                sleep(1)
                print ("The Dragon spits fire at you again")
                move = input ("which way will you go to avoid the scorching fire\n (l)eft of (r)ight")
                if move == "r":
                    print ("You barely avoid the flames and stab the Dragon")
                    print (" you hit it in the heart killing it!")
                    sleep(2)
                    Epilogue ()
                else:
                    print ("You burn up in flames")
                    sleep(2)
                    EndRoom ()
            elif move == "r":
                print ("You burn up in flames")
                sleep(2)
                EndRoom ()
        elif pick == "b":
            print ("You pick up the Bow and arrows")
            sleep(1)
            print ("The Dragon spits fire at you")
            move = input ("which way will you go to avoid the scorching fire\n (l)eft of (r)ight")
            if move == "l":
                print ("You avoid the flames and take a shot at the Dragon")
                shot = input ("will you shoot at the (e)yes or the (h)eart?")
                if shot == "e":
                    print ("You Blind the beast")
                    print ("It spits fire at you")
                    move = input ("which way will you go to avoid the scorching fire\n (l)eft of (r)ight")
                    if move == "r":
                        print ("You avoid the flames and shoot at the Dragon")
                        print ("Your arrow pierces through the Dragon's scales and hits it in the heart killing it!")
                        sleep(2)
                        Epilogue ()
                    else:
                        print ("You die to the Dragon's flames!")
                        sleep(2)
                        EndRoom()
                else:
                    print ("The Dragon blocks the shot and blows flames on you buring you to a crisp")
                    sleep(2)
                    EndRoom()
            else:
                print ("You run towards the fire and burn to a crisp")
                sleep(2)
                EndRoom()
        


#LeftRoom
def GoldenDoor ():
    global torch
    global paper
    if torch == False:
        print("This room is dark and the only thing you can make out is a door and some chairs")
        sleep(1)
        print("You choose to go back to the Mainroom and and through the silver door")
        sleep(2)
        SilverDoor ()
    elif key == True:
        print ("You go to unlock the door")
        sleep(1)
        print ("Whilst unlocking the door you hear a loud (ROAR!) as if from some kind of ferocious beast")
        sleep(2)
        EndRoom ()
    elif torch == True:
        print ("You see a door and chairs but the door has a lock on it")
        sleep (2)
        search = input ("Will you search the (t)able and chairs or the (w)hole room")
        if search == "t":
            print ("You find a piece of parchment paper underneath a torn up book.")
            paper = True
            print ("the paper say the key is in the dungeon")
            go = input ("Will you go to the (d)ungeon or look around the (w)hole room")
            if go == "d":
                print ("You go to the Dungeon")
                sleep(1)
                Dungeon()
            else:
                print ("You search the room and you find a secrect passage and you go through.")
                EasterEgg ()
        else:
            print ("You search the room and find a secret passage way and you through")
            EasterEgg ()
    
 
 
 
#RightRoom
def SilverDoor ():
    global torch
    global orcrus
    if key == True:
        print ("You see a door appear on the wall")
        go = input ("Do you want to go through the (m)agical door or go to the (g)oldenDoor")
        if go == "m":
            print ("You go throught the door to find the legendary Obsidian sword Orcrus!")
            orcrus = True
            print ("You head back to the through the GoldenDoor.")
            sleep(2)
            GoldenDoor()
        else:
            print ("You go back through the GoldenDoor.")
            sleep(2)
            GoldenDoor()
    
    print ("There is a torch on the wall that looks loose")
    print ("The torch is latched on to the cold stone walls but is taken off with ease.")
    sleep(1)
    take = input ("Take the torch? y or n: ")
    if take == "y":
        torch = True
        print ("With the torch you see a passage leading to a dark room.")
        move = input ("will you go back to the (m)ain room and through the gold door or go to the (d)ark room.")
        if move == "d":
            Dungeon ()
        else:
            ("print you go through the main room and enter the goldroom")
            GoldenDoor()
    else:
        print ("You see a very dark passage to a dark room")
        move = input ("will you go back to the (m)ain room and through the gold door or go to the (d)ark room.")
        if move == "d":
            Dungeon ()
        elif move == "m":
            ("print you go through the main room and enter the goldroom")
            GoldRoom()
            
            
            
def MainRoom ():
    print ("You have entered the room behind the keep's large wooden doors.")
    print ("The room is dark, only faintly lit by a magical ever buring torch.")
    sleep(1)
    print("On your right is a silver door and on your left is a golden door")
    sleep(1)
    move = input("Would you like to go (r)ight or (l)eft? ")
    if move == "r":
        SilverDoor ()
    else:
        print ("You go through te Golden door.")
        GoldenDoor ()
        
           
        
#Dungeon
def Dungeon ():
    global torch
    global paper
    global key
    if torch == False:
        print("this room is too dark to explore")
        sleep(2)
        SilverDoor ()
    elif paper == True:
        print ("You look for the key")
        search = input ("Do you want to look for the key in cell (1) or cell (2)")
        if search == "1":
            print ("You look and find the key barried in a pile of armour in the corner of the cell!")
            key = True
            secret = input ("Do you want to head back through the (g)oldenDoor or (s)ilverDoor?.")
            if secret == "s":
                SilverDoor()
            else:
                GoldenDoor()
    
        else:
            print ("You find a skeleton of a past prisoner clenching to the bars as if they're final moments were begging to be freed.")
            print ("But you don't find the key")
            Dungeon()
    elif torch == True:
        print("You look around the room and only find skeletons of prisoners")
        print("You go through back to the main room and through the golden door")
        GoldenDoor()
    
  
#Runs The Whole Thing!!!  
MainMenu()