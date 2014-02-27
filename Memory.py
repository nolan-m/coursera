# implementation of card game - Memory

import simplegui
import random

deck = list(list(range(0,8)) + list(range(0,8)))
random.shuffle(deck)


WIDTH = 50
HEIGHT = 100

exposed = [False for i in range(16)]

index = 0
state = 0
card1 = 0
card2 = 0

turn = 0

# helper function to initialize globals
def new_game():
    global turn, exposed, state
    random.shuffle(deck)
    exposed = [False for i in range(16)]
    turn = 0
    state = 0
    label.set_text("Turns = " + str(turn))
    


     
# define event handlers
def mouseclick(pos):
    global index, state, card1, card2, turn
    
    index = pos[0] // 50
    
    label.set_text("Turns = " + str(turn))
    
    if exposed[index] == True:
        pass
    else:
        exposed[index] = True
        
        if state == 0:
            card1 = index
            state = 1

        elif state == 1:
            card2 = index
            state = 2
            turn += 1
            
        elif state == 2:
            if deck[card1] != deck[card2]:
                exposed[card1] = False
                exposed[card2] = False
            card1 = index
            state = 1

                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    for index in range(len(deck)):
        if exposed[index] == True:
            canvas.draw_text(str(deck[index]),[WIDTH* index + 10, HEIGHT-25],60,"Orange")
        else:
            canvas.draw_polygon([(WIDTH*index,0), (WIDTH*(index+1), 0), (WIDTH*(index+1), 100),(WIDTH*index,100)],3,"Black","Orange")

        
        
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.set_canvas_background('Grey')
frame.add_button("Restart", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric