from jpype import JArray, JDouble, JInt
from ._pyconrad import PyConrad

def makeSimpleVector(vec):
    return PyConrad()["PyConradFabric"].makeSimpleVector(JArray(JDouble)(vec))

def makePointND(vec):
    return PyConrad()["PyConradFabric"].makePointND(JArray(JDouble)(vec))

def makeCameraAxisDirection(val):
    return PyConrad()["PyConradFabric"].makeCameraAxisDirection(JInt(val))
