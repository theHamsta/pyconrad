import pyconrad
import jpype.awt.event.WindowAdapter as wa

class WindowListener(wa):

    def __init__(self, *mth, **kw) :
        object.__init__(self)

        for i, j in kw.items() :
            setattr(self, i, j)

    def windowActivated(self, e) :
        pass

    def windowClosed(self,  e) :
        pass

    def windowDeactivated(self,  e) :
        pass

    def windowDeiconified(self,  e) :
        pass

    def windowIconified(self,  e) :
        pass

    def windowOpened(self,  e) :
        pass

    def windowClosing(self, e):
        pyconrad.PyConrad.get_instance().__stop_gui()