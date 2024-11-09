class BoundingRectangle:
    def __init__(self):
        self._min_x = float('inf')
        self._min_y = float('inf')
        self._max_x = float('-inf')
        self._max_y = float('-inf')
    
    def add_point(self, x, y):
        if x < self._min_x:
            self._min_x = x
        if y < self._min_y:
            self._min_y = y
        if x > self._max_x:
            self._max_x = x
        if y > self._max_y:
            self._max_y = y
    
    def width(self):
        return self._max_x - self._min_x

    
    def height(self):
        return self._max_y - self._min_y

    def top_y(self):
        return self._max_y

    def bottom_y(self):
        return self._min_y
    
    def left_x(self):
        return self._min_x
    
    def right_x(self):
        return self._max_x

rect = BoundingRectangle()
rect.add_point(-16, -11)
rect.add_point(14, -10)
rect.add_point(-18, 5)
print(rect.left_x(), rect.right_x())
print(rect.bottom_y(), rect.top_y())
print(rect.width(), rect.height())
print()
rect.add_point(-20, -9)
rect.add_point(17, -11)
rect.add_point(-17, 20)
print(rect.left_x(), rect.right_x())
print(rect.bottom_y(), rect.top_y())
print(rect.width(), rect.height())
print()
