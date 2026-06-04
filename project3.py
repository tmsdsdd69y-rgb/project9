'''
Bri Radding

This project creates a colorful outdoor scene with a house, sun, tree, grass, and clouds.
For Project 3, I refactored my original draw_scene function into smaller helper functions.
I made separate functions for the grass, sun, house, tree, and clouds so the code would
be easier to read and reuse. After refactoring, I made the scene more populated by adding
extra trees and clouds in the enhanced version.
'''

import turtle
import math


def setup_turtle():
    """Initialize turtle with standard settings"""
    t = turtle.Turtle()
    t.speed(0)
    screen = turtle.Screen()
    screen.title("Turtle Graphics Assignment")
    return t, screen


def draw_rectangle(t, width, height, fill_color=None):
    """Draw a rectangle with optional fill"""
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
    if fill_color:
        t.end_fill()


def draw_square(t, size, fill_color=None):
    """Draw a square with optional fill"""
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    for _ in range(4):
        t.forward(size)
        t.right(90)
    if fill_color:
        t.end_fill()


def draw_triangle(t, size, fill_color=None):
    """Draw an equilateral triangle with optional fill"""
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    for _ in range(3):
        t.forward(size)
        t.left(120)
    if fill_color:
        t.end_fill()


def draw_circle(t, radius, fill_color=None):
    """Draw a circle with optional fill"""
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    t.circle(radius)
    if fill_color:
        t.end_fill()


def draw_polygon(t, sides, size, fill_color=None):
    """Draw a regular polygon with given number of sides"""
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    angle = 360 / sides
    for _ in range(sides):
        t.forward(size)
        t.right(angle)
    if fill_color:
        t.end_fill()


def draw_curve(t, length, curve_factor, segments=10, fill_color=None):
    """
    Draw a curved line using small line segments
    Parameters:
    - t: turtle object
    - length: total length of the curve
    - curve_factor: positive for upward curve, negative for downward curve
    - segments: number of segments (higher = smoother curve)
    - fill_color: optional color to fill if creating a closed shape
    """
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()

    segment_length = length / segments
    original_heading = t.heading()

    for i in range(segments):
        angle = curve_factor * math.sin(math.pi * i / segments)
        t.right(angle)
        t.forward(segment_length)
        t.left(angle)

    t.setheading(original_heading)

    if fill_color:
        t.end_fill()


def jump_to(t, x, y):
    """Move turtle without drawing"""
    t.penup()
    t.goto(x, y)
    t.pendown()


def draw_grass_part(t):
    jump_to(t, -400, -40)
    t.setheading(0)
    draw_rectangle(t, 800, 260, "lightgreen")


def draw_sun_part(t):
    jump_to(t, 260, 260)
    draw_circle(t, 40, "yellow")


def draw_house_part(t):
    jump_to(t, -120, 120)
    t.setheading(0)
    draw_square(t, 180, "pink")

    jump_to(t, -140, 120)
    t.setheading(0)
    draw_triangle(t, 220, "purple")

    jump_to(t, -35, 50)
    t.setheading(0)
    draw_rectangle(t, 45, 70, "white")

    jump_to(t, -85, 100)
    t.setheading(0)
    draw_square(t, 35, "lightblue")

    jump_to(t, 15, 100)
    t.setheading(0)
    draw_square(t, 35, "lightblue")


def draw_tree_part(t, x, y):
    jump_to(t, x, y)
    t.setheading(0)
    draw_rectangle(t, 35, 90, "sienna")

    jump_to(t, x, y - 10)
    draw_circle(t, 35, "forestgreen")

    jump_to(t, x + 45, y - 10)
    draw_circle(t, 35, "forestgreen")

    jump_to(t, x + 22, y + 10)
    draw_circle(t, 40, "forestgreen")


def draw_cloud_part(t, x, y):
    jump_to(t, x, y)
    draw_circle(t, 22, "white")

    jump_to(t, x + 25, y - 10)
    draw_circle(t, 28, "white")

    jump_to(t, x + 60, y)
    draw_circle(t, 22, "white")


def draw_original_scene(t):
    draw_grass_part(t)
    draw_sun_part(t)
    draw_house_part(t)
    draw_tree_part(t, 150, -100)
    draw_cloud_part(t, -260, 320)
    draw_cloud_part(t, 20, 300)


def draw_enhanced_scene(t):
    draw_original_scene(t)

    draw_tree_part(t, -300, -100)
    draw_tree_part(t, 260, -100)

    draw_cloud_part(t, -80, 300)
    draw_cloud_part(t, 170, 320)


def draw_scene(t):
    """Draw both the original scene and the enhanced scene"""
    screen = t.getscreen()
    screen.bgcolor("skyblue")

    draw_original_scene(t)

    jump_to(t, 450, 0)
    draw_enhanced_scene(t)


def main():
    t, screen = setup_turtle()
    draw_scene(t)
    screen.mainloop()


if __name__ == "__main__":
    main()