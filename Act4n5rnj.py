# Romeo and Juliet by William Shakespere game
# Montana
from time import sleep
import sys
import time
paris = False

def print_slow(paragraph):
    """
    Cool function that makes text look like its being typed out
    """

    for letter in paragraph:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.07)

# Scenes


def scene14():
    if paris == True:
        parisalive = """The next morning Friar Lawrence finds Romeo and Juliet dead.\n
He calls the Prince and the Montague's and Capulet's.\n
Lord Montague arrives.\n
Lady and Lord Capulet arrive.\n
Friar Lawrence: Lord Montague were is Lady Montague?\n
Lord Montague: Last night she died of heartbreak from Romeo being exiled.\n
Lord Capulet: What have you called us over for?\n
Friar Lawrence: Romeo and Juliet were found dead outside of your mausoleum.\n
Lord and Lady Capulet and Lord Montague: What?!\n
Friar Lawrence: Romeo came to Juliet's tomb thinking she was dead, which she was not.\n
I gave Juliet a potion that made her seem dead.\n
Romeo came and was killed by Paris, thinking he was a trespasser.\n
All of this wouldn't have happened if your two families didn't have a feud. They would be alive.\n
From now on be kind to each other and don't fight!\n
THE END\n
"""
        print_slow(parisalive)
        sleep(3)
        gameover = """This was Romeo and Juliet a Text Based Game.\n
"""
        print_slow(gameover)
        exit()
    if paris == False:
        parisdead = """The next morning Friar Lawrence finds Romeo and Juliet dead.\n
He calls the Prince and the Montague's and Capulet's.\n
Lord Montague arrives.\n
Lady and Lord Capulet arrive.\n
Friar Lawrence: Lord Montague were is Lady Montague?\n
Lord Montague: Last night she died of heartbreak from Romeo being exiled.\n
Lord Capulet: What have you called us over for?\n
Friar Lawrence: Romeo, Juliet, and Paris were found dead inside of your mausoleum.\n
Lord and Lady Capulet and Lord Montague: What?!\n
Friar Lawrence: Romeo came to Juliet's tomb thinking she was dead, which she was not.\n
I gave Juliet a potion that made her seem dead.\n
Romeo came and killed himself, thinking Juliet was dead.\n
All of this wouldn't have happened if your two families didn't have a feud.  They would be alive.\n
From now on be kind to each other and don't fight!\n
THE END\n
"""
        print_slow(parisdead)
        sleep(3)
        gameover = """This was Romeo and Juliet a Text Based Game.\n
"""
        print_slow(gameover)
        exit()




def scene13():
    global paris
    opening13 = """Romeo arrives at the mausoleum of the Capulet's.\n
Romeo: Balthasar are you there?\n
Balthasar: Yes, I am here.\n
Romeo: Stay here, and keep watch. Whistle to me if you see anyone.\n
Romeo goes to the entrance of the Capulet's mausoleum.\n
He breaks it open with a crowbar.\n
County Paris enters the graveyard, and sees Balthasar sleeping on the ground.\n
Paris draws his sword when he sees Juliet's tomb is open.\n
Paris: Hello! Anyone there?\n
Romeo hears Paris and in the dark sneaks up on him.\n
"""
    print_slow(opening13)
    attack = input("Should Romeo attack Paris? y or n: ")
    if attack == "y":
        tackle = """Romeo tackles Paris.\n
Paris slashes at Romeo and hits him on the arm.\n
Romeo manages to take Paris's sword.\n
Romeo stabs Paris in the stomach.\n
Paris: Ohh, y-you are Romeo, how d-dare you enter h-her t-tomb-\n
Paris dies, Romeo walks back into Juliet's tomb.\n
Romeo: I shall take this potion and soon I will be with you Juliet!\n
"""
        print_slow(tackle)
        potion = input("Should Romeo take the potion? y or n: ")
        if potion == "y":
            potiony = """Romeo takes the potion.\n
Right as he takes the potion Juliet awakes!\n
Romeo sees her eyes open, but then falls to the ground being killed by the potion!\n
Juliet looking into Romeo's dying eyes says\n
Juliet: Why did you take the poison but not leave a drip to take me with you?\n
Then Juliet sees a knife and stabs herself with it.\n
Juliet dies next to Romeo.\n
"""
            print_slow(potiony)
            loading = """
loading next scene\n
||||||||||||||||||||||||||||||||||||||||||||||\n"""
            print_slow(loading)
            sleep(3)
            scene14()

        else:
            potionn = """Romeo throws the potion to the ground breaking it!\n
Juliet awakes!\n
Romeo: I thought you were dead!\n
Juliet: Didn't Friar give you the letter to tell you I was not actually dead?!\n
Romeo: No!\n
Romeo and Juliet run off to Mantua to live together.\n
THE END\n
"""
            print_slow(potionn)
            sleep(3)
            redo = """As you know, since you picked for Romeo to not kill himself you got this ending.\n
                    Do you want to restart the scene and chose the other ending?\n
                    """
            print_slow(redo)
            reedo = input("type y to restart the scene, type n to end the game. y or n: ")
            if reedo == "y":
                restart = """
restarting scene\n
||||||||||||||||||||||||||||||||||||||||||||||\n"""
                print_slow(restart)
                sleep(3)
                scene13()
            else:
                gameover = """This was Romeo and Juliet a Text Based Game.\n
            """
                print_slow(gameover)
                exit()
    else:
        paris = True
        nattack = """Romeo doesn't attack Paris.\n
Paris: You are Romeo! You killed Tybalt and you are banished, you must die!\n
Then Paris stabs Romeo.\n
Romeo dies outside Juliet's tomb.\n
Paris walks into Juliet's tomb.\n
Juliet wakes up!\n
Juliet: Paris? Romeo was supposed to be here!\n
Juliet walks outside the tomb and sees Romeo dead.\n
She sees a potion in Romeo's hand and takes it!\n
Juliet dies next to Romeo.\n
"""
        print_slow(nattack)
        loading = """
        loading next scene\n
        ||||||||||||||||||||||||||||||||||||||||||||||\n"""
        print_slow(loading)
        sleep(3)
        scene14()



