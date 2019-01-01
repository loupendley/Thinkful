def check_equality(a, b):
    """Asserts the equivalent of the two passed objects.

    :param a: First object.
    :param b: Second object.
    :return: Indicates if assertion was successful.
    """
    try:
        Logging.line_separator("ASSERTING EQUIVALENCE OF...")
        # Output objects using __str__ method.
        Logging.log(a)
        Logging.log(b)
        # Assert equivalence of objects, indicating inequality if failed.
        assert a == b, "The objects ARE NOT equal."
        # Indicate that assertion succeeded.
        Logging.log("The objects are equal.")
        return True
    except AssertionError as error:
        # Output expected AssertionErrors.
        Logging.log_exception(error)
    except Exception as exception:
        # Output unexpected Exceptions.
        Logging.log_exception(exception, False)


def fncheck(a, b):
    try:
        assert a == b, "The objects ARE NOT equal."
        print('the objects a, and b are equal')
        return True
    except AssertionError as error:
        print('zoog objects a, and b are not equal')
        return False
    except:
        print('objects a, and b are not equal')
        return False

a = 2
b = 2000
print('do a and b match? {}'.format(fncheck(a,b)))
