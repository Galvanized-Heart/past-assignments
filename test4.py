class Rectangle:
    pass

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width
    
    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."

        picture = ""
        for row in range(self.height):
            picture += "*" * self.width + "\n"
        return picture

    def get_amount_inside(self, shape):
        return int(self.get_area() / shape.get_area())


    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    
    def __init__(self, side):
        self.width = side
        self.height = side

    def set_side(self, side):
        self.width = side
        self.height = side

    def __str__(self):
        return f"Square(side={self.width})"

# Rectangle(width, height)
rect = Rectangle(7, 3)
print(rect.get_area())
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

# Square(side)
sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))