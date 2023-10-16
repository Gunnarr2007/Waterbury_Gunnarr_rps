# This File was made by Gunnarr Waterbury

'''
Goals:
When a user click on their choice, the computer randomly chooses and displays the result 

'''

# import turtle so that you can have a frame/ graphics for our game. we import randit so that we can randomize the choices.
import turtle
from turtle import *
from random import randint
# The os module allows us to access the current directory in order to access assets
import os
print("The current working directory is (getcwd): " + os.getcwd())
print("The current working directory is (path.dirname): " + os.path.dirname(__file__))

# setup the game folders using the os module
game_folder = os.path.dirname(__file__)
images_folder = os.path.join(game_folder, 'images')

# setup the dementations of window
WIDTH, HEIGHT = 1000, 400

rock_w, rock_h = 256, 280

paper_w, paper_h = 256, 204

scissors_w, scissors_h = 256, 170

# setup the screen and turyle screen equal to each other
screen = turtle.Screen()
screen.setup(WIDTH + 4, HEIGHT + 8)  # fudge factors due to window borders & title bar
screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)
screen.screensize(canvwidth=WIDTH, canvheight=HEIGHT, bg="lightblue")


# canvas object
cv = screen.getcanvas()
# make it so the window is not resizeable 
cv._rootwindow.resizable(False, False)


# get the rock image from the file images 
rock_image = os.path.join(images_folder, 'rock.gif')
# create an instance for rock with turtle
rock_instance = turtle.Turtle()
# get paper from images file
paper_image = os.path.join(images_folder, 'paper.gif')
# instantiate (create an instance of) the Turtle class for the paper
paper_instance = turtle.Turtle()
# sget scissors file from images 
scissors_image = os.path.join(images_folder, 'scissors.gif')
# instantiate (create an instance of) the Turtle class for the scissors
scissors_instance = turtle.Turtle()

XMark_image = os.path.join(images_folder, 'XMark.gif')
XMark_instance = turtle.Turtle()

CheckMark_image = os.path.join(images_folder, 'CheckMark.gif')
CheckMark_instance = turtle.Turtle()

def show_rock(x,y):
    # add the rock image as a shape
    screen.addshape(rock_image)
    # attach the rock_image to the rock_instance
    rock_instance.shape(rock_image)
    # remove the pen option from the rock_instance so it doesn't draw lines when moved
    rock_instance.penup()
    # set the position of the rock_instance
    rock_instance.setpos(x,y)

def show_paper(x,y):
    # add the paper image as a shape
    screen.addshape(paper_image)
    # attach the paper_image to the paper_instance
    paper_instance.shape(paper_image)
    # remove the pen option from the paper_instance so it doesn't draw lines when moved
    paper_instance.penup()
    # set the position of the paper_instance
    paper_instance.setpos(x,y)

def show_scissors(x,y):
    # add the scissors image as a shape
    screen.addshape(scissors_image)
    # attach the scissors_image to the scissors_instance
    scissors_instance.shape(scissors_image)
    # remove the pen option from the scissors_instance so it doesn't draw lines when moved
    scissors_instance.penup()
    # set the position of the scissors_instance
    scissors_instance.setpos(x,y)
def ShowXMark(x,y):
    # add the rock image as a shape
    screen.addshape(XMark_image)
    # attach the rock_image to the rock_instance
    XMark_instance.shape(XMark_image)
    # remove the pen option from the rock_instance so it doesn't draw lines when moved
    XMark_instance.penup()
    # set the position of the rock_instance
    XMark_instance.setpos(x,y)
# instantiate a turtle for writing text
def ShowCheckMark(x,y):
    # add the rock image as a shape
    screen.addshape(CheckMark_image)
    # attach the rock_image to the rock_instance
    CheckMark_instance.shape(CheckMark_image)
    # remove the pen option from the rock_instance so it doesn't draw lines when moved
    CheckMark_instance.penup()
    # set the position of the rock_instance
    CheckMark_instance.setpos(x,y)
# instantiate a turtle for writing text
text = turtle.Turtle()
text.color('deep pink')
text.hideturtle()
text.penup() 

