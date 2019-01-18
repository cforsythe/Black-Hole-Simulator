import os
import time
import random
import sys
#Start of game welcome
os.system("mode con: cols=80 lines=100")






def main():


    print"  ___       __   _______   ___       ________  ________  _____ ______   _______ "      
    time.sleep(.1)
    print" |\  \     |\  \|\  ___ \ |\  \     |\   ____\|\   __  \|\   _ \  _   \|\  ___ \ "    
    time.sleep(.1)
    print" \ \  \    \ \  \ \   __/|\ \  \    \ \  \___|\ \  \|\  \ \  \\\__\ \  \ \   __/| "   
    time.sleep(.1)
    print"  \ \  \  __\ \  \ \  \_|/_\ \  \    \ \  \    \ \  \\\  \ \  \\|__| \  \ \  \_|/__ " 
    time.sleep(.1)
    print"   \ \  \|\__\_\  \ \  \_|\ \ \  \____\ \  \____\ \  \\\  \ \  \    \ \  \ \  \_|\ \ "
    time.sleep(.1)
    print"    \ \____________\ \_______\ \_______\ \_______\ \_______\ \__\    \ \__\ \_______\ "
    time.sleep(.1)
    print"     \|____________|\|_______|\|_______|\|_______|\|_______|\|__|     \|__|\|_______| "
    time.sleep(.1)                                                                               
                                                                                    
                                                                                    
    print"  _________  ________             "                                                               
    time.sleep(.1)
    print" |\___   ___\\   __  \            "                                                              
    time.sleep(.1)
    print" \|___ \  \_\ \  \|\  \           "                                                             
    time.sleep(.1)
    print"      \ \  \ \ \  \\\  \          "                                                            
    time.sleep(.1)
    print"       \ \  \ \ \  \\\  \         "                                                            
    time.sleep(.1)
    print"        \ \__\ \ \_______\        "                                                           
    time.sleep(.1)
    print"         \|__|  \|_______|        "                                                           
    time.sleep(.1)                                                                                    
                                                                                    
                                                                                    
    print" ________  ________  ________  ________  _______"                                    
    time.sleep(.1)
    print"|\   ____\|\   __  \|\   __  \|\   ____\|\  ___ \ "                                   
    time.sleep(.1)
    print"\ \  \___|\ \  \|\  \ \  \|\  \ \  \___|\ \   __/| "                                 
    time.sleep(.1)
    print" \ \_____  \ \   ____\ \   __  \ \  \    \ \  \_|/__ "                               
    time.sleep(.1)
    print"  \|____|\  \ \  \___|\ \  \ \  \ \  \____\ \  \_|\ \ "                              
    time.sleep(.1)
    print"    ____\_\  \ \__\    \ \__\ \__\ \_______\ \_______\ "                             
    time.sleep(.1)
    print"   |\_________\|__|     \|__|\|__|\|_______|\|_______|  "                            
    time.sleep(.1)
    print"   \|_________|"     
    time.sleep(.1)

    print "Would you like to explore?"
    print "----------------------------------------------"
    time.sleep(1)
    start = raw_input("Choose 'Yes' or 'No': \n").lower()
    if start == 'yes':
        print "Be careful it's DANGEROUS to go alone, Would you like to continue?"
        print "------------------------------------------------------------------"
        yes()
    elif start == 'no': 
        print "You must be careful making your way back home, space is not a safe place\n"
    else:
        print "Try Yes or No?\n"
        main()

#if answer is yes 
def yes():
    answer = raw_input("'Yes' or 'No'\n").lower()
    if answer == 'yes':
        print "Where would you like to go?"
        print "---------------------------"
        stupid()
    elif answer == 'no':
        print "Then why would you go to space in the first place?!?!?SMH....\n"
    else:
        print "Try Yes or No"
        yes()

#choosing a location to travel to
def stupid():
    loc = raw_input("Type any location\n").lower()
    if loc == 'earth' or loc == 'mars' or loc == 'mercury' or loc == 'venus' or loc == 'jupiter' or loc == 'saturn' or loc == 'neptune' or loc == 'uranus' or loc == 'pluto':
        print "Come on you can go anywhere you want and you choose a planet?!"
        print "Try something further?!"
        stupid()
    else:
        blackhole()

