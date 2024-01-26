class ValueCannotBeNegative(Exception):
    """ Raised if number is negative """
    pass




for _ in range(5):
    number = int(input())

    if number < 0:
        raise ValueCannotBeNegative