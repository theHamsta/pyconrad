from jpype import *
import threading
import time
import os
import pyconrad.window_listener as wl
import pyconrad_java

conradPath = 'CONRAD/src'
libPath = 'CONRAD/lib'



def getInstance():
    if PyConrad._instance is None:
        PyConrad._instance = PyConrad()
    return PyConrad._instance

class PyConrad:

    classes = None
    ij = None

    conrad_repo_set = None
    conrad_repo_path = None

    javaInitalized = None
    isGuiStarted = None
    imageJInstance = None

    ijInstance = None
    guiInstance = None
    guiThread = None
    _instance = None

    __modulDir = None
    __libDir = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(PyConrad, cls).__new__(
                cls, *args, **kwargs)
        return cls._instance

    def setup(self, max_ram = '8G', min_ram = '7G', dev_dirs = []):
        if not self.isJavaInitalized():
            try:
                currDirectory = os.getcwd();
                conradSourceAndLibs = self.__importLibs__(dev_dirs)
                os.chdir(pyconrad_java.conrad_jar_dir)
                startJVM(getDefaultJVMPath(), conradSourceAndLibs, "-Xmx%s" % max_ram, "-Xmn%s" % min_ram )

                os.chdir(currDirectory)
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

    def __importLibs__(self, dev_dirs):
        # check whether CONRAD + RSL can be found nearby
        # yes: navigate there
        # no: use conrad.jar
        # list directories, check whether CONRAD/RSL are there
        directories = os.listdir()
        # if "CONRAD" in directories and "CONRADRSL" in directories:
        #     os.chdir("CONRAD")
        #     conradPath = os.path.dirname(os.getcwd()) + '/CONRAD'
        #     conradPath = conradPath.replace('\\', '/')
        #     conradloc = conradPath + "/src/"
        #     s = "-Djava.class.path=" + conradloc
        #
        #     os.chdir('..')
        #     os.chdir("CONRADRSL")
        #     conradRSLPath = os.path.dirname(os.getcwd()) + '/CONRADRSL'
        #     conradRSLPath = conradRSLPath.replace('\\', '/')
        #     conradRSLloc = conradRSLPath + "/src/"
        #     s = s + ';' + conradRSLloc
        #
        #     libloc = conradPath + "/lib/"
        #     ll = os.listdir(libloc)
        #     for i in ll:
        #         if ".jar" in i:
        #             s = s + ";" + libloc + i
        #     # Unix-like systems use : instead of ; to separate classpaths
        #     if os.name != 'nt':  # Windows
        #         s = s.replace(';',':')
        #
        # elif "CONRAD" in directories:
        #     os.chdir("CONRAD")
        #     conradPath = os.path.dirname(os.getcwd()) + '/CONRAD'
        #     conradPath = conradPath.replace('\\', '/')
        #     conradloc = conradPath + "/src/"
        #     s = "-Djava.class.path=" + conradloc
        #
        #     libloc = conradPath + "/lib/"
        #     ll = os.listdir(libloc)
        #     for i in ll:
        #         if ".jar" in i:
        #             s = s + ";" + libloc + i
        #     s = s + ";" + libloc + i
        #
        # else:
        if True: # TODO:

            s = "-Djava.class.path=%s" % pyconrad_java.conrad_jar_path
            dev_dirs.append(pyconrad_java.conrad_jar_dir + "/plugins")

            for dir in dev_dirs:
                ll = os.listdir(dir)
                for i in ll:
                    if ".jar" in i:
                        s = s + ";" + dir + i
                s = s + ";" + dir

        #Unix-like systems use : instead of ; to separate classpaths
        if os.name != 'nt':  # Windows
            s = s.replace(';',':')

        return s

    def terminate(self):
        shutdownJVM()
