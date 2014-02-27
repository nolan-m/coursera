# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import random
import simplegui

# initialize global variables used in your code
secret_num = 0
remaining = 0
maxrange = 100

# helper function to start and restart the game
def new_game():
    global maxrange
    global remaining
    if maxrange == 100:
        remaining = 7
    if maxrange == 1000:
        remaining = 10
    global secret_num
    secret_num = random.randrange(0, maxrange)
    print "Guess a number between 0 and ", maxrange

# define event handlers for control panel
def range100():
    # button that changes range to range [0,100) and restarts
    global maxrange
    maxrange = 100
    new_game()

def range1000():
    # button that changes range to range [0,1000) and restarts
    global maxrange
    maxrange = 1000
    new_game()   
    
def input_guess(guess):
    global remaining
    if remaining > 0:
        print "Your guess: ", guess
    # main game logic goes here	
        if guess == "":
            print "Please enter value."
        else:
            if int(guess) < maxrange:
                if int(guess) > secret_num:
                    print "Your guess is too high.  Guess lower.\n"
                    remaining = remaining - 1
                    print "Remaining Guesses: ", remaining
                elif int(guess) < secret_num:
                    print "Your guess is too low.  Guess higher. \n"
                    remaining = remaining- 1
                    print "Remaining Guesses: ", remaining, "\n"
                else:
                    print "Guess is correct! \n"
                    new_game()
            else:
                print "Guess is out of range. \n"
    if remaining == 0: 
        print "Out of Guesses.  Correct Number was: ", secret_num
        print
        new_game()
    
# create frame
frame = simplegui.create_frame('Guess a Number!', 200, 200)


# register event handlers for control elements
button1 = frame.add_button('New Game', new_game, 100)
button2 = frame.add_button('Range 0-100', range100, 100)
button3 = frame.add_button('Range 0-1000', range1000, 100)

inp = frame.add_input('Guess a Number:', input_guess, 100)

# call new_game and start frame
new_game()
frame.start()

# always remember to check your completed program against the grading rubric