def scene12():
    opening12 = """In Mantua, Romeo waits for Balthasar to give him a message from Juliet.\n
Romeo: How's Juliet? She is probably as fine as the night sky. Hopefully she is not ill.\n
Balthasar: Juliet is not ill. She will never be ill again for she is in heaven.\n
Romeo: H-heaven? She is dead?!\n
Balthasar: She was found dead yesterday, and now is in the mausoleum of the Capulet's.\n
Romeo: Do you have a piece of paper I can use?\n
Balthasar: Why?\n
Romeo: I need you to deliver a letter to my father, Lord Montague, after I kill myself next to Juliet!\n
Balthasar: You don't need to do this!\n
"""
    print_slow(opening12)
    pick = input("Should Romeo go kill himself next to Juliet? y or n: ")
    if pick == "y":
        killy = """Romeo: I will do this, and you can't stop me!\n
Romeo gives the letter he just wrote to Balthasar.\n
Romeo: Go and meet me at the mausoleum tonight, were I will kill myself!\n
Balthasar rides back to Verona.\n
Romeo goes to an apothecary to by poison.\n
Romeo: I need you to give me poison and I will pay you handsomely.\n
Apothecary: I can't if I do I will get a death penalty!\n
Romeo: You need the money, give me the poison!\n
Romeo gets the poison and heads towards Verona.\n
"""
        print_slow(killy)
        loading = """
loading next scene\n
||||||||||||||||||||||||||||||||||||||||||||||\n"""
        print_slow(loading)
        sleep(3)
        scene13()

    else:
        killn = """ Romeo I should not kill myself.\n
Romeo heads to Juliet's grave and pays his respects.\n
Juliet wakes up and Friar Lawrence is there to take them to Mantua.\n
THE END\n
"""
        print_slow(killn)
        sleep(3)
        redo = """As you know, since you picked for Romeo to not kill himself you got this ending.\n
        Do you want to restart the scene and chose the other ending?\n
        """
        print_slow(redo)
        reedo = input("type y to restart the scene, type n to end the game. y or n: ")
        if reedo == "y":
            restart = """
restarting scene\n
||||||||||||||||||||||||||||||||||||||||||||||\n"""
            print_slow(restart)
            sleep(3)
            scene12()
        else:
            gameover = """This was Romeo and Juliet a Text Based Game.\n
"""
            print_slow(gameover)
            exit()


