import sys

from jpype import JClass

import pyconrad
import pytest
import os

@pytest.mark.skipif("CI" in os.environ and os.environ["CI"] == "true", reason="Only works if cpp file is available")
def test_pyconrad_pyconrad_example():
    """Test PyConradExample in Java"""
    sys.path.append("/home/stephan/projects/CONRAD/")

    pyconrad.setup_pyconrad(dev_dirs=["/home/stephan/projects/CONRAD/"])
    pyconrad.start_gui()

    # from edu.standford.rsl.tutorial.pyconrad import PyConradExample
    PyConradExample = JClass(
        'edu.stanford.rsl.tutorial.pyconrad.PyConradExample')
    PyConradExample.main([])


def main():
    test_pyconrad_pyconrad_example()


if __name__ == '__main__':
    main()
