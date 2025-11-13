import os
from pathlib import Path

def limpiar_pantalla():
    '''Limpia la pantalla de la consola'''
    os.system('cls'if os.name == 'nt' else 'clear')

def pausar_continuar():
    """Pausa el programa hasta que el usuario presione una tecla"""
    
    input("\n📝 Presiona Enter para continuar...")
    
def mostrar_bienvenida():
    """Muestra la bienvenida con información del directorio y recetas"""
    ruta_base = obtener_ruta_recetas()
    total_recetas = contar_recetas_totales(ruta_base)
    
    print("\n" + "=" * 60)
    print("        🍳 BIENVENIDO AL ADMINISTRADOR DE RECETAS 🍳")
    print("=" * 60)
    print(f"📁 Directorio de recetas: {ruta_base.absolute()}")
    print(f"📊 Recetas disponibles: {total_recetas}")
    print("=" * 60)
    

def obtener_ruta_recetas():
    """Obtiene la ruta base donde se guardan las recetas"""
    
    return Path("recetas")    

def contar_recetas_totales(ruta_base):
    """Cuenta el total de recetas en todas las categorías"""
    total = 0
    if ruta_base.exists():
        for carpeta in ruta_base.iterdir():
            if carpeta.is_dir():
                for archivo in carpeta.iterdir():
                    if archivo.is_file() and archivo.suffix == '.txt':
                        total += 1
    return total
                        
def listar_categorias(ruta_base):
    """Lista todas las categorías disponibles"""
    categorias = []
    if ruta_base.exists():
        for carpeta in ruta_base.iterdir():
            if carpeta.is_dir():
                categorias.append(carpeta.name)
    return categorias

def mostrar_categorias(categorias):
    """Muestra las categorías disponibles"""
    print("\n--- CATEGORÍAS DISPONIBLES ---")
    if categorias:
        for i, categoria in enumerate(categorias, 1):
            print(f"{i}. {categoria}")
    else:
        print("No hay categorías disponibles.")
        
def elegir_categoria(categorias):
    """Permite al usuario elegir una categoría"""
    if not categorias:
        return None
    
    while True:
        try:
            opcion = int(input("\nElige el número de la categoría: "))
            if 1 <= opcion <= len(categorias):
                return categorias[opcion - 1]
            else:
                print("❌ Opción no válida. Intenta nuevamente.")
        except ValueError:
            print("❌ Por favor, ingresa un número.")
            
def listar_recetas_en_categoria(ruta_categoria):
    """Lista todas las recetas de una categoría específica"""
    recetas = []
    if ruta_categoria.exists():
        for archivo in ruta_categoria.iterdir():
            if archivo.is_file() and archivo.suffix == '.txt':
                recetas.append(archivo.stem)  # .stem para quitar la extensión
    return recetas

def mostrar_recetas(recetas, categoria):
    """Muestra las recetas de una categoría"""
    print(f"\n--- RECETAS EN {categoria.upper()} ---")
    if recetas:
        for i, receta in enumerate(recetas, 1):
            print(f"{i}. {receta}")
    else:
        print("No hay recetas en esta categoría.")
        
def elegir_receta(recetas):
    """Permite al usuario elegir una receta"""
    if not recetas:
        return None
    
    while True:
        try:
            opcion = int(input("\nElige el número de la receta: "))
            if 1 <= opcion <= len(recetas):
                return recetas[opcion - 1]
            else:
                print("❌ Opción no válida. Intenta nuevamente.")
        except ValueError:
            print("❌ Por favor, ingresa un número.")
            