def scene11():
    opening11 = """Juliet arrives back at House Capulet.\n
She talks to her parents and tells them she is fine marrying Paris.\n
Lord Capulet, joyed by this, makes the wedding one day earlier.\n
Juliet knowing the wedding is tomorrow asks The Nurse if she can be alone in her room tonight.\n
Juliet goes to bed.\n
She takes out the sleeping potion that Friar Lawrence gave her.\n
Juliet: Should I take this?\n
What if Friar Lawrence is wrong and the potion kills me?!\n
"""
    print_slow(opening11)
    potion = input("Should Juliet take the sleeping potion? y or n: ")
    if potion == "y":
        take = """Juliet takes the sleeping potion.\n
The next morning House Capulet is busy with preparing the wedding.\n
Lord Capulet: Nurse! Can you go wake Juliet to get ready for the wedding.\n
The Nurse: Juliet! Ooo Juliet!\n
The Nurse enters Juliet's room...     \n
Lord and Lady Capulet run to Juliet's room.\n
When they arrive they see Juliet lying there not moving.\n
The Nurse: She's Dead!\n
Everyone in the room, Lord Capulet, Lady Capulet, The Nurse, start wailing in sorrow.\n
Lady Capulet: First Tybalt! Now Juliet, m-my only d-daughter!\n
Friar Lawrence enters the room after hearing the screams of Juliet's parents after realizing their daughter is dead.\n
Friar Lawrence: She is in a better place now, she was so smart. Why would she do this?!\n
They cancel the wedding and bring Juliet to their mausoleum, and lie Juliet on a slab next to Tybalt.\n
"""
        print_slow(take)
        loading = """
loading next scene\n
||||||||||||||||||||||||||||||||||||||||||||||\n"""
        print_slow(loading)
        sleep(3)
        scene12()
    else:
        notake = """Juliet throws the potion out of her window.\n
The next morning House Capulet is busy with preparing the wedding.\n
Lord Capulet: Nurse! Can you go wake Juliet to get ready for the wedding.\n
The Nurse: Juliet! Ooo Juliet!\n
The Nurse enters Juliet's room...       \n
Lord and Lady Capulet run to Juliet's room.\n
When they arrive they see Juliet's bed is empty and the Nurse is holing a note.\n
Lord Capulet: Give me that!\n
Lady Capulet: What does it say?\n
Lord Capulet: Dear, Mom and Dad. I will not see you again, I have run off.\n
Love Juliet.\n
Lady Capulet: Where has she gone to?\n
The Nurse: I know!
Juliet arrives at the church surprising Friar Lawrence.\n
Friar Lawrence: I told you to take the potion!\n
Juliet: But I didn't. Take me to Romeo!\n
Friar Lawrence: Ok, he will be surprised.\n
The Nurse and Lord and Lady Capulet enter the church.\n
Juliet and Friar Lawrence ride to Mantua to meet Romeo.\n
The End\n
"""
        print_slow(notake)
        sleep(3)
        redo = """As you know, since you picked for Juliet to not take the potion you got this ending.\n
Do you want to restart the scene and chose the other ending?\n
"""
        print_slow(redo)
        reedo = input("type y to restart the scene, type n to end the game. y or n: ")
        if reedo == "y":
            restart = """
restarting scene\n
||||||||||||||||||||||||||||||||||||||||||||||\n"""
            print_slow(restart)
            sleep(3)
            scene11()
        else:
            gameover = """This was Romeo and Juliet a Text Based Game.\n
"""
            print_slow(gameover)
            exit()


def scene10():
    opening10 = """Juliet arrives at the church,\n
She walks inside and sees Paris is there.\n
Paris: Hello Juliet.\n
Juliet: Hello County Paris.\n
Paris: Goodbye.\n
Friar Lawrence walks over to Juliet.\n
Juliet show Friar Lawrence a knife.\n
Juliet: If I don't get out of this marriage I will use the knife on myself.\n
Friar Lawrence: Ok, I'll help you.\n
Juliet: Good.\n
Friar Lawrence: I have a plan.\n
"""
    print_slow(opening10)

    plan = input("Should Juliet listen to Friar Lawrence's plan? y or n: ")
    if plan == "y":
        yplan = """Juliet listens to Friar Lawrence's plan.\n
Friar Lawrence: I have this potion that will make you seem like you are dead for ten hours.\n
Take this the night before your marriage to County Paris.\n
They will think you are dead, and put you in the mausoleum of the Caplet's.\n
There, Romeo and I will find you and wake you so you two can run off.\n
Juliet: How will Romeo know I am not actually dead?\n
Friar Lawrence: Leave that to me, now go!\n
"""
        print_slow(yplan)
        loading = """
loading next scene\n
||||||||||||||||||||||||||||||||||||||||||||||\n"""
        print_slow(loading)
        sleep(3)
        scene11()

    else:
        nplan = """Juliet doesn't listen to Friar Lawrence's plan.\n
Juliet runs off and kills herself with the knife.\n
GAMEOVER\n
"""
        print_slow(nplan)
        restart = """
restarting scene\n
||||||||||||||||||||||||||||||||||||||||||||||\n"""
        print_slow(restart)
        sleep(3)
        scene10()


