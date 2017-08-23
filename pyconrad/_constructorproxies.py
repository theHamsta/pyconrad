from jpype import *

def pointNdConstructor(array):
    if isinstance(array, JArray(JDouble)):
        return JClass('edu.stanford.rsl.conrad.geometry.shapes.simple.PointND')(array)
    else:
        return JClass('edu.stanford.rsl.conrad.geometry.shapes.simple.PointND')(JArray(JDouble)(array))

def simpleVectorConstructor(array):
    if isinstance(array, JArray(JDouble)):
        return JClass('edu.stanford.rsl.conrad.numerics.SimpleVector')(array)
    else:
        return JClass('edu.stanford.rsl.conrad.numerics.SimpleVector')(JArray(JDouble)(array))

