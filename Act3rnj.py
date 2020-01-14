# Romeo and Juliet by William Shakespere game
# Montana
from time import sleep
import sys
import time
import Act4n5rnj

def print_slow(paragraph):
    """
    Cool function that makes text look like its being typed out
    """

    for letter in paragraph:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.07)


# Scenes


def scene9():
    cutsscene = """Romeo climbs over the wall of House Capulet.\n
He knocks on Juliet's room window.\n
Juliet let's him in.\n
Juliet: Why did you kill Tybalt?\n
Romeo: He killed Mercutio.\n
Romeo stays with Juliet till the morning.\n
The Nurse: Juliet! Breakfast!\n
Juliet: Ok! Romeo you need to leave.\n
Romeo climbs out of Juliet's window.\n
The Nurse enters Juliet's room along with Lady Capulet.\n
Lady Capulet: Juliet you are to be married to County Paris this Wednesday.\n
Juliet: I'd rather marry Romeo than Paris!\n
Lady Capulet does not know Juliet is married to Romeo already.\n
Lady Capulet storms away.\n
Juliet: Nurse what do you think I should do?!\n
The Nurse: I think you should marry Paris, Romeo is practically dead!\n
Juliet is disgusted by The Nurse's explanation.\n
Juliet: Ok, but I need to go confess to the Friar.\n
Juliet leaves House Capulet and starts running to the church.\n
"""
    print_slow(cutsscene)
    loading = """
            loading next scene\n
            ||||||||||||||||||||||||||||||||||||||||||||||\n"""
    print_slow(loading)
    sleep(3)
    Act4n5rnj.scene10()


def scene8():
    opening8 = """At House Capulet Juliet is waiting for Romeo to come to her.\n
The Nurse enters Juliet's room.\n
The Nurse: Tybalt is slain, and Romeo shall be dead!\n
Juliet: Tybalt and Romeo are dead?\n
The Nurse: No, Tybalt was slain by vile Romeo and Romeo is exiled.\n
If he returns he shall face death!\n
Juliet: Romeo is my husband and you want him dead?\n
The Nurse: I am sorry.\n
Juliet: Go find him and give him this ring.\n
"""
    print_slow(opening8)
    ring = input("Should The Nurse give Romeo the ring from Juliet? y or n: ")
    if ring == "y":
        yes = """The Nurse finds Romeo at the church with Friar Lawrence.\n
The Nurse gives Romeo the ring and leaves.\n
Friar Lawrence: Romeo you need to get out of town.\n
Romeo: But how?\n
Friar Lawrence: Go comfort Juliet and make sure not to be seen.\n
After that go to Mantua, where I will send you any news.\n
Romeo: Ok.\n
"""
        print_slow(yes)
        loading = """
        loading cutscene\n
        ||||||||||||||||||||||||||||||||||||||||||||||\n"""
        print_slow(loading)
        sleep(3)
        scene9()

    else:
        no = """The Nurse does not go and find Romeo or gives him the ring.\n
In the church Romeo and Friar Lawrence talk.\n
Friar Lawrence: Romeo you need to get out town.\n
Romeo: But how?\n
Friar Lawrence: Go comfort Juliet and make sure not to be seen.\n
After that go to Mantua, where I will send you any news.\n
Romeo: Ok.\n
"""
        print_slow(no)
        loading = """
                loading cutscene\n
                ||||||||||||||||||||||||||||||||||||||||||||||\n"""
        print_slow(loading)
        sleep(3)
        scene9()


