
## CENTRAL ACADEMY BACKEND PLUS DIA 1 ##


# 2017-09-26
## Listas en Python
```python
#Listas map
>>> lista = [1,2,3,4,5,6,7,8,9,10]
#obtiene el objeto 
>>> map(lambda x: x*3, list)
#transforma el objeto en una lista
>>> list(map(lambda x: x*3, list))
>>> def add(number):
...     return number*3
>>> list(map(add, lista))
```
# Handling Exceptions
# Try Except Finally
# Modules / Class

__init__ no es un constructor.
Existen varias formas de inicializar un objeto ( instancia ). Puede ser desde el __init__ y no hay necesidad de agregarlo como definicion de la clase.
```python
from objects import User
```

```python
class User:
    '''Objeto user , recibe argumento name para inicializar'''
    last_name = ''
    # Init No es un constructor
    def __init__(self, name, last_name):
        self.name = name
        # propiedad privada
        self.__last_name = last_name
        self._dateAdded = ''
        self._dateAddedReadOnly = ''
    # Decoradores Set y Get donde controlas los set y get
    @property
    def date(self):
        return self._dateAdded

    @date.setter
    def date(self,value):
        print('soy un setter')
        self._dateAdded = value

    #Read Only Property
    @property
    def dateReadOnly(self):
        print('soy un get readonly')
        return self._dateAddedReadOnly

    @dateReadOnly.setter
    def dateReadOnly(self,value):
        raise NameError("ReadOnly Attribute")

    # Metodo Privado
    def __log(self):
        print('Printing log from private...')
    # Metodo Publico
    def get_last_name(self):
        print('soy un getter')
        return self.__last_name
```

Para utilizarlo:
```python
>>> import objects
>>> u = objects.User("Lalo","Cotnpaqi")
>>> u.get_last_name()
'Cotnpaqi'
>>>
```

## Herencia

Ejemplo de herencia en python:
```python
class User:
    '''Objeto user , recibe argumento name para inicializar'''
    last_name = ''
    # Init No es un constructor
    def __init__(self, name, last_name):
        self.name = name
        # propiedad privada
        self.__last_name = last_name
        self._dateAdded = ''
        self._dateAddedReadOnly = ''
    # Decoradores Set y Get donde controlas los set y get
    @property
    def date(self):
        return self._dateAdded

    @date.setter
    def date(self,value):
        print('soy un setter')
        self._dateAdded = value

    #Read Only Property
    @property
    def dateReadOnly(self):
        print('soy un get readonly')
        return self._dateAddedReadOnly

    @dateReadOnly.setter
    def dateReadOnly(self,value):
        raise NameError("ReadOnly Attribute")

    # Metodo Privado
    def __log(self):
        print('Printing log from private...')
    # Metodo Publico
    def get_last_name(self):
        print('soy un getter')
        return self.__last_name

    def get_complete_name(self):
        return "{} {}".format(self.name , self.__last_name)

class Student(User):
    '''Clase que hereda de User , recibe argumentos padre'''
    def __init__(self, name, last_name,program):
        User.__init__(self, name, last_name)
        self.program = program
    # Obtiene una representacion del objeto
    def __repr__(self):
        return self.get_complete_name()
```
__repr__ sirve para representar un objeto , es decir cuando haces referencia a el te muestra en consola lo que hayas definido en el metodo __repr__ y no la referencia a memoria.

Como lo utilizas:
```python
>>> import objects
>>> s = objects.Student("Lalo","Contpaqi","Nominas")
>>> s
Lalo Contpaqi
>>>
```