from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('save.txt') as file:
            self.high_score = int(file.read())

        self.up()
        self.goto(x=0, y=260)
        self.color('white')
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High score: {self.high_score}", font=FONT, align=ALIGNMENT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('save.txt', mode='w') as file:
                file.write(f'{self.high_score}')

        self.score = 0
        self.update_scoreboard()
