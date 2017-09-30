from ._pyconrad import PyConrad, JClass
from jpype import JPackage
from pyconrad._autocomplete import AutoCompleteConrad


class ClassGetter:
    """
    Does the same thing as the old PyConrad()['Class'] but not globally,
    i.e. you can have multiple sets of namespaces (e.g. per file)
    """

    def __init__(self, *namespaces ):
        self._imported_namespaces = [ n for n in namespaces ]
        self.edu = JPackage('edu')
        self.ij = JPackage('ij')

    def add_namespaces(self, namespaces):
        if isinstance(namespaces, list):
            for e in namespaces:
                self.add_namespaces(e)
        self._imported_namespaces.append(namespaces)

    @property
    def SimpleVector(self):
        return JClass('edu.stanford.rsl.conrad.numerics.SimpleVector')

    @property
    def PointND(self):
        return JClass('edu.stanford.rsl.conrad.geometry.shapes.simple.PointND')

    @property
    def SimpleMatrix(self):
        return PyConrad().classes.stanford.rsl.conrad.numerics.SimpleMatrix

    @property
    def Grid1D(self):
        return JClass('edu.stanford.rsl.conrad.data.numeric.Grid1D')

    @property
    def Grid2D(self):
        return JClass('edu.stanford.rsl.conrad.data.numeric.Grid2D')

    @property
    def Grid3D(self):
        return JClass('edu.stanford.rsl.conrad.data.numeric.Grid3D')


    def enumval_from_int(self, enum_name: str, value_int):
        return self.__getattr__(enum_name).values()[int(value_int)]

    def enumval_from_string(self, enum_name: str, value_string: str):
        return self.__getattr__(enum_name).enum_name.valueOf(value_string)


    def __getattr__(self, classname):
        if not PyConrad.is_java_initalized():
            raise Exception('JVM not started! Use Pyconrad().setup()')
        success = None

        # Default namespace
        try:
            rtn = JClass(classname)
            success = rtn
        except Exception:
            pass

        # Imported namespaces
        for package in self._imported_namespaces:
            try:
                rtn = JClass(package + "." + classname)
                success = rtn
                break
            except Exception:
                pass

        if not success:
            raise Exception("Class \"%s\" not found in the following namespaces:\n %s" % (classname, self._imported_namespaces))

        return success

