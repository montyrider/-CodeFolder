# Romeo and Juliet by William Shakespere game
# Montana
from time import sleep
import sys
import time
import Act3rnj


def print_slow(paragraph):
    """
    Cool function that makes text look like its being typed out
    """

    for letter in paragraph:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.07)


# Scenes


def scene6():
    opening6 = """Romeo and Friar Lawrence are waiting in the church for Juliet.\n
Juliet arrives at the church with The Nurse,\n
The Nurse: Are you sure about this?\n
Juliet: I am sure nothing's going to happen.\n
The Nurse: Ok.\n
Juliet walks over to where Romeo and Friar Lawrence are at,\n
Friar Lawrence: Are you ready to be married?\n
"""
    print_slow(opening6)
    yes = input("Do Romeo and Juliet want to get married. y or n: ")
    if yes == "y":
        rjyes = """Romeo: Yes.\n
Juliet: Yes.\n
Friar Lawrence: In the name of the lord you two are pronounced bride and groom.\n
Romeo and Juliet run off, out of the church.\n
They split when Juliet reaches The Nurse.\n
"""
        print_slow(rjyes)

        loading = """
loading next scene\n
||||||||||||||||||||||||||||||||||||||||||||||\n"""
        print_slow(loading)
        sleep(3)
        Act3rnj.scene7()


    else:
        rjno = """Romeo does not want to get married and runs out of the church,\n
On the way out he passes The Nurse.\n
Juliet still inside dumbfounded by Romeo, runs out to The Nurse.\n
GAMEOVER\n
"""
        print_slow(rjno)

        restart = """
restarting scene\n
||||||||||||||||||||||||||||||||||||||||||||||\n"""
        print_slow(restart)
        sleep(3)
        scene6()


def scene5():
    opening5 = """The Friar, Lawrence, of the church is picking herbs in his garden.\n
Romeo comes running down the fields,\n
Friar Lawrence: Romeo, where have you been up so early\n
oh, you haven't slept.\n
Romeo: I hath been with the most beautiful women.\n
Friar Lawrence: Rosaline?\n
Romeo: Juliet of Lord Capulet.\n
Friar Lawrence: You have left Rosaline, after weeping over her love?\n
Romeo: Yes, but Juliet I do love now, we're getting married today.\n
Friar Lawrence: By whom?\n
Romeo: You! I have come here to ask you to marry us.\n
Friar Lawrence: I will for you, and to help the conflict of both your houses.\n
"""
    print_slow(opening5)
    loading = """
    loading next scene\n
    ||||||||||||||||||||||||||||||||||||||||||||||\n"""
    print_slow(loading)
    sleep(3)
    scene6()


def scene4():
    opening4 = """Benvolio and Mercutio are outside of the walls of House Capulet.\n
Benvolio: Romeo where are you!\n
 Romeo!\n
At the foot of one of House Capulet's walls, Romeo, started climbing up.\n
On the wall there are vines and brush that you can climb,\n
Romeo is climbing on the vines and brush.\n
The vegetation stops suddenly and it is just a stone wall,\n
Romeo sees two rocks, one a very large rock, and the other a small rock sticking out just enough to grab.\n
"""
    print_slow(opening4)

    wall = input("Which rock should Romeo pick the (L)arge rock or the (S)mall rock: ")
    if wall == "l":
        large = """Romeo grabs a hold of the large rock,\n
He puts his other hand on a rock above but then the large rock slips out of place!\n
He falls ten meters and then...      \n
BLOP!\n
He falls from the sky and sees the top of the castle wall.\n
He grabs for a rock but then slips and falls to the ground,\n
at the bottom of the ground he lies paralyzed.\n
"""

        print_slow(large)

        restart = """
restarting scene\n
||||||||||||||||||||||||||||||||||||||||||||||\n"""
        print_slow(restart)
        sleep(3)
        scene4()
    elif wall == "s":
        small = """Romeo grabs the small rock and climbs up to the top of the wall.\n
There he sees a light coming from the east window,\n
Romeo: The Sun is to the East and Juliet is the Sun.\n
He goes to the East window and finds Juliet and woos her.\n
The Nurse calls her,\n
The Nurse: Juliet!\n
Juliet: Romeo I have to go.\n
Romeo: We must get married.\n
Juliet: When?\n
Romeo: Tomorrow at the hour of nine!\n
Juliet goes to The Nurse\n
Romeo climbs over the wall again and runs to the church.\n
"""
        print_slow(small)
        loading = """
        loading  cut scene\n
        ||||||||||||||||||||||||||||||||||||||||||||||\n"""
        print_slow(loading)
        sleep(3)
        scene5()


