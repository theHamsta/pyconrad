import warnings
import pyconrad
import time
import pyconrad


def test_basic_example():
    import pyconrad_examples.first_steps._1_basic_example
    pyconrad.ij().WindowManager.closeAllWindows()
    return


def test_numpy_example():
    import pyconrad_examples.first_steps._3_numpy_and_conrad
    pyconrad.ij().WindowManager.closeAllWindows()
    return


if __name__ == "__main__":
    test_basic_example()
    # test_numpy_example()
