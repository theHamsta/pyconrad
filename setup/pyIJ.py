from jpype import *
import os
import threading
import time

class PyIJ:
    "ImageJ Gui wraped in python"
    javaInitalized = None
    guiStarted = None
    classes = None
    ijGuiInstance = None
    guiThread = None
    pyijInstance = None

    def __init__(self):
        self.pyijInstance = self

    def initJava(self):
        if not self.isInitialized():
            try:
                os.chdir('..')
                startJVM(getDefaultJVMPath(), "-ea", "-Djava.class.path=lib/ij.jar")
                print("JVM Started(main): ", isJVMStarted())
                self.classes = JPackage('ij')
            except JException as ex:
                print(ex)
            self.javaInitalized = True
        else:
            print("JVM already started")

    def startGui(self):
        if not self.isInitialized():
            self.initJava()
        self.guiThread = threading.Thread(target=self.test)
        self.guiThread.setDaemon(False)
        self.guiThread.start()
        while not self.guiStarted:
            time.sleep(1)

    def isInitialized(self):
        return self.javaInitalized

    def stopJava(self):
        if self.guiStarted:
            self.stopGui()
        shutdownJVM()
        self.javaInitialized = False

    def stopGui(self):
        self.guiStarted = False
        time.sleep(1)
        self.classes.WindowManager.closeAllWindows()
        self.ijGuiInstance.quit()


    def test(self):
        attachThreadToJVM()
        self.ijGuiInstance = self.classes.ImageJ()
        self.guiStarted = True
        print('Gui started', self.ijGuiInstance)
        #detachThreadFromJVM()
        while self.guiStarted:
            if(self.ijGuiInstance.quitting() == 1):
                self.stopGui()
            time.sleep(1)