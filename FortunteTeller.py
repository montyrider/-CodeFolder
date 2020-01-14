#Montana
#fortuneteller

from time import sleep
fortune=[]

print ("Welcome I am Montgomerey the Magnificent!")
sleep(2)
print ("Your wise and powerful Fortune teller!")
sleep(2)

print ("But first I need to know some details from you, to spark my powers!")
name = input("What is you name?")
fortune.append(name)

q1 = input ("Type y if you like dogs and n if you don't:")
if q1 == "n" or q1 == "N" or q1 == " n" or q1 == " N":
    fortune.append("You should avoid dogs in your life")
elif q1 == "y" or q1 == "Y" or q1 == " Y" or q1 == " y":
    fortune.append("A furry friend will come into your life")
    
    
q2 = input ("Type n if you don't like SuperHeros and y if you do:")
if q2 == "y" or q2 == "Y" or q2 == " y" or q2 == " Y":
    fortune.append("May you become a Hero to others!")
elif q2 == "n" or q2 == "N" or q2 == " n" or q2 == " N":
    fortune.append("You are not saved by others but yourself!")
    

q3 = input ("Type b if you like cake and c if you like cookies:")
if q3 == "c" or q3 == " c" or q3 == "C" or q3 == " C":
    fortune.append("You will bake a many cookies in your life")
elif q3 == "b" or q3 == "B" or q3 == " c" or q3 == " C":
    fortune.append("You will celebrate many birthdays")
    
    
q4 = input ("type t if you like TV shows or m if you like Movies more:")
if q4 == "t" or q4 == "T" or q4 == " t" or q4 == " T":
    fortune.append("your favorite show will never end")
elif q4 == "m" or q4 == "M" or q4 == " m" or q4 == " M":
    fortune.append("You will spend many a day watching your favorite Movies")
    
    
q5 = input ("Type m if you like Marvel or D if you like DC")
if q5 == "m" or q5 == "M" or q5 == " m" or q5 == " M":
    fortune.append("Marvel will make movies as long as you live")
elif q5 == "d" or q5 == "D" or q5 == " d" or q5 == " D":
    fourtune.append("Dc will make movies as long as you live")
 
  
print (fortune[0] + ",",fortune[1] + ",",fortune[2] + fortune[3] + ",",fortune[4] + ",",fortune[5])    