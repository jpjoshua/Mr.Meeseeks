from time import *
import pygame
import random
import sys

""" Data """
pygame.mixer.init()


""" Functions """
def prg_start():
    print("******* Mr.Meekseeks Study Buddy ******")
    choice = input("Do you need instruction on how to use a Meeseeks Box? ")
    if (choice.lower() == "yes"):
        print("Let me help you get started here with some simple instructions -Rick")
        play_file("ricks_meeseeks_instructions")
    else:
        play_file("im_mr_meeseeks")

def play_file(filename):
    pygame.mixer.music.load("C:/Users/Joshua/PycharmProjects/Mr.Meeseeks/%s.mp3" %(filename))
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

def main_menu():
    print("Please enter a number to start:")
    print("Main Menu")
    print("1) Study")
    print("2) Take a break")
    print("3) Quiz Me")
    print("4) Play get Schwifty!")
    print("5) Say a Rick Catch Phrase")
    print("6) Exit")

    choice = input("Choice: ")
    if (choice == "1"):
        print("\nA good study habit is in bursts of 30 minutes to 2 hours.")
        print("Please choose 30 minutes, 60 minutes, 90 minutes, or 120 minutes.")
        study()

    elif (choice == "2"):
        play_file("meeseeks_yes_sirie")
        takeBreak("menu")

    elif (choice == "3"):
        play_file("meeseeks_yes_sirie")
        quiz()

    elif (choice == "4"):
        play_file("meeseeks_yes_sirie")
        playGetSchwifty()

    elif (choice == "5"):
        #use the oh boy can do audio here
        play_file("meeseeks_yes_sirie")
        rickCatchPhrases()

    elif(choice == "6"):
        play_file("meeseeks_all_done")
        play_file("poof")
        print("\nThanks for using The Meeseeks Box. \nThe program has ended.")
        sys.exit(0)

    else: print("Choose a valid option."), main_menu()

def study():
    session = 4
    time = input("\nHow long will study(only enter 30, 60, 90, or 120)? ")
    if (time == "30" or time == "60" or time == "90" or time == "120" or time == "test"):
        answer = input("Are you sure? yes or no: ")

        if (answer.lower() == "yes" or answer.lower() == "ys" or answer.lower() == "y"):
            if (time == "30"):
                time = 1800
            elif (time == "60"):
                time = 3600
            elif (time == "90"):
                time = 5400
            elif (time == "120"):
                time = 7200
            elif (time == "test"):
                time = 5
        else:
            print("Please enter a valid answer.")
            study()
    else:
        print("Please enter one of the 4 listed times!")
        study()

    i = time

#Initial study session
    print("Study Session 1 has started.")
    sleep(1)
    while i > -1:
        print(i)
        i -= 1
        sleep(1)
    i = time #set i equal back time
    takeBreak("study")
    print("\n")

# Study Session 2
    print("Study Session 2 has started.")
    i = round(i * .75)
    sleep(1)
    while i > -1:
        print(i)
        i -= 1
        sleep(1)
    i = time  # set i equal back time
    takeBreak("study")
    print("\n")

#Study Session 3
    print("Study Session 3 has started.")
    i = round(i * .5)
    sleep(1)
    while i > -1:
        print(i)
        i -= 1
        sleep(1)
    i = time  # set i equal back time
    takeBreak("study")
    print("\n")

#Last Study Session
    print("Your last Study Session has started!")
    i = round(i * .25)
    sleep(1)
    while i > -1:
        print(i)
        i -= 1
        sleep(1)
    print("Study Time is over!!!")
    print("\n")

    play_file("meeseeks_all_done")
    main_menu() #Show main menu

def takeBreak(calltype):
    if (calltype == "study"):
        print("\nYour break will begin in 5 seconds!!!")
        i = 5
        while i > -1:
            print(i)
            i -= 1
            sleep(1)
        print("\nYou have a 20 minute break")
        i = 5
        while i > -1:
            print(i)
            i -= 1
            sleep(1)

    if (calltype == "menu"):
        time = input("How long do you want to take a break? ")
        i = int(time) * 60
        while i > -1:
            print(i)
            i -= 1
            sleep(1)
    print("\n")
    play_file("meeseeks_all_done")
    main_menu() #Show main menu

