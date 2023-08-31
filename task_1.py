class InvalidLengthError(Exception):
    def __init__(self, length):
        self.length = length

    def __str__(self):
        return f"Недопустимая длина: {self.length}. Длина должна быть положительным числом."


class InvalidWidthError(Exception):
    def __init__(self, width):
        self.width = width

    def __str__(self):
        return f"Недопустимая ширина: {self.width}. Ширина должна быть положительным числом."


class Rectangle:
    def __init__(self, length, width=None):
        if width is None:
            self._length = length
            self._width = length
        else:
            self._length = length
            self._width = width

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, value):
        if value <= 0:
            raise InvalidLengthError(value)
        self._length = value

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value <= 0:
            raise InvalidWidthError(value)
        self._width = value

    def perimeter(self):
        return 2 * (self.length + self.width)

    def area(self):
        return self.length * self.width


try:
    rectangle = Rectangle(5, 3)
    print(f"Периметр: {rectangle.perimeter()}")
    print(f"Площадь: {rectangle.area()}")

    rectangle.length = 7
    rectangle.width = 4
    print(f"Периметр: {rectangle.perimeter()}")
    print(f"Площадь: {rectangle.area()}")

    rectangle.length = -2  # Вызовет исключение InvalidLengthError
except InvalidLengthError as e:
    print(f"Ошибка: {e}")

try:
    rectangle.width = -1  # Вызовет исключение InvalidWidthError
except InvalidWidthError as e:
    print(f"Ошибка: {e}")