show_rock(-300, 0)
show_paper(0, 0)
show_scissors(300, 0)

# this function uses and x y value, an obj, and width and height 
def collide(x,y,obj,w,h):
    if x < obj.pos()[0] + w/2 and x > obj.pos()[0] - w/2 and y < obj.pos()[1] + h/2 and y > obj.pos()[1] - h/2:
        return True
    else:
        return False

# function that passes through wn onlick

# def computer_choice():
#     choice = randint(0,2)
#     if choice == 0:
#         show_rock(300,)

# The code to chose gives us the specific options to what will happen and you can also see that we are stting the position of where the text will do usinf text.goto and thne the values we want 
def mouse_pos(x, y):
    rps_choices=["rock","paper","scissors"]
    computer = rps_choices[randint(0,2)]
    if collide(x,y,rock_instance, rock_w, rock_h):
        print("rock")
        text.clear()
        text.goto(-150,150)
        text.write("you chose rock!!!", False, "left", ("Arial", 24, "normal"))
        if computer == "scissors":
            text.goto(-270,100)
            text.write("computer choose " +computer, False, "left", ("Arial", 24, "normal"))
            text.goto(130,100)
            text.write("you win",False, "left", ("Arial", 24, "normal"))
            ShowCheckMark(300,100)
        elif computer =="paper":
            text.goto(-250,100)
            text.write("computer choose " +computer,False, "left", ("Arial", 24, "normal"))
            text.goto(100,100)
            text.write("you lose",False, "left", ("Arial", 24, "normal")) 
            ShowXMark(300,100)
        else:
            text.goto(-250,100)
            text.write("computer choose " +computer, False, "left", ("Arial", 24, "normal"))
            text.goto(100,100)
            text.write("tie",False, "left", ("Arial", 24, "normal"))
        
    
            #use this code for others (note to self)
      
    
# We do the same thing over again but instead of doing it for rock we do it for paper and set the tect to be over the paper option and make sure that the text will not collide with the image 
    elif collide(x,y,paper_instance, paper_w, paper_h):
        print("paper")
        text.clear()
        text.goto(-150,150)
        text.write("you chose scissors!!!", False, "left", ("Arial", 24, "normal"))
        if computer == "scissors":
            text.goto(-270,100)
            text.write("computer choose " +computer, False, "left", ("Arial", 24, "normal"))
            text.goto(130,100)
            text.write("you win",False, "left", ("Arial", 24, "normal"))
            ShowCheckMark(300,100)
        elif computer =="paper":
            text.goto(-250,100)
            text.write("computer choose " +computer,False, "left", ("Arial", 24, "normal"))
            text.goto(100,100)
            text.write("you lose",False, "left", ("Arial", 24, "normal")) 
            ShowXMark(300,100)
        elif computer == "rock":
            text.goto(-250,100)
            text.write("computer choose " +computer, False, "left", ("Arial", 24, "normal"))
            text.goto(100,100)
            text.write("tie",False, "left", ("Arial", 24, "normal"))
        else:
            print("you chose nothing!!")
    
# Lastly we do the same thing over but for text that will give us the options for scissors we set the text and befine what we want the text to say and the options for winning and losing 
    elif collide(x,y,scissors_instance, scissors_w, scissors_h):
        print("scissors")
        text.clear()
        text.goto(-150,150)
        text.write("you chose scissors!!!", False, "left", ("Arial", 24, "normal"))
        if computer == "scissors":
            text.goto(-270,100)
            text.write("computer choose " +computer, False, "left", ("Arial", 24, "normal"))
            text.goto(130,100)
            text.write("you win",False, "left", ("Arial", 24, "normal"))
            ShowCheckMark(300,100)
        elif computer =="paper":
            text.goto(-250,100)
            text.write("computer choose " +computer,False, "left", ("Arial", 24, "normal"))
            text.goto(100,100)
            text.write("you lose",False, "left", ("Arial", 24, "normal")) 
            ShowXMark(300,100)
        elif computer == "rock":
            text.goto(-250,100)
            text.write("computer choose " +computer, False, "left", ("Arial", 24, "normal"))
            text.goto(100,100)
            text.write("tie",False, "left", ("Arial", 24, "normal"))
        else:
            print("you chose nothing!!")

