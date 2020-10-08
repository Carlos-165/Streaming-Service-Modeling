from videos import Videos

class Episodios(Videos):
    def __init__(self,ID, nombreSerie, duracion, genero, calificacion, fechaEstreno, nombreEpisodio, temporada, numEpisodio, IDEpisodio):
        super().__init__(ID,nombreSerie, duracion, genero, calificacion, fechaEstreno)
        self.__nombreEpisodio = nombreEpisodio
        self.__temporada = temporada
        self.__numEpisodio = numEpisodio
        self.__IDEpisodio = IDEpisodio

    @property
    def nombreEpisodio(self):
        return self.__nombreEpisodio
    
    @property
    def temporada(self):
        return self.__temporada
    
    @property
    def numEpisodio(self):
        return self.__numEpisodio
    
    @property
    def IDEpisodio(self):
        return self.__IDEpisodio

    def __repr__(self):
        return f"Nombre Episodio: {self.nombreEpisodio}, ID: {self.IDEpisodio}, Duracion: {self.duracion}, Género: {self.genero}, Calificación: {self.calificacion}, Fecha de Estreno: {self.fechaEstreno}\n     Serie: {self.nombre}, Temporada: {self.temporada}, Número de Episodio: {self.numEpisodio}, ID Serie: {self.ID}"