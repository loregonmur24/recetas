#importar modulos

import os
from pathlib import Path
from os import system

# Mostrar la ruta

mi_ruta = Path(Path.home(), "Documents", "Programacion", "Python", "Dia 6", "Recetas")

# Cuantas recetas hay

def contar_recetas(ruta):
    
    contador = 0
    
    for txt in Path(ruta).glob("**/*.txt"):
        
        contador+=1
    
    return contador

# Menu inicio

def inicio():
    system("cls")
    print("-------- Bienvenido al menu de inico de recetas -------")
    print("\n")
    
    print(f"Las recetas se encuentran en {mi_ruta} \n")
    print(f"Total de recetas: {contar_recetas(mi_ruta)} \n")
    
    eleccion_menu = "x"
    
    while not eleccion_menu.isnumeric() or int(eleccion_menu) not in range(1,7):
        print("Elige una opcion")
        print('''
              
              {1} - Leer receta
              {2} - Crear receta nueva
              {3} - Crear categoria nueva
              {4} - Eliminar receta
              {5} - Eliminar categora
              {6} - Salir del programa...
              
              ''')
        eleccion_menu = input()
    return int(eleccion_menu)
    
#mostrar categorias

def mostrar_categorias(ruta):
    print("Categorias: ")
    ruta_categorias = Path(ruta)
    lista_categorias=[]
    contador = 1
    
    for carpeta in ruta_categorias.iterdir():
        carpeta_str = str(carpeta.name)
        print(f"[{contador}] - {carpeta_str}")
        lista_categorias.append(carpeta)
        contador += 1
        
    return lista_categorias
        

# elegir categorias

def elegir_categoria(lista):
    eleccion_correcta ="x"
    
    while not eleccion_correcta.isnumeric() or int(eleccion_correcta) not in range(1,len(lista) + 1):
        eleccion_correcta = input("\n Elige una categoria: ")
        
    return lista[int(eleccion_correcta) - 1]

# mostrat recetas
def mostrar_recetas(ruta):
    print("Recetas exsitentes: ")
    ruta_recetas = Path(ruta)
    lista_recetas=[]
    contador = 1
    
    for receta in ruta_recetas.glob("*.txt"):
        receta_str = str(receta.name)
        print(f"[{contador}] - {receta_str}")
        lista_recetas.append(receta)
        contador +=1
        
    return lista_recetas

# elegir recetas funcion

def elegir_recetas(lista):
    eleccion_receta="x"
    
    while not eleccion_receta.isnumeric() or int(eleccion_receta) not in range(1,len(lista) + 1):
        eleccion_receta = input("\n elige una receta: ")
    return lista[int(eleccion_receta) - 1]
    
    
def leer_receta(receta):
    print(receta.read_text())  # CORREGIDO

def crear_receta(ruta):
    existe = False
    while not existe:
        print("Escribe el nombrede tu receta: ")
        nombre_receta = input() + ".txt"
        print("Escribe tu nueva receta: ")
        contenido_receta = input()
        ruta_nueva = Path(ruta, nombre_receta)
        
        if not os.path.exists(ruta_nueva):  # CORREGIDO: exists en lugar de exist
            ruta_nueva.write_text(contenido_receta)  # CORREGIDO
            print(f"Tu receta {nombre_receta} ha sido creada ")
            existe = True
        else:
            print("Lo siento, esta receta ya existe")
            
def crear_categoria(ruta):  # CORREGIDO: agregado parámetro ruta
    existe = False
    while not existe:
        print("Escribe el nombrede tu categoria: ")
        nombre_categoria = input()
        ruta_nueva = Path(ruta, nombre_categoria)
        
        if not os.path.exists(ruta_nueva):  # CORREGIDO: exists en lugar de exist
            Path.mkdir(ruta_nueva)
            print(f"Tu nueva categoria {nombre_categoria} ha sido creada ")
            existe = True
        else:
            print("Lo siento, esta categoria ya existe")
            

def eliminar_receta(receta):
    Path(receta).unlink()
    print (f"La receta {receta.name} ha sido eliminada")
    
def eliminar_categoria(categoria):
    # Verificar si la categoría está vacía antes de eliminar
    categoria_path = Path(categoria)
    if categoria_path.exists() and categoria_path.is_dir():
        # Verificar si la categoría está vacía
        if not any(categoria_path.iterdir()):
            categoria_path.rmdir()
            print(f"La categoria {categoria.name} ha sido eliminada")
        else:
            print(f"No se puede eliminar la categoría {categoria.name} porque no está vacía")
    else:
        print("La categoría no existe o no es un directorio")

def volver_inicio():
    eleccion_regresar = "x"
    
    while eleccion_regresar.lower() != "y":
        eleccion_regresar = input("\n Presione y para volver al menu: ")


finalizar_programa = False

while not finalizar_programa:

    menu = inicio()

    if menu == 1:
        #mostrar categoriasn
        mis_categorias = mostrar_categorias(mi_ruta)
        #elegir categoria
        mi_categoria = elegir_categoria(mis_categorias)
        #mostrar recetas    
        mis_recetas = mostrar_recetas(mi_categoria)
        #elegir recetas
        mi_receta = elegir_recetas(mis_recetas)
        #leer la receta
        leer_receta(mi_receta)
        #volver al inicio
        volver_inicio()
    

    elif menu == 2:
        #mostrar categoriasn
        mis_categorias = mostrar_categorias(mi_ruta)
        #elegir categoria
        mi_categoria = elegir_categoria(mis_categorias)
        #crear una receta nueva
        crear_receta(mi_categoria)
        #volver al inc+icio
        volver_inicio()
    
    

    elif menu == 3:
        #crear categoria - CORREGIDO: agregado mi_ruta como parámetro
        crear_categoria(mi_ruta)
        #volver al inico
        volver_inicio()
    
        


    elif menu== 4:
        #mostrar categorias
        
        mis_categorias = mostrar_categorias(mi_ruta)
        #elegir categoria
        mi_categoria = elegir_categoria(mis_categorias)
        #mostrar recetas
        mis_recetas = mostrar_recetas(mi_categoria)
        #leer la recetas
        mi_receta = elegir_recetas(mis_recetas)
        #eliminar recetas
        eliminar_receta(mi_receta)
        #volver al inicio
        volver_inicio()
        

    elif menu == 5:
        #mostrar categorias
        mis_categorias = mostrar_categorias(mi_ruta)
        #elegir categoria
        mi_categoria = elegir_categoria(mis_categorias)
        #eliminar la categoria
        eliminar_categoria(mi_categoria)
        #volver al inicio
        volver_inicio()
        

    elif menu == 6:
        #finalizar programa
        finalizar_programa = True