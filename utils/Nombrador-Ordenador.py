'''
Script que a partir de un directorio renombra las imágenes en un directorio con el formato imagen(Número)
manteniendo su extensión original, y luego dividirlas en dos carpetas llamadas Train y Val en una proporción
configurable (por ejemplo, 80% para entrenamiento y 20% para validación).
'''

import os
import shutil
import random

Directorio = "D:\\Data\\Carros"

def organizar_imagenes(directorio, ratio_train=0.8):
    # Crear carpetas Train y Val dentro del directorio
    train_dir = os.path.join(directorio, "Train")
    val_dir = os.path.join(directorio, "Val")
    os.makedirs(train_dir, exist_ok=True)
    os.makedirs(val_dir, exist_ok=True)

    # Extensiones válidas
    extensiones_validas = [".jpg", ".jpeg", ".png"]

    # Listar imágenes en el directorio
    imagenes = [f for f in os.listdir(directorio) 
                if os.path.splitext(f)[1].lower() in extensiones_validas]

    # Mezclar aleatoriamente las imágenes
    random.shuffle(imagenes)

    # Renombrar imágenes con formato imagen(Número)
    imagenes_renombradas = []
    for i, nombre in enumerate(imagenes, start=1):
        extension = os.path.splitext(nombre)[1]
        nuevo_nombre = f"imagen({i}){extension}"
        ruta_original = os.path.join(directorio, nombre)
        ruta_nueva = os.path.join(directorio, nuevo_nombre)
        os.rename(ruta_original, ruta_nueva)
        imagenes_renombradas.append(nuevo_nombre)

    # Dividir en Train y Val según el ratio
    total = len(imagenes_renombradas)
    limite_train = int(total * ratio_train)

    for i, nombre in enumerate(imagenes_renombradas):
        origen = os.path.join(directorio, nombre)
        destino = os.path.join(train_dir if i < limite_train else val_dir, nombre)
        shutil.move(origen, destino)

    print(f"Proceso completado: {limite_train} imágenes en Train y {total - limite_train} en Val.")

# Ejemplo de uso:
organizar_imagenes(Directorio, ratio_train=0.8)
