from tkinter import *
import random
import time
import turtle

#Tkinter Program starts here
root = Tk()
root.title("Snake -- Game")
root.geometry("680x700")
root.config(background = "black")
#setting the icon of the tkinter Window 
root.iconbitmap(r"C:\Users\Veeresh\Desktop\python project\favicon_2.ico")
#The icon has to be a .ico file only because allowed formats in Tkinter for changing
#the icon of the root window is only .ico

#Adding Image to the GUI Window
photo = PhotoImage(file = "snake1_edit.png")
img_label = Label(root,image = photo)
img_label.pack()

#defining functions for the buttons 
def close():
    root.destroy()

def play():

    #creating turtle screen
    screen = turtle.Screen()
    screen.title("SNAKE-GAME")#giving titles
    screen.setup(width = 700, height = 700)#describing dimensions of the game window
    screen.tracer(0)#for switching off the screen updates                 
                    #because we dont want to update the 
                    #length of the snak until it eats the food
                    #turns off the animation of the screen 
    screen.bgcolor('black') #setting background color


    ##creating a border for our game
    turtle.speed(5)
    turtle.pensize(4)
    turtle.penup()
    turtle.goto(-310,250)
    turtle.pendown()
    turtle.color('white')
    turtle.forward(600)
    turtle.right(90)
    turtle.forward(500)
    turtle.right(90)
    turtle.forward(600)
    turtle.right(90)
    turtle.forward(500)
    turtle.penup()
    turtle.hideturtle()

    #score
    score = 0
    delay = 0.1

    #snake
    snake = turtle.Turtle()
    snake.speed(0)
    snake.shape('square')
    snake.color("white")
    snake.penup()
    snake.goto(0,0)
    snake.direction = 'stop'


    #food
    colors = ["red","blue","yellow","green"]
    ans = random.choice(colors)
    food = turtle.Turtle()
    food.speed(0)
    food.shape('circle')
    food.color("white")
    food.penup()
    food.goto(30,30)

    segments=[]

    #scoring - for this we assign another turtle and use write to display appropriate text
    scoring = turtle.Turtle()
    scoring.speed(0)
    scoring.color("white")
    scoring.penup()
    scoring.hideturtle()
    scoring.goto(0,300)
    scoring.write("Score :",align="center",font=("Courier",24,"bold"))


    #######define how to move
    def snake_go_up():
        #restriction areises when its going in the opposite direction
        if snake.direction != "down":
            snake.direction = "up"

    def snake_go_down():
        if snake.direction != "up":
            snake.direction = "down"

    def snake_go_left():
        if snake.direction != "right":
            snake.direction = "left"

    def snake_go_right():
        if snake.direction != "left":
            snake.direction = "right"

    def snake_move():
        #defining the movements for the snake object 
        if snake.direction == "up":
            y = snake.ycor()
            snake.sety(y + 20)

        if snake.direction == "down":
            y = snake.ycor()
            snake.sety(y - 20)

        if snake.direction == "left":
            x = snake.xcor()
            snake.setx(x - 20)

        if snake.direction == "right":
            x = snake.xcor()
            snake.setx(x + 20)

    # Keyboard bindings
    # we invoke the .listen() to make the program aware of the scren bindings
    # parameters are 1st --> funtion $$$$$$$$ 2nd -- > key to be pressed on the keyboard5
    screen.listen()
    screen.onkeypress(snake_go_up, "Up")
    screen.onkeypress(snake_go_down, "Down")
    screen.onkeypress(snake_go_left, "Left")
    screen.onkeypress(snake_go_right, "Right")

    #main loop which is similar to root.mainloop() in tkinter

    while True:
            screen.update() # now we want the updates to be showed
            #snake and fruit coliisions
            if snake.distance(food)< 20:
                    x = random.randint(-290,270)
                    y = random.randint(-240,240)
                    food.goto(x,y)
                    scoring.clear()
                    score+=1
                    scoring.write("Score:{}".format(score),align="center",font=("Courier",24,"bold"))
                    delay-=0.001
                    
                    ## creating new_ball
                    colors = ["red","blue","yellow","green"]
                    ans = random.choice(colors)
                    new_length = turtle.Turtle()               
                    new_length.speed(0)
                    new_length.shape('square')
                    new_length.color(ans)
                    new_length.penup()
                    segments.append(new_length)
                    

             
            for index in range(len(segments)-1,0,-1):
                    a = segments[index-1].xcor()
                    b = segments[index-1].ycor()

                    segments[index].goto(a,b)
                                        
            if len(segments)>0:
                    a= snake.xcor()
                    b = snake.ycor()
                    segments[0].goto(a,b)
            snake_move()

            ##snake and border collision    
            if snake.xcor()>280 or snake.xcor()< -300 or snake.ycor()>240 or snake.ycor()<-240:
                    time.sleep(1)
                    screen.clear()
                    screen.bgcolor('black')
                    scoring.goto(0,0)
                    scoring.write("   GAME OVER \n Your Score is {}".format(score),align="center",font=("Courier",30,"bold"))


            ## snake collision
            for segment in segments:
                    if segment.distance(snake) < 20:
                            time.sleep(1)
                            screen.clear()
                            screen.bgcolor('black')
                            scoring.goto(0,0)
                            scoring.write("    GAME OVER \n Your Score is {}".format(score),align="center",font=("Courier",30,"bold"))
                  
            time.sleep(delay)
    root.destroy()
    turtle.Terminator()
    

l1 = Label(text = "Welcome to the Snake-Game",font="consolas 23 bold",fg="green",bg="black")
l1.pack(pady=20,padx=100)
  

l2 = Label(text = "Click Play to play the Game !\nOR \nClick Quit to exit the Game !!",bg="black",fg="green",font=("consolas", "20"))
l2.pack(pady=20,padx=100)

b_play = Button(text = "Play",fg="green",font = "consolas 20",bg="black",command=play)
b_play.pack(pady=20)

b_quit = Button(text="Quit",fg="red",bg="black",font = ("consolas", "20"),command = close)
b_quit.pack()

root.mainloop()