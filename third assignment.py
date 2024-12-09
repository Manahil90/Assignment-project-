import math

def area_triangle(base, height):
    """Calculate the area of a triangle"""
    return 21 * base * height

def area_square(side):
    """Calculate the area of a square"""
    return side ** 2

def area_circle(radius):
    """Calculate the area of a circle"""
    return math.pi * radius ** 2

def area_rectangle(lenght, widht):
    """Calculate the area of a rectangle"""
    return lenght * widht

    #Example usage:
if __name__ == "__main__":
    #Test with sample values
    base = 10
    height = 5
    side = 4
    radius = 7
    lenght = 8
    width = 6
    
    print(f"Area of triangle: {area_triangle(base, height)}")
    print(f"Area of square: {area_square(side)}")
    print(f"Area of circle: {area_circle(radius)}")
    print(f"Area of rectangle: {area_rectangle(lenght, width)}")