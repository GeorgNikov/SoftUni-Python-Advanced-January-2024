from re import findall


class NameToShortError(Exception):
    """ Email username is too short. """
    pass


class MustContainAtSymbolError(Exception):
    """ (at) symbol not found """
    pass


class InvalidDomainError(Exception):
    """ Invalid domain extensions """
    pass


class MoreThanOneAtSymbol(Exception):
    """ (at) symbol is more than once """
    pass


class InvalidNameError(Exception):
    """ Invalid characters found in username """
    pass


VALID_DOMAINS = ("com", "bg", "org", "net")
MIN_NAME_SYMBOLS_COUNT = 4

pattern_name = r'\w+'

email = input()

while email != 'End':
    if email.count("@") > 1:
        raise MoreThanOneAtSymbol("Email should contain only ona @ symbol!")
    elif "@" not in email:
        raise MustContainAtSymbolError("Email must contain @")
    elif len(email.split("@")[0]) <= MIN_NAME_SYMBOLS_COUNT:
        raise NameToShortError("Name must be more than 4 characters!")
    elif email.split(".")[-1] not in VALID_DOMAINS:
        raise InvalidDomainError(f"Domain must be one of the following: {', '.join('.' + d for d in VALID_DOMAINS)}")
    elif findall(pattern_name, email.split("@")[0])[0] != email.split("@")[0]:
        raise InvalidNameError("Name must contain only letters, digits and underscores!")

    print("Email is valid")

    email = input()
