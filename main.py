import math

import math

def rectangle_area(length, width):
    """
    Calculate the area of a rectangle.

    Parameters:
        length (float): The length of the rectangle. Must be non-negative.
        width (float): The width of the rectangle. Must be non-negative.

    Returns:
        float: The area of the rectangle.

    Raises:
        ValueError: If length or width is negative.
    """
    if length < 0 or width < 0:
        raise ValueError("Length and width must be non-negative.")
    return length * width

def triangle_area(base, height):
    """
    Calculate the area of a triangle.

    Parameters:
        base (float): The base of the triangle. Must be non-negative.
        height (float): The height of the triangle. Must be non-negative.

    Returns:
        float: The area of the triangle.

    Raises:
        ValueError: If base or height is negative.
    """
    """
    Calculate the area of a triangle.

    Parameters:
        base (float): The base of the triangle. Must be non-negative.
        height (float): The height of the triangle. Must be non-negative.

    Returns:
        float: The area of the triangle.

    Raises:
        ValueError: If base or height is negative.
    """
    if base < 0 or height < 0:
        raise ValueError("Base and height must be non-negative.")
    return 0.5 * base * height

# Test cases
def test_should_return_area():
    assert rectangle_area(5, 10) == 50
    assert rectangle_area(0, 10) == 0
    try:
        rectangle_area(-5, 10)
    except ValueError as e:
        assert str(e) == "Length and width must be non-negative."

def test_should_return_area2():
    assert triangle_area(6, 8) == 24
    assert triangle_area(0, 8) == 0
    try:
        triangle_area(-6, 8)
    except ValueError as e:
        assert str(e) == "Base and height must be non-negative."

