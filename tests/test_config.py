"""

"""

import pyconrad.autoinit


def test_get_projection_matrices():
    import pyconrad.config
    matrices = pyconrad.config.get_projection_matrices()
    for m in matrices:
        print(m)


def main():
    test_get_projection_matrices()


if __name__ == '__main__':
    main()
