#!/usr/bin/env python  

from abc import ABCMeta, abstractmethod

class IPolygon():

    __metaclass__ = ABCMeta

    @abstractmethod
    def number_of_sides(self):
        pass



class Rectangle(IPolygon):

    def __init__(self):
        self.name = "RECTANGLE"

    def number_of_sides(self):
        print("I have 2 sides")


Shape = Rectangle()
Shape.number_of_sides()
print("%s" % Shape.name)