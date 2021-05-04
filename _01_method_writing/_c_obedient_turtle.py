"""
Make an obedient turtle that will obey commands to draw shapes.
"""
from tkinter import messagebox, simpledialog, Tk
import turtle

def draw_square(t):
    for i in range(4):
        t.forward(100)
        t.right(90)
def draw_triangle(t):
    for i in range(3):
        t.forward(100)
        t.right(120)

def draw_circle(t):
    for i in range(360):
        t.forward(1)
        t.right(1)

if __name__ == '__main__':
    # TODO)
    #   1. Create a turtle.
    window = Tk()
    window.withdraw()

    shelly = turtle.Turtle()
    shape = simpledialog.askstring(None, "What shape do you want the turtle to draw?")
    if shape.lower() == "circle":
        draw_circle(shelly)
    elif shape.lower() == "triangle":
        draw_triangle(shelly)
    elif shape.lower() == "square":
        draw_square(shelly)
    #   2. Write 3 method definitions for drawing a square, triangle, and
    #      circle.
    #   3. Ask the user for the for a shape to draw.
    #   4. Draw the appropriate shape depending on their answer (call the right
    #      function)
