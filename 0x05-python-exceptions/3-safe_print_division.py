#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    except (ValueError, TypeError):
        result =  None
    else:
        return result
    finally:
        print("Inside result: {}".format(result))