#Sucked into blackhole
def blackhole():
    print "************************************************************************"
    print "On the way there you found a blackhole and couldn't get away"
    print "------------------------------------------------------------------------"
    print "You haven't died yet so lets explore"
    escape()

#escape from blackhole
def escape():
    

    print "------------------------------------------------------------------------"
    print "You have 4 options"
    print "------------------------------------------------------------------------"
    print "1. Fly towards the entrance in hopes of escaping(chance of escaping)"      #45 percent chance of escaping
    print "------------------------------------------------------------------------"
    print "2. Accept your imminent defeat and eat cyanide(cyanide may not work)"      #35 percent chance cyanide doesn't work
    print "------------------------------------------------------------------------"
    print "3. Develop a device with your current resources"                           #List of possible devices to create
    print "------------------------------------------------------------------------"
    print "4. Attempt to continue further into the black whole(chance of dying)"      #75 percent chance of dying
    print "------------------------------------------------------------------------"
    print "Type the number that corresponds with what you'd like to do"
    escapeplan = raw_input("What would you like to do?\n")
    if escapeplan == "1":
        a = random.random()
        if a < .45:
            print "You Escaped!"
            print "------------"
            print "What would you like to do?"
            print "You can re-enter the blackhole and experiment"
            print "possibly changing science forever"
            print "or"
            print "find your way back to earth"
            print "------------------------------------------------------"
            escaped()
        else:
            print "You're in a black hole, there's no light in here silly"
            print "You  cant see your way out"
            print "Try again"
            escape()
    elif escapeplan == "2":
        a = random.random()
        if a < .35:
            print "You have died, this is the end of the line for you, but you chose this life"
            again()
        elif (a > .35) & (a < .60):
            print "You didn't die from the cyanide and will now(possibly) live the last days of your life in pain"
            print "However with proper research you can find the antidote of Cyanide and further continue your quest"
            def anti():
                ant = raw_input("Would you like to find the antidote?\n").lower()
                if ant == 'yes':
                    antidote()
                elif ant == 'no':
                    print "You will die a slow painful death"
                    print "There are no choices left, this is gameover.... you lose"
                elif ant == 'antidote':
                    print "The name of the antidote is Cyanokit or Nithiodote"
                    print "This is a guarantee"
                    print "You will live if you take the antidote... better hope you have it"
                    antidote()
                else:
                    print "There are three possible answers to this question.. 'Yes'...'No'.."
                    print "and the last one is a secret"
                    anti()
            anti()
        else:
            print "The Cyanide had no effect"
            print "Maybe trying something else would be a better course of action"
            escape()
    elif escapeplan == '3':
        print "Sooo... you want to be inovative!"
        time.sleep(1)
        print "I like the idea of that."
        time.sleep(1)
        print "However you have to figure out what to build"
        combine()

def combine():        
    print "--------------------------------------------"
    time.sleep(1)
    print "Here are some options"
    print "********************************************"
    print "1. A Bottle of Syrup"
    print "2. A Lighter"
    print "3. A Sat Phone"
    print "4. A Jetpack"
    print "5. A Samaurai Sword"
    print "6. Medicine(unknown)"
    options()

def options():
    choice = raw_input("Would you like to use 1 or 2 items?/n")
    if choice == '1':
        item = raw_input("Which item would you like to use?")
        if item == '1':
            print "Now what on earth are you going to do with a bottle of syrup?"
            time.sleep(2)
            print "I suppose you could drink it and extend your life"
            time.sleep(1)
            print "Or you could combine it with something else and get far more use of it"
            print "Which choice would you prefer?"
            print "------------------------------"
            print "1. Just drink it"
            print "2. Combine with an item"
            a = raw_input("Choose 1 or 2")
            if a == '1':
                print "All the possibilities you can choose and you go for drinking the syrup"
                time.sleep(2)
                print "Good for you, now that you've drank the syrup..."
                time.sleep(1)
                print "You can teleport anywhere you want with a simple thought"
                time.sleep(.5)
                print "The downside is that you can only do it once"
                time.sleep(1)
                print "Oh, and I lied..."
                time.sleep(2)
                print "You have two places you can teleport too"
                print "So dont mess up, otherwise your teleport will go to waste"
                time.sleep(2)
                print "1. Teleport to Earth"
                print "2. Teleport back to the entrance of the Black Hole"
                tp = raw_input("Hurry and choose 1 or 2")
               # if tp == '1':
        
