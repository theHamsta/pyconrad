import os


def test_import():
    import pyconrad


def test_installation():
    import pyconrad

    assert os.path.exists(pyconrad.conrad_jar_dir())
    assert os.path.exists(pyconrad.conrad_jar_file())


def test_java():
    import pyconrad

    pyconrad._pyconrad.PyConrad()._check_jre_version()
