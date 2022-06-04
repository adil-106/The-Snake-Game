from turtle import Turtle

ALIGNMENT = "center"

FONT = ('Courier', 15, 'normal')

class Score(Turtle):
    
    def __init__(self,score):
        super().__init__()
        self.hideturtle()
        self.score = score
        self.penup()
        self.setpos(0,270)
        self.pendown()
        self.color("white")
        self.write(f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)
        
    def refresh(self):
        self.clear()
    
    def game_over_wall(self):
        self.setpos(0,0)
        self.write(f"Game Over! You Hit The Wall", move=False, align=ALIGNMENT, font=FONT)
    
    def game_over_tail(self):
        self.setpos(0,0)
        self.write(f"Game Over! You Ate Yourself", move=False, align=ALIGNMENT, font=FONT)
        
        