def antidote():
    antidot = raw_input("What is the antidote called?\n").lower()
    
    if antidot == 'cyanokit' or antidote == 'nithiodote':
        a = random.random()
        print " Wow, you are pretty smart to figure this one out"
        print " However, there is a chance that you wont find it"
        print " Searching"
        print "---------------------------------------------------"
        if a < .50:
            print " You do not have the antidote"
            print " Sorry to say but you just have bad luck"
            print " GAMEOVER SUCKA"
            print "-----------------------------------------"
            again()
        else:
            print "The antidote was found, and it worked on you"
            print "You are one lucky person"
            print "However you are still stuck in a black hole"
            print "Here you go"
            escape()
    else:
        print "Sorry that is not the correct antidote"
        def retry():
            tryagain = raw_input("Would you like to try again?").lower()
            if tryagain == 'yes':
                antidote()
            elif tryagain == 'no':
                print "Okay, goodnight...............maybe next time"
                again()
            else:
                print " Try 'Yes or 'No'"
                retry()
        retry()
    antidote()
            
        
     
   
        
#escaping black hole            
def escaped():
    print "1. Re-enter Blackhole"
    print "---------------------"
    print "2. Return to Earth"
    print "---------------------"
    dec = raw_input("Choose an Option\n")
    if dec == '1':
        print "Back in we gooooooooooo"
        escape()
    elif dec == '2':
        earth()

def earth():
    a = random.random()

    if a < .25:
        print "On the way to earth, you were hit by an astroid and died"
        print "--------------------------------------------------------"
        print "Maybe next time"
        again()
    elif (a > .25) & (a < .75):
        print "For some reason the captain ran out of gas"
        print "you landed on Mars."
        mars()
    else:
        success()

def tp():
    a = random.random()
    if a > 50:
        success()
    else:
        print "Well you've made it back to earth now"
        print "However, upon teleporting the side-effects of this super syrup have become obvious"
        print "You are now a Griffin..."
        print "and also in the midst of WW2"
        print "Not only will this teleportation change history..."
        print "But you have to join a side"
        print "Who would you like to join?"
        print "1. Allied Powers(United States)"
        print "2. Axis Powers(Germany)"
        this = raw_input("1 or 2?")
        if this == '1':
            print "You win the war..."
            print "And the game."
            print "Good Game"
            again()
        elif this == '2':
            print "You help Germany win the war"
            time.sleep(1)
            print "You exterminate the holocaust in a covert OPs mission"
            time.sleep(2)
            print "You secretly were working for the United States the whole time"
            time.sleep(2)
            print "Not only do you rip Germany to shreds but you also save the German scientists"
            time.sleep(2)
            print "After saving the German scientists, you fly them to the United States"
            time.sleep(2)
            print "After taking the scientists to America, you are greeted by a group of hunters"
            time.sleep(2)
            print "The hunters capture you and lock you up in a zoo"
            time.sleep(2)
            print "You win the game..."
            time.sleep(2)
            print "But is it really considered winning if you're stuck in a zoo?"
            again()
        
    




def success():
    print "You made it back to Earth safe and sound"
    print "nobody believes that you actually survived a black hole."
    print "--------------------------------------------------------"
    print "This is GAMEOVER for you"
    again()
        
def mars():
    a = random.random()


    print "Would you like to attempt calling someone on earth?"
    print "Or live your last days on Mars?"
    print "1. Call"
    print "2. Die"
    dec = raw_input("Choose an option\n").lower()
    if dec == '1':
        if a < .50:
            print "The call made it home and support is on its way"
            print "However you will be exiting space so, this is game over"
            again()
        elif a > .50:
            print "Sorry to inform you but the call didn't reach back to Earth"
            print "-----------------------------------------------------------"
            print "You will spend your last days on Mars, and die a slow death"
            again()
    if dec == '2':
        print "You will spend your last days on Mars, and die a slow death"
        again()
        
    


def again():
    print "Would you like to play again?"
    dec = raw_input("Yes or no?\n").lower()
    if dec == 'yes':
        print "Restarting"
        print "---------------------------------------------"
        main()
    elif dec == 'no':
        sys.exit()
    else:
        again()
        









        

main()

