from jpype import  *
import time
import threading
import os

def run():
    try:
        os.getcwd();
        os.chdir('..')
        os.chdir("CONRAD")
        print("os.getcwd() = " + os.getcwd())

        conradloc = os.getcwd() + "\\src\\"
        s = "-Djava.class.path=" + conradloc
        
        libloc = os.getcwd() + "\\lib\\"
        ll = os.listdir(libloc)
        for i in ll:
            if ".jar" in i:
                s = s + ";" + libloc + i
        
        print("s = " + s)

        startJVM(getDefaultJVMPath(), s, "-Xmx8G", "-Xmn7G")
          
        gui = JPackage("edu").stanford.rsl.apps.gui
        gui.ReconstructionPipelineFrame.main(JArray(JString)(''))
          
        while True: time.sleep(1)
        
    except JException as ex:
        print (ex)
    
t = threading.Thread(target=run)
t.start()