# OPCIÓN 1: Leer receta
def leer_receta():
    """Opción 1: Leer una receta específica"""
    ruta_base = obtener_ruta_recetas()
    categorias = listar_categorias(ruta_base)
    
    if not categorias:
        print("❌ No hay categorías disponibles.")
        pausar_continuar()
        return
    
    mostrar_categorias(categorias)
    categoria_elegida = elegir_categoria(categorias)
    
    if not categoria_elegida:
        pausar_continuar()
        return
    
    ruta_categoria = ruta_base / categoria_elegida
    recetas = listar_recetas_en_categoria(ruta_categoria)
    
    if not recetas:
        print("❌ No hay recetas en esta categoría.")
        pausar_continuar()
        return
    
    mostrar_recetas(recetas, categoria_elegida)
    receta_elegida = elegir_receta(recetas)
    
    if receta_elegida:
        ruta_receta = ruta_categoria / f"{receta_elegida}.txt"
        try:
            with open(ruta_receta, 'r', encoding='utf-8') as archivo:
                contenido = archivo.read()
            print(f"\n📖 RECETA: {receta_elegida}")
            print("=" * 40)
            print(contenido)
            print("=" * 40)
        except FileNotFoundError:
            print("❌ Error: La receta no se encuentra disponible.")
    
    pausar_continuar()

# OPCIÓN 2: Crear receta
def crear_receta():
    """Opción 2: Crear una nueva receta"""
    ruta_base = obtener_ruta_recetas()
    categorias = listar_categorias(ruta_base)
    
    if not categorias:
        print("❌ No hay categorías disponibles. Primero crea una categoría.")
        pausar_continuar()
        return
    
    mostrar_categorias(categorias)
    categoria_elegida = elegir_categoria(categorias)
    
    if not categoria_elegida:
        pausar_continuar()
        return
    
    ruta_categoria = ruta_base / categoria_elegida
    
    # Nombre de la nueva receta
    nombre_receta = input("\n📝 Nombre de la nueva receta: ").strip()
    if not nombre_receta:
        print("❌ El nombre no puede estar vacío.")
        pausar_continuar()
        return
    
    nombre_archivo = f"{nombre_receta.replace(' ', '_')}.txt"
    ruta_receta = ruta_categoria / nombre_archivo
    
    if ruta_receta.exists():
        print("❌ Esta receta ya existe.")
        pausar_continuar()
        return
    
    # Contenido de la receta
    print(f"\n✍️  Escribe el contenido de '{nombre_receta}':")
    print("(Presiona Enter两次 para finalizar)")
    
    lineas = []
    while True:
        linea = input()
        if linea == "" and lineas and lineas[-1] == "":
            break
        lineas.append(linea)
    
    # Quitar las dos líneas vacías finales
    contenido = "\n".join(lineas[:-1])
    
    # Guardar la receta
    try:
        with open(ruta_receta, 'w', encoding='utf-8') as archivo:
            archivo.write(contenido)
        print(f"✅ Receta '{nombre_receta}' creada exitosamente en {categoria_elegida}!")
    except Exception as e:
        print(f"❌ Error al crear la receta: {e}")
    
    pausar_continuar()

# OPCIÓN 3: Crear categoría
def crear_categoria():
    """Opción 3: Crear una nueva categoría"""
    ruta_base = obtener_ruta_recetas()
    
    nombre_categoria = input("\n📁 Nombre de la nueva categoría: ").strip()
    if not nombre_categoria:
        print("❌ El nombre no puede estar vacío.")
        pausar_continuar()
        return
    
    # Reemplazar espacios por guiones bajos para el nombre de carpeta
    nombre_carpeta = nombre_categoria.replace(' ', '_')
    ruta_categoria = ruta_base / nombre_carpeta
    
    if ruta_categoria.exists():
        print("❌ Esta categoría ya existe.")
        pausar_continuar()
        return
    
    try:
        os.makedirs(ruta_categoria)
        print(f"✅ Categoría '{nombre_categoria}' creada exitosamente!")
    except Exception as e:
        print(f"❌ Error al crear la categoría: {e}")
    
    pausar_continuar()

