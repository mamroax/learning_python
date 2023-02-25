class Rectangle:

    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

    def set_height(self, h):
        self.__height = h

    def set_width(self, w):
        self.__width = w

    def area(self):
        return self.__width * self.__height

rect = Rectangle(10, 20)
print(rect.get_height())
print(rect.get_width())
print(rect.area())