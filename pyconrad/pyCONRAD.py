from jpype import *
import threading
import time
import os
import pyconrad.window_listener as wl
from . import __download_conrad as downloadconrad
from pathlib import Path

conradPath = 'CONRAD/src'
libPath = 'CONRAD/lib'



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

    @staticmethod
    def getInstance():
        if PyConrad._instance is None:
            PyConrad._instance = PyConrad()
        return PyConrad._instance

    def setup(self, max_ram = '8G', min_ram = '7G', devdir = ['']):
        if not self.isJavaInitalized():
            try:
                currDirectory = os.getcwd();
                conradSourceAndLibs = self.__importLibs__(devdir)
                if self.conrad_repo_path is not None:
                    os.chdir(self.conrad_repo_path)
                else:
                    os.chdir(self.__libDir)
                startJVM(getDefaultJVMPath(), conradSourceAndLibs, "-Xmx%s" % max_ram, "-Xmn%s" % min_ram )
                #os.chdir(self.__modulDir)
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

    def __importLibs__(self,devdir):
        # check whether CONRAD + RSL can be found nearby
        # yes: navigate there
        # no: use conrad.jar
        self.conrad_repo_set = False
        s = ""
        self.__modulDir = os.path.dirname(__file__)
        os.chdir(self.__modulDir)
        os.chdir('..')
        os.chdir('..')
        extra_libs=''
        dev_src = []
        for dev in devdir:
            dev_path = Path(dev)
            dev_src.append(dev_path.joinpath('src'))
            if dev_path.match("CONRAD"):
                self.conrad_repo_path = dev_path
                self.conrad_repo_set = True
                dev_lib = dev_path.joinpath('lib')
                dev_classes = dev_path.joinpath('classes', 'production', 'CONRAD')
                os.chdir(dev_path)
                extra_libs = (dev_lib.joinpath(fn) for fn in dev_lib.iterdir() if '.jar' == fn.suffix)
                extra_libs = ';'.join(map(str, [dev_classes, *extra_libs]))

        src = ';'.join(map(str,dev_src))

        if self.conrad_repo_set:
            s = f'-Djava.class.path={src};{extra_libs}'
        else:
            conrad_jar = downloadconrad.conrad_jar_fullpath()
            if not os.path.isfile(conrad_jar):
                downloadconrad.download_conrad()
            if not os.path.isfile(conrad_jar):
                raise Exception('Could not find %s' % conrad_jar)

            dev_src.append(conrad_jar)
            src = ';'.join(map(str, dev_src))
            self.__libDir = downloadconrad.conrad_jar_dir()
            s = f'-Djava.class.path={src};{extra_libs}'

        #Unix-like systems use : instead of ; to separate classpaths
        if os.name != 'nt':  # Windows
            s = s.replace(';',':')

        return s

    def terminate(self):
        shutdownJVM()
