#!/usr/bin/python3


import sys


def safe_function(fct, *args):

    try:
        funct_result = fct(*args)
        return (funct_result)
    except ValueError:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
    return (None)
