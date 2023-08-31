"""
Make 4 functions named circle, rectange, square, triangle
Take parameter as you like

Return the area
"""


def circle(radius: float):
    return 3.16 * (radius**2)


def rectangle(length: float, breadth: float):
    return length * breadth


def square(side: float):
    return side**2


def triangle(base: float, height: float):
    return 0.5 * base * height


# Now instead of calling function..we can call these functions in other files also
