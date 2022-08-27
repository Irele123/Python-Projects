from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.snake_pos = []
        self.pos = 0
        self.create_snake()
        self.head = self.snake_pos[0]

    def create_snake(self):
        for i in range(0, 3):
            turtle_obj = Turtle()
            turtle_obj.shape("square")
            turtle_obj.color("white")
            turtle_obj.penup()
            turtle_obj.goto(x=self.pos, y=0)
            self.snake_pos.append(turtle_obj)
            self.pos += -20

    def add_segment(self, position):
        turtle_obj = Turtle()
        turtle_obj.shape("square")
        turtle_obj.color("white")
        turtle_obj.penup()
        turtle_obj.goto(position)
        self.snake_pos.append(turtle_obj)

    def extend(self):
        self.add_segment(self.snake_pos[-1].position())

    def reset(self):
        for seg in self.snake_pos:
            seg.goto(1000, 1000)

        self.snake_pos.clear()
        self.create_snake()
        self.head = self.snake_pos[0]

    def move(self):
        for seg_num in range(len(self.snake_pos) - 1, 0, -1):
            new_x = self.snake_pos[seg_num - 1].xcor()
            new_y = self.snake_pos[seg_num - 1].ycor()
            self.snake_pos[seg_num].goto(new_x, new_y)
        self.snake_pos[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
