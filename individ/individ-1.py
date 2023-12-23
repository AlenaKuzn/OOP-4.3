#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Создать класс Pair (пара чисел); определить методы изменения полей и вы числения
произведения чисел. Определить производный класс RightAngled с полями-катетами.
Определить методы вычисления гипотенузы и площади треугольника.
"""

import math


class Triangle:
    def __init__(self, side_a, side_b, side_c):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def calculate_corner(self):
        self.angle_a = math.degrees(math.atan2(self.side_b, self.side_a))
        self.angle_b = 90 - self.angle_a
        self.angle_c = 90

    def calculate_perimeter(self):
        self.p =self.side_a + self.side_b + self.side_c

    def display(self):
        print(f"Углы равны: {self.angle_a:.2f}, {self.angle_b:.2f}, {self.angle_c:.2f}, периметр равен: {self.p}")


class RightAngled(Triangle):
    def __init__(self, side_a, side_b, side_c):
        super().__init__(side_a, side_b, side_c)
        self.area = self.calculate_area()

    def calculate_area(self):
        self.s = 0.5 * self.side_a * self.side_b

    def display(self):
        print(f"Площадь равна: {self.s}, углы равны: {self.angle_a:.2f}, {self.angle_b:.2f}, {self.angle_c:.2f}, периметр равен: {self.p}")


if __name__ == '__main__':
    triangle = Triangle(3, 4, 5)

    triangle.calculate_corner()
    triangle.calculate_perimeter()
    triangle.display()

    right_triangle = RightAngled(21, 20, 29)

    right_triangle.calculate_corner()
    right_triangle.calculate_perimeter()
    right_triangle.display()
