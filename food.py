from turtle import Turtle
import random

class Food(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color("white")
        self.speed("fastest")
        self.refresh()
        
    def refresh(self):
        '''Method to re-locate the food after every collision with the snake'''
        rand_x = random.randint(-270,270)
        rand_y = random.randint(-270,270)
        self.goto(rand_x,rand_y)
        