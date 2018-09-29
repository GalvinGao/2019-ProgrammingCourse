import turtle as t

t.mode('standard')
t.speed(0)
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

    def rectangle(self, top_left_corner: tuple, bottom_right_corner: tuple, fill_color: str="black"):
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
    def circle(distance=DISTANCE):
        t.circle(RESIZE_RATIO * distance)


d = Draw()
d.line((0, 0), (24, 0))
d.line((5, 10), (0, 0))
d.line((19, 10), (24, 0))
d.rectangle((5, 10), (19, 12), "black")
d.line((7, 12), (10, 22))
d.line((17, 12), (14, 22))
d.rectangle((8, 22), (16, 23), "black")
d.line((10, 23), (11, 35))
d.line((13, 35), (14, 23))
d.rectangle((10, 35), (14, 36), "black")
d.line((11, 36), (11, 48))
d.line((13, 36), (13, 48))
d.line((19, 10), (0, 0))
d.line((5, 10), (24, 0))
d.line((14, 21), (7, 13))
d.line((17, 13), (10, 21))
d.line((13, 34), (10, 24))
d.line((11, 34), (14, 24))
d.line((13, 47), (11, 37))
d.line((11, 47), (13, 37))
d.goto(12, 48)
t.fillcolor("black")
t.begin_fill()
d.circle(2)
t.end_fill()
t.penup()
t.home()

t.done()
