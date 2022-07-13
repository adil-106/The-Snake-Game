from turtle import Turtle
class Snake():
    
    def __init__(self,shape,color):
        self.shape = shape
        self.color = color
        self.snake_segments = []    #Storing all turtle-snake segment objects
        
    def create_snake(self):
        '''Method to create initial 3 snake segments'''
        x_coordinate = 0
        for snakes in range(0,3):
            snake_segment = Turtle(self.shape)
            snake_segment.color(self.color)
            snake_segment.penup()
            snake_segment.setpos(x_coordinate,0)
            self.snake_segments.append(snake_segment)
            x_coordinate -= 20
    
    def move(self):
        '''Method to move the turtle'''
        for i in range(1,len(self.snake_segments)+1):
            if len(self.snake_segments)-i == 0:
                self.snake_segments[len(self.snake_segments)-i].forward(20)
            else:
                self.snake_segments[len(self.snake_segments)-i].goto(self.snake_segments[len(self.snake_segments)-i-1].pos())
    
    def up(self):
        if self.snake_segments[0].heading() != 270:
            self.snake_segments[0].setheading(90)
    
    def down(self):
        if self.snake_segments[0].heading() != 90:
            self.snake_segments[0].setheading(270)
    
    def right(self):
        if self.snake_segments[0].heading() != 180:
            self.snake_segments[0].setheading(0)
        
    def left(self):
        if self.snake_segments[0].heading() != 0:
            self.snake_segments[0].setheading(180)
    
    def add_segment(self):
        '''Method to add a segment after every food collison'''
        seg = Turtle(self.shape)
        seg.penup()
        seg.color(self.color)
        self.snake_segments.append(seg)
        
    def reset_snake(self):
        for snakes in self.snake_segments:
            snakes.goto(1000,1000)
        self.snake_segments.clear()
        self.snake_segments = []
        self.create_snake()
        
    
    
    
            