def scene3():
    opening3 = """They walk onto the dance floor,\n
There are many people on this dance floor,\n
One of them is Rosaline, which Romeo says he loves.\n
Rosaline is dancing with someone, Romeo thinks she will not love him now and looks around the room.\n
From his peripheral he sees a flash of red coming from the right, and a someone dancing to his left.\n
"""
    print_slow(opening3)
    look = input("Do you want Romeo to look (R)ight or (L)eft")
    if look == "r":
        right = """He turns his head to the right and sees a magnificent dancer in red.\n
He thinks they dance like an angel,\n
The music stops and everyone leaves the dance floor.\n
Sitting next to Lord Capulet in his throne, Tybalt, spies Romeo as a Montague.  \n
He asks Lord Capulet if he can confront him.\n
"""
        print_slow(right)
        confront = input("Should Lord Capulet let Tybalt confront Romeo? y or n: ")
        if confront == "y":
            attack = """Tybalt starts walking towards Romeo and confronts him.\n
Tybalt: Romeo! I know you a Montague, you should not be here!\n
And I a Capulet shall cap you!\n
Tybalt throws the cap of his drink at Romeo, hitting him square in the forehead.\n
Romeo shakes it off.\n
Lord Capulet: Tybalt leave him!\n
Tybalt leaves Romeo and goes to Capulet.\n
\n
Romeo now walks over to the angel of a dancer he sees,\n
Romeo: Hello, may I speak with you?\n
The dancer he is talking to is Juliet, the only daughter of Lord Capulet.\n
Juliet is stunned by Romeo.\n
Juliet: You may speak.\n
Romeo: You are a marvellous dancer.\n
Juliet: Thank you, you are stunning.\n
It is love at first sight.\n
But Lord Capulet announces that the feast is over.\n
Juliet is led off by her maiden Then Nurse.\n
Juliet: Nurse can you get his name?\n
The Nurse runs off and asks Romeo his name.\n
He gives it to her and in return The Nurse gives him Juliet's name.\n
"""
            print_slow(attack)
            loading = """
loading next scene\n
||||||||||||||||||||||||||||||||||||||||||||||\n"""
            print_slow(loading)
            sleep(3)
            scene4()
        else:
            meet = """Tybalt is told to sit down and starts pouting.\n
Romeo walks over to the angel of a dancer he sees,\n
Romeo: Hello, may I speak with you?\n
The dancer he is talking to is Juliet, only daughter of Lord Capulet.\n
Juliet is stunned by Romeo.\n
Juliet: You may speak.\n
Romeo: You are a marvellous dancer.\n
Juliet: Thank you, you are stunning.\n
It is love at first sight.\n
But Lord Capulet announces that the feast is over.\n
Juliet is led off by her maiden Then Nurse.\n
Juliet: Nurse can you get his name?\n
The Nurse runs off and asks Romeo his name.\n
He gives it to her and in return The Nurse gives him Juliet's name.\n
"""
            print_slow(meet)
            loading = """
loading next scene\n
||||||||||||||||||||||||||||||||||||||||||||||\n"""
            print_slow(loading)
            sleep(3)
            scene4()
    else:
        devito = """Romeo walks over to the dancer that he sees.\n
Romeo: Hello, may I speak with you?\n
The person he is talking to is a 4'10" person with glasses and has a bald head, except for two lengths of hair on both\n
sides of their head.\n
Danny of DeVito: Hello I am Danny of DeVito, you may speak with me!\n
Romeo faints and wakes at his house.\n
"""
        print_slow(devito)
        restart = """
restarting scene\n
||||||||||||||||||||||||||||||||||||||||||||||\n"""
        print_slow(restart)
        sleep(3)
        scene3()


