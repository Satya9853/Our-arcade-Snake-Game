import turtle as t
ALIGNMENT = "center"
FONT = ("Arial", 14, 'normal')


class ScoreBoard(t.Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0
        with open("highscore.txt", mode='r') as saved_Score:
            self.highscore = saved_Score.read()
        self.penup()
        self.color('white')
        self.speed('fastest')
        self.goto(0, 280)
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align='center', font=('Arial', 24, 'normal'))

    def scoring_increment(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()


    def highscore_track(self):
        if self.score > int(self.highscore):
            self.highscore = self.score
            print(self.score)
            with open("highscore.txt", mode='w') as saved_score:
                saved_score.write(str(self.highscore))
            self.update_scoreboard()
        self.score = 0

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score} Highscore: {self.highscore}", align=ALIGNMENT, font=FONT)
