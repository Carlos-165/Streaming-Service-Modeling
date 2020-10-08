from videos import Videos

class Peliculas(Videos):
    def __init__(self,ID, nombre, duracion, genero, calificacion, fechaEstreno):
        super().__init__(ID,nombre, duracion, genero, calificacion, fechaEstreno)

    def __repr__(self):
        return f"Nombre Película: {self.nombre}, ID: {self.ID}, Duracion: {self.duracion}, Género: {self.genero}, Calificación: {self.calificacion}, Fecha de Estreno: {self.fechaEstreno}"