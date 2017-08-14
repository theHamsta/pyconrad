from jpype import *
import threading
import time
import os

conradPath = 'CONRAD/src'
libPath = 'CONRAD/lib'

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

    def setup(self):
        if not self.isJavaInitalized():
            try:
                conradSourceAndLibs = self.__importLibs__()
                startJVM(getDefaultJVMPath(), "-ea", conradSourceAndLibs)
                print("JVM Started(main): ", isJVMStarted())
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
        self.ij.WindowManager.closeAllWindows()
        self.ijGuiInstance.quit()
        self.guiStarted = False


    def __startRPFGUI___(self):
        attachThreadToJVM()
        self.guiInstance = JPackage("edu").stanford.rsl.apps.gui
        self.guiInstance.ReconstructionPipelineFrame.main(JArray(JString)(''))
        self.isGuiStarted = True
        print('Gui started', self.guiInstance)
        # detachThreadFromJVM()
        while self.isGuiStarted:
            if not self.ijInstance is None:#TODO: get ij Instance from ReconstructionPipelineFrame
                if (self.ijGuiInstance.quitting() == 1):
                    self.stopGui()
            time.sleep(1)

    def __startIJGUI___(self):
        attachThreadToJVM()
        self.guiInstance = JPackage("edu").stanford.rsl.conrad.utils
        self.guiInstance.CONRAD.setup()
        self.isGuiStarted = True
        print('Gui started', self.guiInstance)
        # detachThreadFromJVM()
        while self.isGuiStarted:
            if not self.ijInstance is None:  # TODO: get ij Instance from CONRAD
                if (self.ijGuiInstance.quitting() == 1):
                    self.stopGui()
            time.sleep(1)

    def __importLibs__(self):
        os.getcwd()
        os.chdir('..')
        os.chdir("CONRAD")
        conradPath = os.path.dirname(os.getcwd()) + '\\CONRAD'
        conradPath = conradPath.replace('\\', '/')
        conradloc = conradPath + "/src/"
        s = "-Djava.class.path=" + conradloc

        libloc = conradPath + "/lib/"
        ll = os.listdir(libloc)
        for i in ll:
            if ".jar" in i:
                s = s + ";" + libloc + i

        s = s.replace('/','\\')
        print(s)
        return s