# The first text that shows up to tell you your options and is set to the middle of the screen
text.setpos(-200,150)
text.write("Choose rock or paper or scissors", False, "left", ("Arial", 24, "normal"))

#lets us click it with the mouse
screen.onclick(mouse_pos)
# runs a loop for turtle to run
screen.mainloop()


# defining the choice that yo u can make for rock paper scissors
rps_choices=["rock","paper","scissors"]
def rps():
    #creates variable InfinateRounds = 1 makes while loop so goes on forever while Infinate roands varible is greater than 0
    InfinateRounds =1
    
    while InfinateRounds > 0:
        #player choice is equal to rock, paper or scissors
        player_choice=input("choose rock, paper or scissors, you have infinate rounds ")
        #computer has choices of rock paper or scissors which is randomized by randint
        computer = rps_choices[randint(0,2)]
    
        
        #If player_choice == rock & computer == scissors than player wins
        if player_choice=="rock" :
            if computer == "scissors":
             text.goto(150,0)
             print("computer choose "+computer )
             text.goto(150,0)
             print("you win",False, "left", ("Arial", 24, "normal")) 
        #If player_choice == scissors & computer == paper than player wins & prints what computer choose
        if player_choice=="scissors" :
            if computer == "paper":
             text.goto(150,0)
             print("computer choose "+computer )
             text.goto(150,0)
             print("you win",False, "left", ("Arial", 24, "normal"))  
        #If player_choice == paper & computer == rock than player wins & prints what computer choose
        if player_choice=="paper" :
            if computer == "rock":
             text.goto(150,0)
             print("computer choose "+computer,False, "left", ("Arial", 24, "normal"))
             text.goto(150,0)
             print("you win",False, "left", ("Arial", 24, "normal")) 
        #if player choice is equal to computer than it is a tie + prints what computer choose
        elif player_choice == computer:
            text.goto(150,0)
            print("computer choose "+computer,False, "left", ("Arial", 24, "normal"))
            text.goto(150,0)
            print("tie",False, "left", ("Arial", 24, "normal"))
        #if player chooses rock & computer chooses paper, player lose & prints what computer choose
        elif player_choice == "rock":
             if computer =="paper":
                text.goto(150,150)
                print("computer choose "+computer,False, "left", ("Arial", 24, "normal"))
                text.goto(150,150)
                print("you lose",False, "left", ("Arial", 24, "normal"))    
        #if player chooses rock & computer chooses paper, player lose & prints what computer choose
        elif player_choice == "scissors":
             if computer=="rock":
                text.goto(150,150)
                print("computer choose "+computer,False, "left", ("Arial", 24, "normal"))
                text.goto(150,150)
                print("you lose",False, "left", ("Arial", 24, "normal"))
        #if player chooses rock & computer chooses paper, player lose & prints what computer choose   
        elif player_choice == "paper":
             if computer =="scissors":
                text.goto(150,150)
                print("computer choose "+computer,False, "left", ("Arial", 24, "normal"))
                text.goto(150,150)
                print("you lose",False, "left", ("Arial", 24, "normal"))   
#runs func