def scene7():
    opening7 = """Benvolio and Mercutio walk in the main street of Verona.\n
Benvolio: Methinks we should go inside.\n
Mercutio: You want to go inside just because of some Capulets?\n
Benvolio: There might be a brawl!\n
Tybalt, a Capulet, sees Benvolio and Mercutio.\n
"""
    print_slow(opening7)

    fight = input("Should Tybalt start a fight with Mercutio and Benvolio? y or n: ")
    if fight == "y":
        brawl = """Tybalt walks up to Mercutio and Benvolio.\n
Tybalt: May I speak with one of you?\n
Mercutio annoyed by this request insults Tybalt.\n
Mercutio: You sluggish, crowbrained, clotpole!\n
Romeo enters from being newly married to Juliet.\n
Romeo: What's going on here?\n
Tybalt: Mercutio just insulted me, Mercutio let us brawl!\n
Tybalt and Mercutio start fighting.\n
"""
        print_slow(brawl)

        stop = input("Should Romeo intervene and stop Tybalt and Mercutio fighting? y or n: ")
        if stop == "y":
            intervene = """Romeo jumps between Mercutio and Tybalt.\n
Tybalt stabs Mercutio from under Romeo's arm!\n
Mercutio: I've been slain! I've been slain!\n
Romeo: I didn't mean for him to kill you!\n
Mercutio: A plague o' both your houses!\n
Benvolio brings Mercutio inside to one of the nearby houses.\n
Benvolio comes back out to Romeo and Tybalt.
Benvolio: He's dead!\n
Romeo: Tybalt! YOU DID THIS!\n
Romeo runs after Tybalt drawing Mercutio's sword.\n
"""
            print_slow(intervene)
            kill = input("Should Romeo kill Tybalt? y or n: ")
            if kill == "y":
                stab = """Tybalt stands his ground.\n
But Romeo stabs him through the heart!\n
Benvolio tells Romeo to run away at once.\n
People around the fight get the Prince.\n
The Prince enters.\n
The Prince: Benvolio, tell me what happened. I see that Tybalt and Mercutio are slain.\n
Benvolio: Romeo slain Tybalt.\n
The Prince: Why?\n
Benvolio: Before Tybalt slain Mercutio.\n
The Prince: Then if Romeo slain Tybalt who slain Mercutio? Romeo shall be exiled!\n
When he is found again, he shall become dead.\n
"""
                print_slow(stab)

                loading = """
loading next scene\n
||||||||||||||||||||||||||||||||||||||||||||||\n"""
                print_slow(loading)
                sleep(3)
                scene8()

            else:
                notstab = """Tybalt stands his ground.\n
Romeo settles down.\n
Tybalt: Mercutio was slain right!\n
Then Romeo stabs him through the heart!\n
Benvolio tells Romeo to run away at once.\n
People around the fight get the Prince.\n
The Prince enters.\n
The Prince: Benvolio, tell me what happened. I see that Tybalt and Mercutio are slain.\n
Benvolio: Romeo slain Tybalt.\n
The Prince: Why?\n
Benvolio: Before Tybalt slain Mercutio.\n
The Prince: Then if Romeo slain Tybalt who slain Mercutio? Romeo shall be exiled!\n
When he is found again, he shall become dead.\n
"""
                print_slow(notstab)

                loading = """
loading next scene\n
||||||||||||||||||||||||||||||||||||||||||||||\n"""
                print_slow(loading)
                sleep(3)
                scene8()
        else:
            nointervene = """Romeo watches Tybalt and Mercutio fight.\n
Tybalt stabs Mercutio!\n
Mercutio: I've been slain! I've been slain!\n
Romeo! why didn't you help me!
Romeo: I didn't mean for him to kill you!\n
Mercutio: A plague o' both your houses!\n
Benvolio brings Mercutio inside to one of the nearby houses.\n
Benvolio comes back out to Romeo and Tybalt.
Benvolio: He's dead!\n
Romeo: Tybalt! YOU DID THIS!\n
Romeo runs after Tybalt drawing Mercutio's sword.\n
"""
            print_slow(nointervene)
            kill = input("Should Romeo kill Tybalt? y or n: ")
            if kill == "y":
                stab = """Tybalt stands his ground.\n
But Romeo stabs him through the heart!\n
Benvolio tells Romeo to run away at once.\n
People around the fight get the Prince.\n
The Prince enters.\n
The Prince: Benvolio, tell me what happened. I see that Tybalt and Mercutio are slain.\n
Benvolio: Romeo slain Tybalt.\n
The Prince: Why?\n
Benvolio: Before Tybalt slain Mercutio.\n
The Prince: Then if Romeo slain Tybalt who slain Mercutio? Romeo shall be exiled!\n
When he is found again, he shall become dead.\n
"""
                print_slow(stab)

                loading = """
loading next scene\n
||||||||||||||||||||||||||||||||||||||||||||||\n"""
                print_slow(loading)
                sleep(3)
                scene8()

            else:
                notstab = """Tybalt stand his ground.\n
Romeo settles down.\n
Tybalt: Mercutio was slain right!\n
Then Romeo stabs him through the heart!\n
Benvolio tells Romeo to run away at once.\n
People around the fight get the Prince.\n
The Prince enters.\n
The Prince: Benvolio, tell me what happened. I see that Tybalt and Mercutio are slain.\n
Benvolio: Romeo slain Tybalt.\n
The Prince: Why?\n
Benvolio: Before Tybalt slain Mercutio.\n
The Prince: Then if Romeo slain Tybalt who slain Mercutio? Romeo shall be exiled!\n
When he is found again, he shall become dead.\n
"""
                print_slow(notstab)

                loading = """
loading next scene\n
||||||||||||||||||||||||||||||||||||||||||||||\n"""
                print_slow(loading)
                sleep(3)
                scene8()
    else:
        nofight = """Tybalt walks by Mercutio and Benvolio.\n
Mercutio: You sluggish, crowbrained, clotpole!\n
Romeo enters from being newly married to Juliet.\n
Romeo: What's going on here?\n
Tybalt: Mercutio just insulted me. Mercutio let us brawl!\n
Tybalt and Mercutio start fighting.\n
"""
        print_slow(nofight)

        stop = input("Should Romeo intervene and stop Tybalt and Mercutio's fighting? y or n: ")
        if stop == "y":
            intervene = """Romeo jumps between Mercutio and Tybalt.\n
Tybalt stabs Mercutio from under Romeo's arm!\n
Mercutio: I've been slain! I've been slain!\n
Romeo: I didn't mean for him to kill you!\n
Mercutio: A plague o' both your houses!\n
Benvolio brings Mercutio inside to one of the nearby houses.\n
Benvolio comes back out to Romeo and Tybalt.
Benvolio: He's dead!\n
Romeo: Tybalt! YOU DID THIS!\n
Romeo runs after Tybalt drawing Mercutio's sword.\n
"""
            print_slow(intervene)
            kill = input("Should Romeo kill Tybalt? y or n: ")
            if kill == "y":
                stab = """Tybalt stands his ground.\n
But Romeo stabs him through the heart!\n
Benvolio tells Romeo to run away at once.\n
People around the fight get the Prince.\n
The Prince enters.\n
The Prince: Benvolio, tell me what happened. I see that Tybalt and Mercutio are slain.\n
Benvolio: Romeo slain Tybalt.\n
The Prince: Why?\n
Benvolio: Before Tybalt slain Mercutio.\n
The Prince: Then if Romeo slain Tybalt who slain Mercutio? Romeo shall be exiled!\n
When he is found again, he shall become dead.\n
"""
                print_slow(stab)

                loading = """
loading next scene\n
||||||||||||||||||||||||||||||||||||||||||||||\n"""
                print_slow(loading)
                sleep(3)
                scene8()

            else:
                notstab = """Tybalt stand his ground.\n
Romeo settles down.\n
Tybalt: Mercutio was slain right!\n
Then Romeo stabs him through the heart!\n
Benvolio tells Romeo to run away at once.\n
People around the fight get the Prince.\n
The Prince enters.\n
The Prince: Benvolio, tell me what happened. I see that Tybalt and Mercutio are slain.\n
Benvolio: Romeo slain Tybalt.\n
The Prince: Why?\n
Benvolio: Before Tybalt slain Mercutio.\n
The Prince: Then if Romeo slain Tybalt who slain Mercutio? Romeo shall be exiled!\n
When he is found again, he shall become dead.\n
"""
                print_slow(notstab)

                loading = """
loading next scene\n
||||||||||||||||||||||||||||||||||||||||||||||\n"""
                print_slow(loading)
                sleep(3)
                scene8()
        else:
            nointervene = """Romeo watches Tybalt and Mercutio fight.\n
Tybalt stabs Mercutio!\n
Mercutio: I've been slain! I've been slain!\n
Romeo! why didn't you help me!
Romeo: I didn't mean for him to kill you!\n
Mercutio: A plague o' both your houses!\n
Benvolio brings Mercutio inside to one of the nearby houses.\n
Benvolio comes back out to Romeo and Tybalt.
Benvolio: He's dead!\n
Romeo: Tybalt! YOU DID THIS!\n
Romeo runs after Tybalt drawing Mercutio's sword.\n
"""
            print_slow(nointervene)
            kill = input("Should Romeo kill Tybalt? y or n: ")
            if kill == "y":
                stab = """Tybalt stands his ground.\n
But Romeo stabs him through the heart!\n
Benvolio tells Romeo to run away at once.\n
People around the fight get the Prince.\n
The Prince enters.\n
The Prince: Benvolio, tell me what happened? I see that Tybalt and Mercutio are slain.\n
Benvolio: Romeo slain Tybalt.\n
The Prince: Why?\n
Benvolio: Before Tybalt slain Mercutio.\n
The Prince: Then if Romeo slain Tybalt who slain Mercutio? Romeo shall be exiled!\n
When he is found again, he shall become dead.\n
"""
                print_slow(stab)

                loading = """
loading next scene\n
||||||||||||||||||||||||||||||||||||||||||||||\n"""
                print_slow(loading)
                sleep(3)
                scene8()

            else:
                notstab = """Tybalt stands his ground.\n
Romeo settles down.\n
Tybalt: Mercutio was slain right!\n
Then Romeo stabs him through the heart!\n
Benvolio tells Romeo to run away at once.\n
People around the fight get the Prince.\n
The Prince enters.\n
The Prince: Benvolio, tell me what happened? I see that Tybalt and Mercutio are slain.\n
Benvolio: Romeo slain Tybalt.\n
The Prince: Why?\n
Benvolio: Before Tybalt slain Mercutio.\n
The Prince: Then if Romeo slain Tybalt who slain Mercutio? Romeo shall be exiled!\n
When he is found again, he shall become dead.\n
"""
                print_slow(notstab)

                loading = """
loading next scene\n
||||||||||||||||||||||||||||||||||||||||||||||\n"""
                print_slow(loading)
                sleep(3)
                scene8()
