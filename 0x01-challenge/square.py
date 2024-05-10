#!/usr/bin/python3
"""
    A Square Class that calculates perimeter and area
"""

class Square:
    """A square class"""
        
    def __init__(self, *args, **kwargs):
        """The square constrictor"""
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def perimeter_of_my_square(self):
        """Perimeter of the square"""
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        "String Representation"
        return "{}/{}".format(self.width, self.height)

if __name__ == "__main__":
    """If file is run by itself"""

    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_my_square())
