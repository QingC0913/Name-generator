#imports the ability to get a random number (we will learn more about this later!)
from random import *

#Create the list of words you want to choose from.
name = ["Qing", "Yairy", "Riddhimaa", "Shreya", "Nia", "Rima", "Sree", "Olivia", "Angeline"]


#Generates a random integer.
aRandomIndex = randint(0, len(name)-1)

answer = input("If you want a random girl's name, type ok.")
if answer == "ok":
    print ("Your random name is", name[aRandomIndex])
