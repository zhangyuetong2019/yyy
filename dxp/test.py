# GRADED FUNCTION: basic_sigmoid

import math

from statsmodels.gam.tests.test_gam import sigmoid


def basic_sigmoid(x):
    """
    Compute sigmoid of x.

    Arguments:
    x -- A scalar

    Return:
    s -- sigmoid(x)
    """

    ### START CODE HERE ### (≈ 1 line of code)
    s = 1.0 / (1 + 1/ math.exp(x))
    ### END CODE HERE ###

    return  s

print ("sigmoid(3) = " + str(sigmoid(0)))


