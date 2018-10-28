import time
import turtle

# Goal: No use of turtle classes in actual running code (in { if __name__ == "__main__": })
turtle.mode('standard')
turtle.speed(10)
DISTANCE = 8
BLOCK_SIZE = 6


# Seems like we got a canvas that is 730 * 640


class Restorer:
    def __init__(self):
        self.last_pos = turtle.pos()

    def restore(self):
        turtle.goto(self.last_pos[0], self.last_pos[1])


class Draw:
    def goto(self, x, y, heading=0):
        turtle.penup()
        turtle.goto(x * BLOCK_SIZE, y * BLOCK_SIZE)
        turtle.setheading(heading)
        turtle.pendown()

    def line(self, first_line=(), second_line=()):
        restorer = Restorer()
        assert len(first_line) == 2 and type(
            first_line) == tuple, "'first_line' must be a Tuple object with 2 positional parameters."
        assert len(second_line) == 2 and type(
            second_line) == tuple, "'second_line' must be a Tuple object with 2 positional parameters."
        turtle.penup()
        turtle.goto(first_line[0] * BLOCK_SIZE, first_line[1] * BLOCK_SIZE)
        turtle.pendown()
        turtle.goto(second_line[0] * BLOCK_SIZE, second_line[1] * BLOCK_SIZE)
        turtle.penup()
        restorer.restore()

    def function(self, function, trace_size: float = 0.1, x_range: tuple = (), y_range: tuple = ()):
        restorer = Restorer()
        for index in range(trace_size, trace_size):
            y = function(index)
        restorer.restore()

    def rectangle_absolute(self, top_left_corner: tuple, bottom_right_corner: tuple, fill_color: str = "black"):
        turtle.fillcolor(fill_color)
        self.goto(top_left_corner[0], top_left_corner[1])
        turtle.begin_fill()
        for _ in range(2):
            turtle.forward((bottom_right_corner[0] - top_left_corner[0]) * BLOCK_SIZE)
            turtle.left(90)
            turtle.forward((bottom_right_corner[1] - top_left_corner[1]) * BLOCK_SIZE)
            turtle.left(90)
        turtle.end_fill()

    def square(self, length: int = DISTANCE, stroke="black"):
        turtle.color(stroke)
        for _ in range(4):
            turtle.forward(length * BLOCK_SIZE)
            self.turn_left()

    def rectangle(self, x_side, y_side):
        for _ in range(2):
            turtle.forward(x_side * BLOCK_SIZE)
            self.turn_left()
            turtle.forward(y_side * BLOCK_SIZE)
            self.turn_left()

    def triangle(self):
        self.polygon(sides=3, fill="white", stroke="black")

    def circle(self, distance: float = DISTANCE):
        turtle.circle(BLOCK_SIZE * distance)

    def polygon(self, sides=5, fill="red", stroke="black"):
        assert sides >= 3, "Side amount of a polygon should be greater or equals to 3."
        turtle.color(stroke, fill)
        turn_angle = 360 / sides
        turtle.begin_fill()
        for i in range(sides):
            turtle.forward(BLOCK_SIZE * DISTANCE / sides * 5)
            turtle.left(turn_angle)
        turtle.end_fill()

    def car(self):
        self.goto(-4, -3)
        self.rectangle(8, 3)
        turtle.fillcolor("black")
        self.goto(-2, -4)
        turtle.begin_fill()
        self.circle(1)
        turtle.end_fill()
        self.goto(2, -4)
        turtle.begin_fill()
        self.circle(1)
        turtle.end_fill()
        self.goto(-4, -2.5)
        turtle.begin_fill()
        self.circle(.5)
        turtle.end_fill()

    def mickey_mouse(self):
        self.goto(0, -4)
        turtle.fillcolor("black")
        turtle.begin_fill()
        self.circle(4)
        turtle.end_fill()
        self.goto(-3.9, 2.4)
        turtle.begin_fill()
        self.circle(2)
        turtle.end_fill()
        self.goto(3.9, 2.4)
        turtle.begin_fill()
        self.circle(2)
        turtle.end_fill()

    def house(self):
        # we should have a door!
        self.goto(6, 0)
        self.rectangle(1, 2)
        # umm, what about a building with 5 floors~
        for side_offset in range(5):
            # building (each floor)
            self.goto(0, 3 * side_offset)
            self.rectangle(8, 3)
            # windows
            self.goto(2, 3 * side_offset + 1)
            self.rectangle(1, 1)
            # air conditioner (outside machine)
            self.goto(-0.5, 3 * side_offset + 1)
            self.rectangle(0.5, 1)
            # Balcony ;)
            if side_offset == 0:  # but not at the first floor
                continue
            else:
                pass
            # balcony floor
            self.goto(8, 3 * side_offset + 0.618)
            self.rectangle(1, 0.2)
            # balcony railing
            self.goto(8 + 1 - 0.2, 3 * side_offset + 0.618 + 0.2)
            self.rectangle(0.2, 1.3)

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
        turtle.fillcolor("black")
        turtle.begin_fill()
        self.circle(2)
        turtle.end_fill()

    def turn_left(self):
        turtle.left(90)

    def turn_right(self):
        turtle.right(90)

    def turn_around(self):
        turtle.left(180)

    def start_section(self, text):
        turtle.penup()
        self.turn_right()
        turtle.forward(DISTANCE * BLOCK_SIZE)
        turtle.pendown()
        turtle.write(text)
        turtle.penup()
        self.goto(0, 0, 0)
        turtle.pendown()
        turtle.pensize(2)

    def end_section(self):
        time.sleep(.5)
        turtle.reset()


if __name__ == "__main__":
    draw = Draw()
    # 1. Square
    draw.start_section("1. Square")
    draw.square()
    draw.end_section()
    # 2. Rectangle
    draw.start_section("2. Rectangle")
    draw.rectangle(x_side=8, y_side=4)
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
    draw.square(stroke="blue")
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
    # 9. Mickey Mouse
    draw.start_section("9. Mickey Mouse")
    draw.mickey_mouse()
    draw.end_section()
    # 10. Eiffel Tower
    draw.start_section("10. Eiffel Tower")
    draw.tower()
    draw.end_section()
