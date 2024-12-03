# Python Game - In this section we will be creating a Python (Snake) Game

from tkinter import *
import random


# These are our (constants). Although Python does not really have constants, we can program these variables to
#behave as such. Our constants are designated by all caps
GAME_WIDTH = 900
GAME_HEIGHT = 600
SPEED = 300
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"

class Snake: # This is our class object
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        for i in range(0,BODY_PARTS):
            self.coordinates.append([0,0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x,y,x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="Snake")
            self.squares.append(square)



class Food: # This is our class object
    def __init__(self): # This will construct our food object for us
        x = random.randint(0, (GAME_WIDTH / SPACE_SIZE) - 1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT / SPACE_SIZE) - 1) * SPACE_SIZE

        self.coordinates = [x,y]

        canvas.create_oval(x,y,x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR,tag=Food)



def next_turn(snake, food):
    x, y = snake.coordinates[0]

    if direction == "up":
        y -= SPACE_SIZE

    elif direction == "down":
        y += SPACE_SIZE

    elif direction == "left":
        x -= SPACE_SIZE

    elif direction == "right":
        x += SPACE_SIZE


    snake.coordinates.insert(0, (x, y))

    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)

    snake.squares.insert(0, square)

    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score
        score += 1

        label.config(text="Score:{}".format(score))
        canvas.delete("food")

        food = Food()
    
    else:
        del snake.coordinates[-1]

        canvas.delete(snake.squares[-1])

        del snake.squares[-1]

    if check_collisions(snake):
        game_over()

    else:
        window.after(SPEED, next_turn, snake, food)

def change_direction(new_direction):
    global direction

    if new_direction == "left":
        if new_direction != "right":
            direction = new_direction

    elif new_direction == "right":
        if new_direction != "left":
            direction = new_direction

    elif new_direction == "up":
        if new_direction != "down":
            direction = new_direction

    elif new_direction == "down":
        if new_direction != "up":
            direction = new_direction        


def check_collisions(snake):
    x, y = snake.coordinates[0]

    if x < 0 or x >= GAME_WIDTH:
        return True
    
    elif y < 0 or y >= GAME_HEIGHT:
        return True
    
    #for body_part in snake.coordinates[1:]:
        #if x == body_part[0] and y == body_part[1]:
            #return True
        
    return False
        

def game_over():
    canvas.delete(ALL)

    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2,font=("Italic",72), 
                       text="Game Over",fill="red",tag="gameover")




window = Tk()
window.title("Python Papi")
window.resizable(False, False) # This is how we keep our window the same size. We can't expand or shrink the window 


score = 0
direction = "down"

label = Label(window,text="Score:{}".format(score), font=("consoles",45))
label.pack()

canvas = Canvas(window,bg=BACKGROUND_COLOR,height=GAME_HEIGHT,width=GAME_WIDTH) # Thos is how we create and define 
#our canvas
canvas.pack() # This is how we display our canvas in our winddow

# This is how program our canvas/window to open up in the middle of our screen
window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width / 2) - (window_width /2)) # We cast x as an int so we could get a whole number
y = int((screen_height / 2) - (window_height /2)) # We cast y as an int so we could get a whole number


window.geometry(f"{window_width}x{window_height}+{x}+{y}")
# The code of above is part of the window centering

window.bind("<Left>", lambda event: change_direction("left"))
window.bind("<Right>", lambda event: change_direction("right"))
window.bind("<Up>", lambda event: change_direction("up"))
window.bind("<Down>", lambda event: change_direction("down"))


snake = Snake()

food = Food()

next_turn(snake, food)

window.mainloop()