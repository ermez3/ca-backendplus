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