def scene2():
    opening2 = """Benvolio, Mercutio, a friend of Benvolio, and Romeo, the son of Lord Montague, are walking down an alley\n
They are headed to a feast hosted by Lord Capulet.\n
It is a masked dance and feast, which means the Capulets' can't tell that Romeo and Benvolio are Montagues.\n
At the end of the alley there are two paths, both seem to lead to the feast,\n
The way on the right is shining bright as the heart of a torch.\n
The left is as dark as a shark's eye.\n
"""
    print_slow(opening2)
    alley = input("Which way do you want them to head (L)eft or (R)ight: ")
    if alley == "l":
        left = """They go down the pitch black alley.\n
A couple meters down the alley they make a right turn into a well lit road.\n
They see others walking with them, all carrying masks, headed to the feast.\n
On the rest of the walk Mercutio rants of Queen Mab, the fairies mid-wife who is as small as an agate stone.\n
Once Romeo calms Mercutio down they head into the feast.\n
"""
        print_slow(left)
        loading = """
loading next scene\n
||||||||||||||||||||||||||||||||||||||||||||||\n"""
        print_slow(loading)
        sleep(3)
        scene3()
    else:
        right = """ They head towards the shining alley way.\n
They can barely see because of the light,\n
Their eyes scorch from the light in the air.\n
They fall to their knees, and start to crawl on all fours,\n
Romeo feels a step with his hands, and tells everyone to move forward.\n
Once they crawl to the drop off, they fall into an endless pit cursed for eternity\n
"""
    print_slow(right)
    restart = """
restarting scene\n
||||||||||||||||||||||||||||||||||||||||||||||\n"""
    print_slow(restart)
    sleep(3)
    scene2()


def scene1():
    opening = """In the isles of Verona's street market\n
Sampson and Gregory Capulet spy Abram and Balthasar rival House Montague\n
"""
    print_slow(opening)
    fight = input("Do you want them to fight? y or n: ")
    if fight == "y":
        theyfight = """ Sampson bites his thumb at Abram, a sign of disrespect!\n
Abram: If you bite your thumb at us sir, then we must fight.\n
They all fight along with the other people in the market.\n
Out of nowhere Benvolio, a Montague starts getting attacked by Tybalt, a Capulet.\n
Tybalt hits Benvolio with a mackerel.\n
Benvolio hits Tybalt with a baguette.\n
The Prince comes in and stops the fighting.\n
Prince: Montague, Capulet this is the second time you have started a fight in my city! Next time you will be\n
thrown out of it! Montague see me this afternoon, Capulet come with me now!\n
"""

        print_slow(theyfight)
        loading = """
loading next scene\n
||||||||||||||||||||||||||||||||||||||||||||||\n"""
        print_slow(loading)
        sleep(3)
        scene2()

    elif fight == "n":
        theyfight = """ Abram bites his thumb at Sampson, a sign of disrespect.\n
Sampson: If you bite your thumb at us sir, then we must fight.\n
They all fight along with the other people in the market.\n
Out of nowhere Benvolio, a Montague starts getting attacked by Tybalt, a Capulet.\n
Tybalt hits Benvolio with a mackerel.\n
Benvolio hits Tybalt with a baguette.\n
The Prince comes in and stops the fighting.\n
Prince: Montague, Capulet this is the second time you have started a fight in my city! Next time you will be\n
thrown out of it! Montague see me this afternoon, Capulet come with me now!\n
"""

        print_slow(theyfight)
        loading = """
loading next scene
||||||||||||||||||||||||||||||||||||||||||||||\n"""
        print_slow(loading)
        sleep(3)
        scene2()


def mainmenu():
    mainmenu = """Welcome to Romeo & Juliet text based game!"""
    print_slow(mainmenu)
    ready = input("Ready to play? On the first question, click next to the colon and type y or n and press enter : ")
    if ready == "y":
        start = """Great! Let The Story Begin!"""
        print_slow(start)
        intro()
    else:
        exit()


# Intro to the game
def intro():
    introop = """Romeo and Juliet. A text based game.\n

Play written by William Shakespere\n

Game programmed by Montana Sanchez.\n

Starting game\n
||||||||||||||||||||||||||||||||||||||||||||||\n
Loading Verona\n
||||||||||||||||||||||||||||||||||||||||||||||\n
Placing characters\n
||||||||||||||||||||||||||||||||||||||||||||||\n

"""
    print_slow(introop)
    sleep(3)
    scene1()


mainmenu()
