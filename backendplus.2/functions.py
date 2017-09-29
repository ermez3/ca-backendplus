def add_by(number1,number2):
    """this function return number by number"""
    try:
        return number1 * number2
    except TypeError:
        raise("Necesito un valor numerico")
    except ZeroDivisionError as err:
        raise("No puedo dividir entre 0")

def sum_by(number1,number2):    
    '''this function return number + number'''
    try:
        return number1 + number2
    except:
        raise("Cannot sum values")

def compare_value(number1,number2):
    '''this function return bool comparing two numbers'''
    try:
        if not str(number1).isnumeric():
            raise TypeError("{} is not numeric".format(number1))
        if not str(number2).isnumeric():
            raise TypeError("{} is not numeric".format(number2))

        return number1 == number2
    except:
        raise TypeError("No se proporcionaron numeros validos.")