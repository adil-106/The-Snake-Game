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
food = Food()

screen.onkey(snake.up,key="Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")

# #Turning off the tracer method once all 3 initial segments of snake are created.
# screen.update()   

score = 0
scoreboard = Score(score)

def detect_tail_collison():
    for i in range(1,len(snake.snake_segments)):
        if snake.snake_segments[0].distance(snake.snake_segments[i]) < 10:
            return True
    return False       
    
        
game_is_on = True
while game_is_on:
    snake.move()
    screen.update()
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