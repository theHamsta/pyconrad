from jpype import *

class PyIJ:
    "ImageJ Gui wraped in python"
    javaInitalized = None
    guiStarted = None
    classes = None
    ijGuiInstance = None

    def initJava(self):
        if not self.isInitialized():
            try:
                startJVM(getDefaultJVMPath(), "-ea", "-Djava.class.path=lib\\ij.jar")
                print("JVM Started(main): ", isJVMStarted())
                self.classes = JPackage('ij')
            except JException as ex:
                print(ex)
            self.javaInitalized = True
        print("JVM already started")

    def startGui(self):
        if not self.isInitialized():
            self.initJava()
        self.ijGuiInstance = self.classes.ImageJ()
        self.guiStarted = True
        print('Gui started',self.ijGuiInstance)

    def isInitialized(self):
        return self.javaInitalized

    def stopJava(self):
        if self.guiStarted:
            self.stopGui()
        shutdownJVM()
        self.javaInitialized = False

    def stopGui(self):
        self.classes.WindowManager.closeAllWindows()
        self.ijGuiInstance.quit()
        self.guiStarted = False