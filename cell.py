from window import *
from line import *
from point import *
class Cell():
    def __init__(self, window=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = window
        self.visited = False
    
    def draw(self, x1, y1, x2, y2):
        if self._win is None:
            return
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        if self.has_left_wall:
            self._win.draw_line(Line(Point(x1, y1),Point(x1, y2)), "black")
        if self.has_left_wall == False:
            self._win.draw_line(Line(Point(x1, y1),Point(x1, y2)), "white")
        if self.has_right_wall:
            self._win.draw_line(Line(Point(x2, y1), Point(x2, y2)), "black")
        if self.has_right_wall == False:
            self._win.draw_line(Line(Point(x2, y1), Point(x2, y2)), "white")
        if self.has_top_wall:
            self._win.draw_line(Line(Point(x1, y1), Point(x2, y1)), "black")
        if self.has_top_wall == False:
            self._win.draw_line(Line(Point(x1, y1), Point(x2, y1)), "white")
        if self.has_bottom_wall:
            self._win.draw_line(Line(Point(x1, y2), Point(x2, y2)), "black")
        if self.has_bottom_wall == False:
            self._win.draw_line(Line(Point(x1, y2), Point(x2, y2)), "white")


    def draw_move(self, to_cell, undo=False):
        # Calculate half widths and heights
        half_width = abs(self._x2 - self._x1) // 2
        half_height = abs(self._y2 - self._y1) // 2
    
        # Calculate centers
        x_center = self._x1 + half_width
        y_center = self._y1 + half_height
    
        half_width2 = abs(to_cell._x2 - to_cell._x1) // 2
        half_height2 = abs(to_cell._y2 - to_cell._y1) // 2
    
        x_center2 = to_cell._x1 + half_width2
        y_center2 = to_cell._y1 + half_height2
    
        fill_color = "red"
        if undo:
            fill_color = "gray"
    
        line = Line(Point(x_center, y_center), Point(x_center2, y_center2))
        self._win.draw_line(line, fill_color)
