# Archivos [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con archivos

import csv


def ej3():
    print('Ejercicio de archivos CSV 1º')
    archivo = 'stock.csv'
    
    # Realice un programa que abra el archivo 'stock.csv'
    # en modo lectura y cuente el stock total de tornillos
    # a lo largo de todo el archivo, 
    # sumando el stock en cada fila del archivo

    # Para eso debe leer los datos del archivo
    # con "csv.DictReader", y luego recorrer los datos
    # dentro de un bucle y solo acceder a la columna "tornillos"
    # para cumplir con el enunciado del ejercicio

    # Comenzar aquí, recuerde el identado dentro de esta funcion
    csvfile = open(archivo, 'r')
    buscar_tornillos = list(csv.DictReader(csvfile))
    
    total_tornillo = 0
    for mercaderia in buscar_tornillos:
        total_tornillo += int(mercaderia['tornillos'])

    print(total_tornillo, 'Es el nuevo saldo en el stock de tornillos')
    csvfile.close()



def ej4():
    print('Ejercicios con archivos CSV 2º')
    archivo = 'propiedades.csv'

    # Realice un programa que abra el archivo CSV "propiedades.csv"
    # en modo lectura. Recorrar dicho archivo y contar
    # la cantidad de departamentos de 2 ambientes y la cantidad
    # de departamentos de 3 ambientes disponibles.
    # Al finalizar el proceso, imprima en pantalla los resultados.

    # Tener cuidado que hay departamentos que no tienen definidos
    # la cantidad de ambientes, verifique el texto no esté vacio
    # antes de convertirlo a entero con "int( .. )"
    # NOTA: Si desea investigar puede evitar que el programa explote
    # utilizando "try except", tema que se verá la clase que viene.

    # Comenzar aquí, recuerde el identado dentro de esta funcion
    csvfile = open(archivo, 'r')
    buscar_departamentos = list(csv.DictReader(csvfile))

    total_2ambientes = 0
    total_3ambientes = 0
    cantidad_dptos = len(buscar_departamentos)

    for dptos in range(cantidad_dptos):
        row = buscar_departamentos[dptos]
        try:
            cant_ambientes = int(row.get('ambientes'))
            if cant_ambientes == 2:
                total_2ambientes += 1 
            elif cant_ambientes == 3:
                total_3ambientes += 1
        except:
            continue
    
    print('Al analizar', cantidad_dptos, 'departamentos')
    print(total_2ambientes, 'son departamentos de 2 ambientes')
    print(total_3ambientes, 'son departamentos de 3 ambientes')
    csvfile.close()

            
     
if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    ej3()
    ej4()
