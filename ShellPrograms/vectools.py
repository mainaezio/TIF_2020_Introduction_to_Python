import numpy as np


def norm(x):
    """returns the magnitude of a vector x"""
    return np.sqrt(np.sum(x ** 2))


def unitvector(x):
    """returns a unit vector x/|x|. x needs to be a numpy array."""
    xnorm = norm(x)
    if xnorm == 0:
        raise ValueError("Can't normalise vector with length 0")
    return x / norm(x)


if __name__ == "__main__":
    #a little demo of how the functions in this module can be used:
    x1 = np.array([0, 1, 2])
    print("The norm of " + str(x1) + " is " + str(norm(x1)) + ".")
    print("The unitvector in the direction of " + str(x1) + " is " \
        + str(unitvector(x1)) + ".")
