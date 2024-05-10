from turtle import Turtle
STARTING_POSITIONS= [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE=20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
class Snake:
    def __init__(self):
        self.ttls= []
        self.create_snake()
        self.head = self.ttls[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_ttl(position)

    def move(self):
            for ttl_num in range(len(self.ttls)-1, 0, -1):
                new_x = self.ttls[ttl_num-1].xcor()
                new_y = self.ttls[ttl_num - 1].ycor()
                self.ttls[ttl_num].goto(new_x, new_y)
            self.ttls[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def add_ttl(self, position):
        new_ttl = Turtle("square")
        new_ttl.color("white")
        new_ttl.penup()
        new_ttl.goto(position)
        self.ttls.append(new_ttl)

    def extend(self):
        self.add_ttl(self.ttls[-1].position())
