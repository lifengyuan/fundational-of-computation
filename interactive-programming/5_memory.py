# implementation of card game - Memory
 
import simplegui
import random
 
state = 0
turn = 0
number = []
exposed = []
 
 
# helper function to initialize globals
def new_game():
    global turn, number, exposed, state
    turn = 0
    state = 0
    number = range(0, 8)
    numberOther = range(0, 8)
    number.extend(numberOther)  
    random.shuffle(number)
    exposed = [False for i in range(16)]
 
     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global state, turn, index1, index2
    index = pos[0] // 50
    if exposed[index] == False:
        if state == 0:
            exposed[index] = True
            state = 1
            index1 = index
        elif state == 1:
            exposed[index] = True
            index2 = index
            state = 2
        else:
            state = 1
            if number[index1] != number[index2]:
                exposed[index1] = False
                exposed[index2] = False
            index1 = index
            exposed[index] = True
            turn += 1             
      
# cards are logically 50x100 pixels in size    
def draw(canvas):
    label.set_text("Turns = " + str(turn))
    for index in range(0, len(number)):
        if exposed[index] == True:
            canvas.draw_text(str(number[index]), [index * 50 + 10, 75], 60, "White") 
        else:
            canvas.draw_polygon([(50 * index, 0), (50 * (index + 1), 0), (50 * (index + 1), 100), (50 * index, 100)], 2, 'Red', 'Green')
 
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")
 
# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)
 
# get things rolling
new_game()
frame.start()

#http://www.codeskulptor.org/#user41_vBf8f5uXsN_2.py
 
# Always remember to review the grading rubric