# OPCIÓN 4: Eliminar receta
def eliminar_receta():
    """Opción 4: Eliminar una receta"""
    ruta_base = obtener_ruta_recetas()
    categorias = listar_categorias(ruta_base)
    
    if not categorias:
        print("❌ No hay categorías disponibles.")
        pausar_continuar()
        return
    
    mostrar_categorias(categorias)
    categoria_elegida = elegir_categoria(categorias)
    
    if not categoria_elegida:
        pausar_continuar()
        return
    
    ruta_categoria = ruta_base / categoria_elegida
    recetas = listar_recetas_en_categoria(ruta_categoria)
    
    if not recetas:
        print("❌ No hay recetas en esta categoría.")
        pausar_continuar()
        return
    
    mostrar_recetas(recetas, categoria_elegida)
    receta_elegida = elegir_receta(recetas)
    
    if receta_elegida:
        ruta_receta = ruta_categoria / f"{receta_elegida}.txt"
        confirmacion = input(f"¿Estás seguro de eliminar '{receta_elegida}'? (s/n): ")
        if confirmacion.lower() == 's':
            try:
                os.remove(ruta_receta)
                print(f"✅ Receta '{receta_elegida}' eliminada exitosamente!")
            except Exception as e:
                print(f"❌ Error al eliminar la receta: {e}")
        else:
            print("❌ Eliminación cancelada.")
    
    pausar_continuar()

# OPCIÓN 5: Eliminar categoría
def eliminar_categoria():
    """Opción 5: Eliminar una categoría"""
    ruta_base = obtener_ruta_recetas()
    categorias = listar_categorias(ruta_base)
    
    if not categorias:
        print("❌ No hay categorías disponibles.")
        pausar_continuar()
        return
    
    mostrar_categorias(categorias)
    categoria_elegida = elegir_categoria(categorias)
    
    if not categoria_elegida:
        pausar_continuar()
        return
    
    ruta_categoria = ruta_base / categoria_elegida
    
    # Verificar si la categoría está vacía
    recetas = listar_recetas_en_categoria(ruta_categoria)
    if recetas:
        print("❌ No se puede eliminar: la categoría contiene recetas.")
        print("   Elimina primero todas las recetas de esta categoría.")
        pausar_continuar()
        return
    
    confirmacion = input(f"¿Estás seguro de eliminar la categoría '{categoria_elegida}'? (s/n): ")
    if confirmacion.lower() == 's':
        try:
            os.rmdir(ruta_categoria)
            print(f"✅ Categoría '{categoria_elegida}' eliminada exitosamente!")
        except Exception as e:
            print(f"❌ Error al eliminar la categoría: {e}")
    else:
        print("❌ Eliminación cancelada.")
    
    pausar_continuar()

def mostrar_menu_principal():
    """Muestra el menú principal de opciones"""
    print("\n" + "=" * 40)
    print("           MENÚ PRINCIPAL")
    print("=" * 40)
    print("1. Leer receta")
    print("2. Crear receta")
    print("3. Crear categoría")
    print("4. Eliminar receta")
    print("5. Eliminar categoría")
    print("6. Finalizar programa")
    print("=" * 40)

def ejecutar_opcion(opcion):
    """Ejecuta la opción seleccionada por el usuario"""
    if opcion == 1:
        leer_receta()
    elif opcion == 2:
        crear_receta()
    elif opcion == 3:
        crear_categoria()
    elif opcion == 4:
        eliminar_receta()
    elif opcion == 5:
        eliminar_categoria()
    elif opcion == 6:
        print("\n👋 ¡Gracias por usar el Administrador de Recetas!")
        return False
    else:
        print("❌ Opción no válida. Por favor elige una opción del 1 al 6.")
        pausar_continuar()
    
    return True

def main():
    """Función principal del programa"""
    # Inicializar directorio si no existe
    ruta_base = obtener_ruta_recetas()
    if not ruta_base.exists():
        os.makedirs(ruta_base)
        print("📁 Directorio de recetas creado.")
    
    # Bucle principal
    continuar = True
    while continuar:
        try:
            limpiar_pantalla()
            mostrar_bienvenida()
            mostrar_menu_principal()
            opcion = int(input("\nElige una opción (1-6): "))
            continuar = ejecutar_opcion(opcion)
        except ValueError:
            print("❌ Por favor, ingresa un número válido.")
            pausar_continuar()
        except KeyboardInterrupt:
            print("\n\n👋 Programa interrumpido por el usuario.")
            break

if __name__ == "__main__":
    main()