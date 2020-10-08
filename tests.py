import csv
lista = []

with open("BasePelículas.csv","r",encoding="utf-8-sig") as csv_archivo:
            csv_lector = csv.DictReader(csv_archivo)
            for linea in csv_lector:
                lista.append(linea["Calificación"])


print(lista)