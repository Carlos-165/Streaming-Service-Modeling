from abc import ABC,abstractmethod

class Videos(ABC):
    def __init__(self, ID, nombre, duracion, genero, calificacion, fechaEstreno):
        self.__ID = ID
        self.__nombre = nombre
        self.__duracion = duracion
        self.__genero = genero
        self.__calificacion = calificacion
        self.__fechaEstreno = fechaEstreno
    
    @property
    def ID(self):
        return self.__ID

    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def duracion(self):
        return self.__duracion
    
    @property
    def genero(self):
        return self.__genero

    @property
    def calificacion(self):
        return self.__calificacion
    
    @property
    def fechaEstreno(self):
        return self.__fechaEstreno

    def calificar(self,calificacionUsuario):
        self.calificacionUsuario = calificacionUsuario

    @abstractmethod
    def __repr__(self):
        pass