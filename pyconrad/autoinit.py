import pyconrad
import pyconrad._pyconrad

if not pyconrad._pyconrad.PyConrad().is_initialized:
    pyconrad.setup_pyconrad()

if not  pyconrad._pyconrad.PyConrad().is_gui_started:
    pyconrad.start_conrad()