from turtle import Turtle

# Global Variables
DOWN = 270
LEFT = 180
MOVE_DISTANCE = 15
RIGHT = 0
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90


class Snake:

    # ====================================================================== #
    #   Creates the snake with segments.
    # ====================================================================== #
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    # ====================================================================== #
    #   Initializes the starting snake segments.
    # ====================================================================== #
    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle("circle")
            if position == STARTING_POSITIONS[1]:
                new_segment.color("orange")
            else:
                new_segment.color("green")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    # ====================================================================== #
    #   Initializes a new snake segment.
    # ====================================================================== #
    def add_segment(self, position):
        new_segment = Turtle("circle")
        new_segment.color("green")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    # ====================================================================== #
    #   Adds a new snake segment to the end of the snake.
    # ====================================================================== #
    def extend(self):
        self.add_segment(self.segments[-1].position())

    # ====================================================================== #
    #   Changes the position of the segments to follow after the head.
    # ====================================================================== #
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
            # TODO 1: Change segment heading to match direction
            # new_heading = self.segments[seg_num].heading()
            # self.segments[seg_num].setheading(new_heading)

        self.segments[0].forward(MOVE_DISTANCE)

    # ====================================================================== #
    #   Changes the direction of the snake to go north.
    # ====================================================================== #
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    # ====================================================================== #
    #   Changes the direction of the snake to go south.
    # ====================================================================== #
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    # ====================================================================== #
    #   Changes the direction of the snake to go west.
    # ====================================================================== #
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    # ====================================================================== #
    #   Changes the direction of the snake to go east.
    # ====================================================================== #
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)
