#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Создать абстрактный базовый класс Pair с виртуальными арифметическими операциями.
Реализовать производные классы Complex (комплексное число) и Rational (рациональное число).
"""

from abc import ABC, abstractmethod


class Pair(ABC):
    @abstractmethod
    def __add__(self, other):
        pass

    @abstractmethod
    def __sub__(self, other):
        pass

    @abstractmethod
    def __mul__(self, other):
        pass

    @abstractmethod
    def __truediv__(self, other):
        pass

    @abstractmethod
    def __str__(self):
        pass

def display(pair):
    print(f"Ответ: {pair}")


class Complex(Pair):
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        if isinstance(other, Complex):
            return Complex(self.real + other.real, self.imag + other.imag)
        else:
            raise ValueError("Неправильный тип данных")

    def __sub__(self, other):
        if isinstance(other, Complex):
            return Complex(self.real - other.real, self.imag - other.imag)
        else:
            raise ValueError("Неправильный тип данных")

    def __mul__(self, other):
        if isinstance(other, Complex):
            real_part = self.real * other.real - self.imag * other.imag
            imag_part = self.real * other.imag + self.imag * other.real
            return Complex(real_part, imag_part)
        else:
            raise ValueError("Неправильный тип данных")

    def __truediv__(self, other):
        if isinstance(other, Complex):
            denominator = other.real**2 + other.imag**2
            real_part = (self.real * other.real + self.imag * other.imag) / denominator
            imag_part = (self.imag * other.real - self.real * other.imag) / denominator
            return Complex(real_part, imag_part)
        else:
            raise ValueError("Неправильный тип данных")

    def __str__(self):
        return f"{self.real} + {self.imag}i"


class Rational(Pair):
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __add__(self, other):
        if isinstance(other, Rational):
            common_denominator = self.denominator * other.denominator
            result_numerator = (self.numerator * other.denominator) + (other.numerator * self.denominator)
            return Rational(result_numerator, common_denominator)
        else:
            raise ValueError("Неправильный тип данных")

    def __sub__(self, other):
        if isinstance(other, Rational):
            common_denominator = self.denominator * other.denominator
            result_numerator = (self.numerator * other.denominator) - (other.numerator * self.denominator)
            return Rational(result_numerator, common_denominator)
        else:
            raise ValueError("Неправильный тип данных")

    def __mul__(self, other):
        if isinstance(other, Rational):
            result_numerator = self.numerator * other.numerator
            result_denominator = self.denominator * other.denominator
            return Rational(result_numerator, result_denominator)
        else:
            raise ValueError("Неправильный тип данных")

    def __truediv__(self, other):
        if isinstance(other, Rational):
            result_numerator = self.numerator * other.denominator
            result_denominator = self.denominator * other.numerator
            return Rational(result_numerator, result_denominator)
        else:
            raise ValueError("Неправильный тип данных")

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"


if __name__ == '__main__':
    complex1 = Complex(1, 3)
    complex2 = Complex(1, 5)

    display(complex1 + complex2)
    display(complex1 - complex2)
    display(complex1 * complex2)
    display(complex1 / complex2)

    rational1 = Rational(3, 6)
    rational2 = Rational(1, 9)

    display(rational1 + rational2)
    display(rational1 - rational2)
    display(rational1 * rational2)
    display(rational1 / rational2)
