import time
import turtle as t

t.mode('standard')
t.speed(8)
DISTANCE = 8
RESIZE_RATIO = 6

t.pensize(RESIZE_RATIO)


class Restorer:
    def __init__(self):
        self.last_pos = t.pos()

    def restore(self):
        t.goto(self.last_pos[0], self.last_pos[1])


class Draw:
    @staticmethod
    def goto(x, y, heading=0):
        t.penup()
        t.goto(x * RESIZE_RATIO, y * RESIZE_RATIO)
        t.setheading(heading)
        t.pendown()

    @staticmethod
    def line(first_line=(), second_line=()):
        restorer = Restorer()
        assert len(first_line) == 2 and type(
            first_line) == tuple, "'first_line' must be a Tuple object with 2 positional parameters."
        assert len(second_line) == 2 and type(
            second_line) == tuple, "'second_line' must be a Tuple object with 2 positional parameters."
        t.penup()
        t.goto(first_line[0] * RESIZE_RATIO, first_line[1] * RESIZE_RATIO)
        t.pendown()
        t.goto(second_line[0] * RESIZE_RATIO, second_line[1] * RESIZE_RATIO)
        t.penup()
        restorer.restore()

    def rectangle_absolute(self, top_left_corner: tuple, bottom_right_corner: tuple, fill_color: str = "black"):
        t.fillcolor(fill_color)
        self.goto(top_left_corner[0], top_left_corner[1])
        t.begin_fill()
        for _ in range(2):
            t.forward((bottom_right_corner[0] - top_left_corner[0]) * RESIZE_RATIO)
            t.left(90)
            t.forward((bottom_right_corner[1] - top_left_corner[1]) * RESIZE_RATIO)
            t.left(90)
        t.end_fill()

    @staticmethod
    def circle(distance: float = DISTANCE):
        t.circle(RESIZE_RATIO * distance)

    def function(self, _function, trace_size: float = 0.1, x_range: tuple = (), y_range: tuple = ()):
        restorer = Restorer()
        for index in range(trace_size, trace_size):
            y = _function(index)
        restorer.restore()

    def square(self, stroke="black"):
        t.color(stroke)
        for _ in range(4):
            t.forward(DISTANCE * RESIZE_RATIO)
            self.turn_left()

    def rectangle_relative(self, x_side, y_side):
        for _ in range(2):
            t.forward(x_side * RESIZE_RATIO)
            self.turn_left()
            t.forward(y_side * RESIZE_RATIO)
            self.turn_left()

    def triangle(self):
        self.polygon(sides=3, fill="white", stroke="black")

    def circle(self, distance=DISTANCE):
        t.circle(RESIZE_RATIO * distance)

    def polygon(self, sides=5, fill="red", stroke="black"):
        assert sides >= 3, "Side amount of a polygon should be greater or equals to 3."
        t.color(stroke, fill)
        turnAngle = 360 / sides
        t.begin_fill()
        for i in range(sides):
            t.forward(RESIZE_RATIO * DISTANCE / sides * 5)
            t.left(turnAngle)
        t.end_fill()

    def car(self):
        self.goto(-4, -3)
        self.rectangle_relative(8, 3)
        t.fillcolor("black")
        self.goto(-2, -4)
        t.begin_fill()
        self.circle(1)
        t.end_fill()
        self.goto(2, -4)
        t.begin_fill()
        self.circle(1)
        t.end_fill()
        self.goto(-4, -2.5)
        t.begin_fill()
        self.circle(0.5)
        t.end_fill()

    def house(self):
        self.rectangle_relative(8, 6)
        self.goto(8, 6, heading=-150)
        triangle_sides = 4.6
        t.forward(triangle_sides * RESIZE_RATIO)
        t.left(60)
        t.forward(triangle_sides * RESIZE_RATIO)


    def tower(self):
        self.line((0, 0), (24, 0))
        self.line((5, 10), (0, 0))
        self.line((19, 10), (24, 0))
        self.rectangle_absolute((5, 10), (19, 12), "black")
        self.line((7, 12), (10, 22))
        self.line((17, 12), (14, 22))
        self.rectangle_absolute((8, 22), (16, 23), "black")
        self.line((10, 23), (11, 35))
        self.line((13, 35), (14, 23))
        self.rectangle_absolute((10, 35), (14, 36), "black")
        self.line((11, 36), (11, 48))
        self.line((13, 36), (13, 48))
        self.line((19, 10), (0, 0))
        self.line((5, 10), (24, 0))
        self.line((14, 21), (7, 13))
        self.line((17, 13), (10, 21))
        self.line((13, 34), (10, 24))
        self.line((11, 34), (14, 24))
        self.line((13, 47), (11, 37))
        self.line((11, 47), (13, 37))
        self.goto(12, 48)
        t.fillcolor("black")
        t.begin_fill()
        self.circle(2)
        t.end_fill()

    def turn_left(self):
        t.left(90)

    def turn_right(self):
        t.right(90)

    def turn_around(self):
        t.left(180)

    def start_section(self, text):
        t.penup()
        self.turn_right()
        t.forward(DISTANCE * RESIZE_RATIO)
        t.pendown()
        t.write(text)
        t.penup()
        self.goto(0, 0, 0)
        t.pendown()
        t.pensize(2)

    def end_section(self):
        time.sleep(.5)
        t.reset()


draw = Draw()

# 1. Square
draw.start_section("1. Square")
draw.square()
draw.end_section()
# 2. Rectangle
draw.start_section("2. Rectangle")
draw.rectangle_relative(8, 4)
draw.end_section()
# 3. Triangle
draw.start_section("3. Triangle")
draw.triangle()
draw.end_section()
# 4. Circle
draw.start_section("4. Circle")
draw.circle()
draw.end_section()
# 5. Blue Square
draw.start_section("5. Blue Square")
draw.square("blue")
draw.end_section()
# 6. Hexagon with red background and yellow border
draw.start_section("6. Hexagon with red background and yellow border")
draw.polygon(sides=6, fill="red", stroke="yellow")
draw.end_section()
# 7. Car
draw.start_section("7. Car")
draw.car()
draw.end_section()
# 8. House
draw.start_section("8. House")
draw.house()
draw.end_section()
# 10. Tower
draw.start_section("10. Tower")
draw.tower()
draw.end_section()
