# Alumno : Carlos David Toapanta Noroña
# Matricula : A01657439

from baseDatos import BaseDatos

class Aplicacion:
    def start(self):
        a = BaseDatos()

        while True:
            print("--" * 15)
            try:
                self.input = int(input("1. Cargar archivos a la base de datos\n"
                               "2. Mostrar videos por genero o calificacion\n"
                               "3. Mostrar episiodios de una serie\n"
                               "4. Mostrar peliculas con cierta calificacion\n"
                               "5. Calificar video\n"
                               "6. Comparar con otra base de datos\n"
                               "7. Salir\n"
                               "¿Que deseas hacer?: "))

                if self.input == 1:
                    nombreArchivo = input("Escribe el nombre de tu archivo csv: ")
                    a.cargarArchivo(nombreArchivo)
                    print(f"\n  Tu base de datos tiene {len(a)} videos")
    
                elif self.input == 2:
                    tipoBusqueda = int(input("Si deseas buscar por género digita 1, o si quieres buscar por calificación digita 2: "))

                    if tipoBusqueda == 1:
                        condicion = input("Escribe el género: ")
                        a.buscarVideos(condicion)
                    elif tipoBusqueda == 2:
                        condicion = float(input("Escribe la calificación mínima deseada (Se aceptan valores entre 0 y 10): "))
                        a.buscarVideos(condicion)
                    else:
                        raise ValueError
    
                elif self.input == 3:
                    serie = input("Escribe el nombre de la serie: ")
                    a.buscarEpisodios(serie)
                
                elif self.input == 4:
                    calificacion = float(input("Digita la calificación mínima deseada (Se aceptan valores entre 0 y 10): "))
                    if calificacion >= 0 and calificacion <=10:
                        a.buscarPeliculas(calificacion)
                    else:
                        raise ValueError
    
                elif self.input == 5:
                    video = input("Escribe el nombre del video a calificar: ")
                    calificacion = float(input("Digita tu calificación (Se aceptan valores entre 0 y 10): "))
                    a.calificarVideo(video,calificacion)

                elif self.input == 6:
                    nuevoArchivo = input("Escribe el nombre de tu segundo archivo csv: ")
                    b = BaseDatos()
                    b.cargarArchivo(nuevoArchivo)
                    print("\n  ",a|b)

                elif self.input == 7:
                    print("Hasta pronto")
                    break
                
                else:
                    print("Ese numero no está entre las opciones")

            except ValueError:
                print("\n  No se reconoce la entrada, vuelve a intentarlo")
            except FileNotFoundError:
                print("\n  El archivo sellecionado no existe")
            except Exception:
                print("\n  El archivo no es compatible")

if __name__ == "__main__":
    streaming = Aplicacion()
    streaming.start()