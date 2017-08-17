from jpype import *
import threading
import time
import os
import pyconrad.window_listener as wl

conradPath = 'CONRAD/src'
libPath = 'CONRAD/lib'


def getInstance():
    if PyConrad._instance is None:
        PyConrad._instance = PyConrad()
    return PyConrad._instance

class PyConrad:

    classes = None
    ij = None

    javaInitalized = None
    isGuiStarted = None
    imageJInstance = None

    ijInstance = None
    guiInstance = None
    guiThread = None
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(PyConrad, cls).__new__(
                cls, *args, **kwargs)
        return cls._instance

    def setup(self, max_ram = '8G', min_ram = '7G'):
        if not self.isJavaInitalized():
            try:
                conradSourceAndLibs = self.__importLibs__()
                startJVM(getDefaultJVMPath(), conradSourceAndLibs, "-Xmx%s" % max_ram, "-Xmn%s" % min_ram )
                self.classes = JPackage('edu')
                self.ij = JPackage('ij')

            except JException as ex:
                print(ex)
            self.javaInitalized = True
        else:
            print("JVM already started")

    def startConrad(self):
        if self.guiThread is None:
            self.guiThread = threading.Thread(target=self.__startIJGUI___)
            self.guiThread.start()
            while not self.isGuiStarted:
                time.sleep(1)
        else:
            print("Some GUI is already started")

    def startReconstructionFilterPipeline(self):
        if self.guiThread is None:
            self.guiThread = threading.Thread(target=self.__startRPFGUI___)
            self.guiThread.start()
            while not self.isGuiStarted:
                time.sleep(1)
        else:
            print("Some GUI is already started")

    def isJavaInitalized(self):
        return self.javaInitalized

    def stopGui(self):
        java.lang.System.exit(0)
        self.isGuiStarted = False

    def __startRPFGUI___(self):
        attachThreadToJVM()
        self.guiInstance = JPackage("edu").stanford.rsl.apps.gui
        listener = wl.WindowListener()
        proxy = JProxy("java.awt.event.WindowListener", inst=listener)
        self.guiInstance.ReconstructionPipelineFrame
        self.guiInstance.ReconstructionPipelineFrame.startConrad(proxy)
        self.isGuiStarted = True
        print('Gui started', self.guiInstance)
        detachThreadFromJVM()
        while self.isGuiStarted:
            time.sleep(1)

    def __startIJGUI___(self):
        attachThreadToJVM()
        self.guiInstance = JPackage("edu").stanford.rsl.conrad.utils
        listener = wl.WindowListener()
        proxy = JProxy("java.awt.event.WindowListener", inst=listener)
        self.guiInstance.CONRAD.setup(proxy)
        self.isGuiStarted = True
        print('Gui started', self.guiInstance)
        detachThreadFromJVM()
        while self.isGuiStarted:
            time.sleep(1)

    def __importLibs__(self):
        # check whether CONRAD + RSL can be found nearby
        # yes: navigate there
        # no: use conrad.jar
        currDirectory = os.getcwd();

        s = ""
        os.chdir(os.path.dirname(__file__))
        os.chdir('..')
        os.chdir('..')
        # list directories, check whether CONRAD/RSL are there
        directories = os.listdir()
        if "CONRAD" in directories and "CONRADRSL" in directories:
            os.chdir("CONRAD")
            conradPath = os.path.dirname(os.getcwd()) + '/CONRAD'
            conradPath = conradPath.replace('\\', '/')
            conradloc = conradPath + "/src/"
            s = "-Djava.class.path=" + conradloc

            os.chdir('..')
            os.chdir("CONRADRSL")
            conradRSLPath = os.path.dirname(os.getcwd()) + '/CONRADRSL'
            conradRSLPath = conradRSLPath.replace('\\', '/')
            conradRSLloc = conradRSLPath + "/src/"
            s = s + ';' + conradRSLloc

            libloc = conradPath + "/lib/"
            ll = os.listdir(libloc)
            for i in ll:
                if ".jar" in i:
                    s = s + ";" + libloc + i
            # Unix-like systems use : instead of ; to separate classpaths
            if os.name != 'nt':  # Windows
                s = s.replace(';',':')

        elif "CONRAD" in directories:
            os.chdir("CONRAD")
            conradPath = os.path.dirname(os.getcwd()) + '/CONRAD'
            conradPath = conradPath.replace('\\', '/')
            conradloc = conradPath + "/src/"
            s = "-Djava.class.path=" + conradloc

            libloc = conradPath + "/lib/"
            ll = os.listdir(libloc)
            for i in ll:
                if ".jar" in i:
                    s = s + ";" + libloc + i
            s = s + ";" + libloc + i

        else:
            s = "-Djava.class.path=pyCONRAD/lib/conrad_1.0.6.jar"

        # Unix-like systems use : instead of ; to separate classpaths
        if os.name != 'nt':  # Windows
            s = s.replace(';',':')

        os.chdir(currDirectory)
        
        return s

    def terminate(self):
        shutdownJVM()
