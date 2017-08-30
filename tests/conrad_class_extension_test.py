from pyconrad import *

import numpy as np
import pyconrad._extend_conrad_classes
import jpype


jvm = PyConrad()
jvm.setup()
jvm.add_import('edu.stanford.rsl.conrad.geometry.shapes.simple')


point = jvm['PointND'](JArray(JDouble)([3.2,1.]))
print(type(point.numpy()))
print(point.numpy())

otherpoint = point.clone()
print(otherpoint.numpy())

# print(type(aclass))
#
# def say_hello(self):
#     print("hallo")
# aclass.numpy = say_hello
#
# print(type(aclass))
#
# grid = aclass(JArray(JDouble)([3,3]))
# grid.numpy()

# def add_to_numpy_method(magic):
#     class subclass(magic):
#         def __init__(self, *args):
#             super().__init__(self, *args)
#         def numpy(self):
#             return np.array(self.getCoordinates())
#     return subclass
#
# subclass = add_to_numpy_method(aclass)
# foo= subclass(3,3)
# print(subclass.numpy())
#