def quiz():
    print("\nLet's Get Quizzing!")
    print("First enter you questions and answers.")
    print("Then when its quizzing time, type 'Y' and press enter \nto reveal the answer when you're ready to see it\n")
    q = int(input("How many questions do you have?: "))
    if (q == 0):
        print("\n")
        main_menu()
    user = input("Continue? (yes or no): ")
    if (user.lower() == "yes"):
        i = 0
        j = 0
        questions = []
        answers =[]

        """Loop for entering in questions and answers"""
        print("\nType your questions and answers and hit enter to continue!")
        while i < q:
            response1 = input("\nQuestion #%d: \n" %(i))
            questions.append(response1)
            i += 1

            response2 = input("Answer #%d: \n" %(j))
            answers.append(response2)
            j += 1
        """ Quizzing time"""
        print("\nLet the Quiz begin!!!")
        k = 0
        index = 0
        while k < q:
            print("Question #%d" % (k))
            k += 1
            print(questions[index])
            reveal = input("Press y and hit enter to reveal answer: ")
            while reveal.lower() != "y":
                print("Not a valid input!")
                reveal = input("Press y and hit enter to reveal answer: ")
            print(answers[index])
            index += 1
        print("\n")
        play_file("meeseeks_all_done")
        main_menu()

    else:
        print("\n")
        main_menu() # return to main menu

def playGetSchwifty():
    # pygame.init() # this is what breaks it...
    print("\nNow Playing Get Schwifty!")
    play_file("Get_Schwifty")
    print("\n")
    main_menu()#Show main menu

def rickCatchPhrases():
    catchphrase = ["aids","burger_time","grass_taste_bad","hit_the_sack_jack","lick_my_balls",
                   "no_jumping_in_the_sewer","rikki_tikki_tavi_bitch","rubber_baby_beddy_bunkers",
                   "shum_shum_shlipidy_dop","summer_sault_jump","thats_the_way_the_news_goes",
                   "wubba_lubba_dub_dub"]
    rchoice = input("\nDo you want to pick a catchphrase (yes or no): ")
    if (rchoice.lower() == "yes"):
        print("\nPlease choose a number below.")
        print("""
         1) Aids!
         2) Burgertime!
         3) Grass...Tastes bad
         4) Hit the sack jack 
         5) Lick my balls
         6) No jumping in sewers
         7) Rikki tikki tavi bitch
         8) Rubber baby beddy bunker
         9) Shum shum shlipidy dop
        10) Summer sault jump
        11) And thats the way the new goes
        12) Wubba lubba dub dub""")

        choice = input("Please enter the number of the catchphrase you want to play:  ")
        if (choice == "1"): filename = "aids"
        elif (choice == "2"): filename = "burger_time"
        elif (choice == "3"): filename = "grass_taste_bad"
        elif (choice == "4"): filename = "hit_the_sack_jack"
        elif (choice == "5"): filename = "lick_my_balls"
        elif (choice == "6"): filename = "no_jumping_in_the_summer"
        elif (choice == "7"): filename = "rikki_tikki_tavi_bitch"
        elif (choice == "8"): filename = "rubber_baby_beddy_bunkers"
        elif (choice == "9"): filename = "shum_shum_shlipidy_dop"
        elif (choice == "10"): filename = "summer_sault_jump"
        elif (choice == "11"): filename = "thats_the_way_the_news_goes"
        elif (choice == "12"): filename = "wubba_lubba_dub_dub"
        else:
            print("Invalid option, playing a random catchphrase")
            filename = random.choice(catchphrase)

        print("\nNow Playing One of Rick's Catchphrases!")
        play_file(filename)

    else:
        print("Now playing a random Rick Catchphrase")
        filename = random.choice(catchphrase)
        play_file(filename)

    print("\n")
    main_menu() #Show main menu

def sassLevel(level):
    if (level == 1):
        pass
    if (level == 2):
        pass
    if (level == 3):
        pass
    if (level == 4):
        pass
    if (level == 5):
        pass

""" Program Starts Here """
prg_start()
main_menu()




""" PROGRAMER NOTES """
"""
--> use vlc for audio stuff
--> Sample HTML code
html_file = open('Meeseeks.html','w')
 a = ['f','d','s','a']
 x = -1
 scope = vars()
 data = ''
 for i in a: #TIP: use a generator
     scope['x']+=1
     data += a[x]
     data += '\n'
 html_file.write(data)
 html_file.close()"""
