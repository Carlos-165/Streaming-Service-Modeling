import csv
from peliculas import Peliculas
from episodios import Episodios

class BaseDatos():

    def __init__(self):
        self.__ID = []
        self.__nombre = []
        self.__duracion = []
        self.__genero = []
        self.__calificacion = []
        self.__fechaEstreno = []
        self.__nombreEpisodio = []
        self.__temporada = []
        self.__numEpisodio = []
        self.__IDEpisodio = []
    
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

    def __len__(self):
        return len(self.ID)
    
    def __or__(self,other):
        if len(self) > len(other):
            return "La primera base de datos es más grande"
        elif len(self) < len(other):
            return "La segunda base de datos es más grande"
        else:
            return "Las bases de datos son de igual tamaño"

    def cargarArchivo(self, nombreArchivo):
        with open(nombreArchivo,"r",encoding="utf-8-sig") as csv_archivo:
            csv_lector = csv.DictReader(csv_archivo)
            for linea in csv_lector:
                self.ID.append(linea["ID"])
                self.nombre.append(linea["Nombre Película/Serie"])
                self.duracion.append(linea["Duración"])
                self.genero.append(linea["Género"])
                self.calificacion.append(linea["Calificación"])
                self.fechaEstreno.append(linea["Fecha Estreno"])
                self.nombreEpisodio.append(linea["Nombre Episodio"])
                self.temporada.append(linea["Temporada"])
                self.numEpisodio.append(linea["Num Episodio"])
                self.IDEpisodio.append(linea["ID Episodio"])
                self.calificacionesUsuario = [None]*len(self.ID)
        
    def buscarVideos(self,condicion):
        if isinstance(condicion, str):
            indicesPeliculas = [i for i, x in enumerate(self.genero) if (condicion in x and self.nombreEpisodio[i] == '')]
            indicesEpisodios = [i for i, x in enumerate(self.genero) if (condicion in x and self.nombreEpisodio[i] != '')]
            
            peliculasEncontradas = [Peliculas(self.ID[indicesPeliculas[i-1]],self.nombre[indicesPeliculas[i-1]],self.duracion[indicesPeliculas[i-1]],self.genero[indicesPeliculas[i-1]],self.calificacion[indicesPeliculas[i-1]],self.fechaEstreno[indicesPeliculas[i-1]]) for i in range(len(indicesPeliculas))]
            episodiosEncontrados =[Episodios(self.ID[indicesEpisodios[i-1]],self.nombre[indicesEpisodios[i-1]],self.duracion[indicesEpisodios[i-1]],self.genero[indicesEpisodios[i-1]],self.calificacion[indicesEpisodios[i-1]],self.fechaEstreno[indicesEpisodios[i-1]],self.nombreEpisodio[indicesEpisodios[i-1]],self.temporada[indicesEpisodios[i-1]], self.numEpisodio[indicesEpisodios[i-1]], self.IDEpisodio[indicesEpisodios[i-1]]) for i in range(len(indicesEpisodios))]
            videosEncontrados = peliculasEncontradas + episodiosEncontrados

            if len(videosEncontrados) > 0:
                print(f"\n  Videos Encontrados del género {condicion}:\n")
                for i, video in enumerate(videosEncontrados):
                    print("  ",i+1,video,"\n")
                return videosEncontrados
            else:
                print(f"No se encontraron videos del género {condicion}")

        else:
            print(f"\n  Videos Encontrados con calificación mínima de {condicion}:\n")    
            indicesPeliculas = [i for i, x in enumerate(self.calificacion) if (float(x) >= condicion and self.nombreEpisodio[i] == '')]
            indicesEpisodios = [i for i, x in enumerate(self.calificacion) if (float(x) >= condicion and self.nombreEpisodio[i] != '')]
            
            peliculasEncontradas = [Peliculas(self.ID[indicesPeliculas[i-1]],self.nombre[indicesPeliculas[i-1]],self.duracion[indicesPeliculas[i-1]],self.genero[indicesPeliculas[i-1]],self.calificacion[indicesPeliculas[i-1]],self.fechaEstreno[indicesPeliculas[i-1]]) for i in range(len(indicesPeliculas))]
            episodiosEncontrados =[Episodios(self.ID[indicesEpisodios[i-1]],self.nombre[indicesEpisodios[i-1]],self.duracion[indicesEpisodios[i-1]],self.genero[indicesEpisodios[i-1]],self.calificacion[indicesEpisodios[i-1]],self.fechaEstreno[indicesEpisodios[i-1]],self.nombreEpisodio[indicesEpisodios[i-1]],self.temporada[indicesEpisodios[i-1]], self.numEpisodio[indicesEpisodios[i-1]], self.IDEpisodio[indicesEpisodios[i-1]]) for i in range(len(indicesEpisodios))]
            videosEncontrados = peliculasEncontradas + episodiosEncontrados

            if len(videosEncontrados) > 0:
                print(f"\n  Videos Encontrados del género {condicion}:\n")
                for i, video in enumerate(videosEncontrados):
                    print("  ",i+1,video,"\n")
                return videosEncontrados
            else:
                print(f"No se encontraron videos con califiación mayor a {condicion}")

    def buscarPeliculas(self,condicion):

        if isinstance(condicion, str):
            print(f"\n  Películas encontradas del género {condicion}:\n")
            indices = [i for i, x in enumerate(self.genero) if (x == condicion and self.nombreEpisodio[i] == '')]
            peliculasEncontradas =  [Peliculas(self.ID[indices[i-1]],self.nombre[indices[i-1]],self.duracion[indices[i-1]],self.genero[indices[i-1]],self.calificacion[indices[i-1]],self.fechaEstreno[indices[i-1]]) for i in range(len(indices))]
            
            if len(peliculasEncontradas) > 0:
                for i, pelicula in enumerate(peliculasEncontradas):
                    print("  ",i+1,pelicula,"\n")
                return peliculasEncontradas
            else:
                print(f"No se encontraron películas del género {condicion}")

        else:
            print(f"\n  Películas encontradas con calificación mínima de {condicion}:\n")
            indices = [i for i, x in enumerate(self.calificacion) if (float(x) >= condicion and self.nombreEpisodio[i] == '')]
            peliculasEncontradas = [Peliculas(self.ID[indices[i-1]],self.nombre[indices[i-1]],self.duracion[indices[i-1]],self.genero[indices[i-1]],self.calificacion[indices[i-1]],self.fechaEstreno[indices[i-1]]) for i in range(len(indices))]
            
            if len(peliculasEncontradas) > 0:
                for i, pelicula in enumerate(peliculasEncontradas):
                    print("  ",i+1,pelicula,"\n")
                return peliculasEncontradas
            else:
                print(f"No se encontraron películas con calificación mayor o igual a {condicion}")

    def buscarEpisodios(self,condicion):
        indices = [i for i, x in enumerate(self.nombre) if x == condicion]
        episodiosEncontrados = [Episodios(self.ID[indices[i-1]],self.nombre[indices[i-1]],self.duracion[indices[i-1]],self.genero[indices[i-1]],self.calificacion[indices[i-1]],self.fechaEstreno[indices[i-1]],self.nombreEpisodio[indices[i-1]],self.temporada[indices[i-1]], self.numEpisodio[indices[i-1]], self.IDEpisodio[indices[i-1]]) for i in range(len(indices))]
        
        if len(episodiosEncontrados) > 0:
            print(f"\n  Episodios encontrados de la serie {condicion}:\n")
            for i, episodio in enumerate(episodiosEncontrados):
                print("  ",i+1,episodio,"\n")
        else:
            print(f"\n  No se encontraron episodios de la serie {condicion}")
        
        return episodiosEncontrados

    def calificarVideo(self,nombre,calificacionUsuario):
        indices1 = [i for i, x in enumerate(self.nombre) if x == nombre]
        indices2 = [i for i, x in enumerate(self.nombreEpisodio) if x == nombre]
        
        if len(indices1) == 1:
            self.calificacionesUsuario[indices1[0]] = calificacionUsuario
            videoCalificado = Peliculas(self.ID[indices1[0]],self.nombre[indices1[0]],self.duracion[indices1[0]],self.genero[indices1[0]],self.calificacion[indices1[0]],self.fechaEstreno[indices1[0]])
            videoCalificado.calificar(calificacionUsuario)
            print(f"\n  Tu califiación ha sido agregada a la siguiente película:\n")
            print("  ",videoCalificado,f", Calificación Usuario: {videoCalificado.calificacionUsuario}")
            return videoCalificado
        elif len(indices2) == 1:
            self.calificacionesUsuario[indices2[0]] = calificacionUsuario
            videoCalificado = Episodios(self.ID[indices2[0]],self.nombre[indices2[0]],self.duracion[indices2[0]],self.genero[indices2[0]],self.calificacion[indices2[0]],self.fechaEstreno[indices2[0]],self.nombreEpisodio[indices2[0]],self.temporada[indices2[0]], self.numEpisodio[indices2[0]], self.IDEpisodio[indices2[0]])
            videoCalificado.calificar(calificacionUsuario)
            print(f"\n  Tu califiación ha sido agregada al siguiente episodio:\n")
            print("  ",videoCalificado,f", Calificación Usuario: {videoCalificado.calificacionUsuario}")
            return videoCalificado
        else:
            print("\n  No existe el video") 