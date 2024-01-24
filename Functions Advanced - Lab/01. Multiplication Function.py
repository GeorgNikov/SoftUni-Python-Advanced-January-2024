# import numpy
#
#
# def multiply(*args):
#     return numpy.prod(args)
#

def multiply(*args):

    if len(args) == 0:
        return 0

    result = 1
    for arg in args:
        result *= arg
    return result

print(multiply())