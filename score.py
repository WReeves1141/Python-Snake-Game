from turtle import Turtle


class Score(Turtle):

    # ====================================================================== #
    #   Initializes the scoreboard.
    # ====================================================================== #
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("highscore.txt", mode="r") as score_file:
            self.high_score = score_file.read()
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", \
                   align="center", font=("Comic Sans", 24, "normal"))

    # ====================================================================== #
    #   Increases the numerical value on the scoreboard.
    # ====================================================================== #
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > int(self.high_score):
            self.high_score = self.score
            with open("highscore.txt", mode="w") as score_file:
                score_file.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()
