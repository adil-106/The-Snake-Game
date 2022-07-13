from turtle import Turtle

ALIGNMENT = "center"

FONT = ('Courier', 15, 'normal')

class Score(Turtle):
    
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0
        self.high_score = 0
        self.penup()
        self.setpos(0,270)
        self.pendown()
        self.color("white")
        self.write(f"Score: {self.score}    High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)
        
    def refresh(self):
        self.clear()
        self.write(f"Score: {self.score}    High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)
    
    def game_over_wall(self):
        self.setpos(0,0)
        self.write(f"Game Over! You Hit The Wall", move=False, align=ALIGNMENT, font=FONT)
    
    def game_over_tail(self):
        self.setpos(0,0)
        self.write(f"Game Over! You Ate Yourself", move=False, align=ALIGNMENT, font=FONT)
        
    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.refresh()
        #self.write(f"Score: {self.score}    High Score:{self.high_score}", move=False, align=ALIGNMENT, font=FONT)
        
        