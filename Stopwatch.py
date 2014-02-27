# template for "Stopwatch: The Game"
import simplegui

# define global variable
interval = 100
clock = 0
position = [100, 100]

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
#def format(t):
#    t = 
#    pass
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def timer_start():
    timer.start()

def timer_stop():
    timer.stop()

def reset():
    global clock
    timer.stop()
    clock = 0

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global clock
    clock = clock + 1
    return clock

# define draw handler
def draw(canvas):
    canvas.draw_text(str(clock), position, 46, "red")
    
# create frame
frame = simplegui.create_frame("Stopwatch", 200, 200)
button1 = frame.add_button("Start", timer_start, 50)
button2 = frame.add_button("Stop", timer_stop, 50)
button3 = frame.add_button("Reset", reset, 50)

# register event handlers


frame.set_draw_handler(draw)
timer = simplegui.create_timer(interval, timer_handler)

# start frame
frame.start()

# Please remember to review the grading rubric
