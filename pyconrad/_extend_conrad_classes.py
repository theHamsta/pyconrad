from jpype import *
import pyconrad

def say_hello(self):
    print("Hello!")


def extend_all_classes():
   pointnd_class = pyconrad.PyConrad().classes.stanford.rsl.conrad.geometry.shapes.simple.PointND
   pointnd_class.numpy = say_hello