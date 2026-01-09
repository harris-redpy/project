import random 
import tkinter as tk


GAME_WIDTH = int(700)
GAME_HEIGTH = int(750)
SPEED = int(65)
SPACE_SIZE = int(50)
BODY_PARTS = 3
SNAKE_COLOR = "green"
FOOD_COLOR = "#ff0000"
BACKGROUND_COLOR = "BLACK"

class Snake:

    def __init__(self):

        self.body_size = BODY_PARTS
        self.coordinates =[]
        self.squares = []

        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 0])
        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tags="snake")
            self.squares.append(square)

        
   
    

class Food:

     def __init__(self):
         
         max_index = GAME_WIDTH // SPACE_SIZE  

         x = int(random.randint(0, max_index - 1) * SPACE_SIZE)
         y = int(random.randint(0, max_index - 1) * SPACE_SIZE) 

         self.coordinates = [x, y]
         canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tags="food")


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
    
    snake.coordinates.insert(0,(x, y))

    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)

    snake.squares.insert(0, square)

    if x == food.coordinates[0] and y == food.coordinates[1]:
            
            global score 

            score =+ (score + 1)

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

    if new_direction == 'left':
        if direction != 'right': 
          direction = new_direction
    elif new_direction == 'right':
        if direction != 'left':
            direction = new_direction    
    elif new_direction == 'up':
        if direction != 'down':
            direction = new_direction  
    elif new_direction == 'down':
        if direction != 'up':
            direction = new_direction          
            


    
def check_collisions(snake):
    x, y = snake.coordinates[0]

   
    if y < 0 or  y >= GAME_HEIGTH:
        return True
    elif x < 0 or  x >= GAME_WIDTH:
        return True
    

    for BODY_PARTS in snake.coordinates[1:]:
        if x == BODY_PARTS[0] and y == BODY_PARTS[1]:
            return True
        
    return False    
     

    

def game_over():
    canvas.delete("all")
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2, font=('consolas',70), text="GAME OVER", fill="red" )
    

window = tk.Tk()
window.title("snake game")
window.resizable(False, False)

score = 0
direction = 'down'

label = tk.Label(window, text="Score:{}" .format(score), font=('consolas', 40))
label.pack()

canvas = tk.Canvas(window,  bg=BACKGROUND_COLOR, height= GAME_HEIGTH, width= GAME_WIDTH)
canvas.pack()

window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

X = int((screen_width/2) - (window_width/2))
Y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{X}+{Y}")



window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down')) 


snake = Snake()
food = Food()

next_turn(snake, food)


window.mainloop()