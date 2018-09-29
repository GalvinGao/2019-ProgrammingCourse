import time
import turtle as t

t.speed(10)
t.pencolor("")
time.sleep(10)


class Block:
    def __init__(self, block_size: int = 16):
        self.block_size = block_size

    def add(self, x: int, y: int, color: str):
        t.pensize(0)
        t.penup()
        # Reset the position of the turtle
        t.home()
        # Let the turtle go to the west-south corner of the next block
        t.forward(x * self.block_size)
        t.left(90)
        t.forward(y * self.block_size)
        t.setheading(0)
        t.pendown()
        # Now draw the block
        t.fillcolor(color)
        t.begin_fill()
        for _ in range(4):
            t.forward(self.block_size)
            t.left(90)
        t.end_fill()

    def bulk(self, operations: list):
        operations.reverse()
        for row_index, row_operations in enumerate(operations):
            for column_index, column_operation in enumerate(row_operations):
                self.add(x=column_index, y=row_index, color=column_operation)


class Draw:
    @staticmethod
    def cow():
        block = Block(block_size=32)
        block.bulk([["#2d231a", "#30261b", "#2d231a", "#818182", "#818182", "#5d5d5e", "#5d5d5e", "#261e17"],
                    ["#31271c", "#31271c", "#31271c", "#848485", "#848485", "#818182", "#261e17", "#30261b"],
                    ["#919192", "#919192", "#30261b", "#818182", "#818182", "#30261b", "#919192", "#919192"],
                    ["#000000", "#b7b7ba", "#2d231a", "#747475", "#2d231a", "#2d231a", "#b7b7ba", "#000000"],
                    ["#2d231a", "#2d231a", "#2d231a", "#2d231a", "#2d231a", "#2d231a", "#2d231a", "#2d231a"],
                    ["#2d231a", "#261e17", "#9e9ea0", "#9e9ea0", "#9e9ea0", "#9e9ea0", "#261e17", "#2d231a"],
                    ["#2d231a", "#9e9ea0", "#000000", "#454546", "#454546", "#000000", "#9e9ea0", "#2d1e17"],
                    ["#2d231a", "#8d8d8f", "#454546", "#353535", "#353535", "#454546", "#9e9ea0", "#2d231a"]])
        t.home()


draw = Draw()
draw.cow()

t.done()
