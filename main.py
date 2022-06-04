from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Score

#Setting up the game screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Snake Game")
screen.listen()

#Using tracer method to turn off animation until all initial snake segments are created
screen.tracer(0)    

#Setting up initial snake segments for game startup
snake = Snake("square","green")
snake.create_snake()

#Creating food object
food = Food()

#Setting on-click feature for turtle movement
screen.onkey(snake.up,key="Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")

score = 0

#Creating a turtle object for a scoreboard.
scoreboard = Score(score)

def detect_tail_collison():
    '''Function to detect collision of the snake with tail'''
    for i in range(1,len(snake.snake_segments)):
        if snake.snake_segments[0].distance(snake.snake_segments[i]) < 10:
            return True
    return False       
          
game_is_on = True
while game_is_on:
    snake.move()
    screen.update() # #Turning off the tracer method once all 3 initial segments of snake are created and on each movement
    time.sleep(0.1)
    
    #Detecting Collision with Food & Updating Scoreboard
    if snake.snake_segments[0].distance(food) < 15:
        score += 1
        scoreboard.refresh()
        food.refresh()
        scoreboard = Score(score)
        screen.tracer(0)
        snake.add_segment()
    
    #Detecting Collison with Wall
    if snake.snake_segments[0].xcor() < -280 or snake.snake_segments[0].ycor() < -280 or snake.snake_segments[0].xcor() > 280 or snake.snake_segments[0].ycor() > 280:
        scoreboard.game_over_wall()
        game_is_on = False
    
    #Detecting Collison with Tail
    if detect_tail_collison():
        scoreboard.game_over_tail()
        game_is_on = False
       

screen.exitonclick()