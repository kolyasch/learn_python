from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 40, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.color('white')
        self.up()
        self.l_score = 0
        self.r_score = 0
        self.goto(x=0, y=240)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"{self.l_score}   {self.r_score}", font=FONT, align=ALIGNMENT)

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()