rps_choices=["rock","paper","scissors"]
def rps():
    #creates variable InfinateRounds = 1 makes while loop so goes on forever while Infinate roands varible is greater than 0
    InfinateRounds =1
    
    while InfinateRounds > 0:
        #player choice is equal to rock, paper or scissors
        player_choice=input("choose rock, paper or scissors, you have infinate rounds ")
        #computer has choices of rock paper or scissors which is randomized by randint
        computer = rps_choices[randint(0,2)]
    
        
        #If player_choice == rock & computer == scissors than player wins
        if player_choice=="rock" :
            if computer == "scissors":
             text.goto(150,150)
             print("computer choose "+computer ,False, "left", ("Arial", 24, "normal"))
             text.goto(150,150)
             print("you win",False, "left", ("Arial", 24, "normal"))
             text.goto(150,150)
        #If player_choice == scissors & computer == paper than player wins & prints what computer choose
        if player_choice=="scissors" :
            if computer == "paper":
             text.goto(150,150)
             print("computer choose "+computer ,False, "left", ("Arial", 24, "normal"))
             text.goto(150,150)
             print("you win",False, "left", ("Arial", 24, "normal"))   
        #If player_choice == paper & computer == rock than player wins & prints what computer choose
        if player_choice=="paper" :
            if computer == "rock":
             text.goto(150,150)
             print("computer choose "+computer ,False, "left", ("Arial", 24, "normal"))
             text.goto(150,150)
             print("you win",False, "left", ("Arial", 24, "normal"))
        #if player choice is equal to computer than it is a tie + prints what computer choose
        elif player_choice == computer:
            text.goto(150,150)
            print("computer choose "+computer,False, "left", ("Arial", 24, "normal"))
            text.goto(150,150)
            print("tie",False, "left", ("Arial", 24, "normal"))
        #if player chooses rock & computer chooses paper, player lose & prints what computer choose
        elif player_choice == "rock":
             if computer =="paper":
                text.goto(200,100)
                print("computer choose "+computer,False, "left", ("Arial", 24, "normal"))
                text.goto(150,150)
                print("you lose",False, "left", ("Arial", 24, "normal"))    
        #if player chooses rock & computer chooses paper, player lose & prints what computer choose
        elif player_choice == "scissors":
             if computer=="rock":
                text.goto(150,150)
                print("computer choose "+computer,False, "left", ("Arial", 24, "normal"))
                text.goto(150,150)
                print("you lose",False, "left", ("Arial", 24, "normal"))
        #if player chooses rock & computer chooses paper, player lose & prints what computer choose   
        elif player_choice == "paper":
             if computer =="scissors":
                text.goto(150,150)
                print("computer choose "+computer,False, "left", ("Arial", 24, "normal"))
                text.goto(150,150)
                print("you lose",False, "left", ("Arial", 24, "normal"))
#runs func


# first you import randint from random so that the computer has a random choice
from random import randint

 
#second you defend what the choices are for rock paper scissors
rpc_choices = ("rock", "paper", "scissors")

 
# then a scoring system so that you can follow along with who wins and keeps count
def score_eval(a, b):

   

    checker = a > b

   

    if checker:

        return True

    else:

        return False

 
# then you start to code the core of the game
def rock_paper_scissors(x):
# first you ask the player what you want to choice
    while x > 0:

        CPU_choice = rpc_choices[randint(0, 2)]

        player = input("What is your choice?")

    

        global player_score

        player_score = 0

        global CPU_score

        CPU_score = 0
# make a code that will idiot proof it if someone tries to choice a choice that is not in rps_choices 
        if player not in rpc_choices:
            print ("THAT IS NOT A CHOICE!!!!!!")
            break
# tell in the termal what each player have choicen 
        print("The player chose " + player)

        print("The computer chose " + CPU_choice)

#  then you code the possiblilities of what will happen with all the choices 
# first one that we code is a tie u ask the computer to check if the player and computer have choicen the same choice and if so print a tie
        if player == CPU_choice:

            print("The round was a tie.")

#  this section of code is the possible outcomes of the game with rock beeating scissors, scissors beating paper and paper beats rock

        if player == "rock":

            x -= 1

            if CPU_choice == "paper":

                print("The computer has won.")

                CPU_score += 1

            elif CPU_choice == "scissors":

                print("The player has won.")

                player_score += 1

       

        if player == "scissors":

            x -= 1

            if CPU_choice == "rock":

                print("The computer has won.")

                CPU_score += 1

            elif CPU_choice == "paper":

                print("The player has won.")

                player_score += 1

       

        if player == "paper":

            x -= 1

            if CPU_choice == "scissors":

                print("The computer has won.")

                CPU_score += 1

            elif CPU_choice == "rock":

                print("The player has won.")

                player_score += 1

   
# this will alway the player to view the score of their rounds and it will also count for them if they won or not  
    if x == 0 and player_score:

        print("The player's score was " + str(player_score))

        print("The computer's score was " + str(CPU_score))
