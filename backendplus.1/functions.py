def add_by(number):
    """this function return number by number"""
    try:
        print(number / number)
    except TypeError:
        print("Necesito un valor numerico")
    except ZeroDivisionError as err:
        print("No puedo dividir entre 0")
        print(err)

add_by(0)