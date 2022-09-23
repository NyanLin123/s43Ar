import random
import math


def argmaxall(gen):
    """ gen is a generator of (element, value) pairs, wher value is real.
    argmaxall returns a list of all of the elements wiht maximal value."""

    maxv = -math.inf
    maxvals = []
    for (e, v) in gen:
        if v > maxv:
            maxvals.maxv = [e], v
        elif v == maxv:
            maxvals.append(e)
    return maxvals
