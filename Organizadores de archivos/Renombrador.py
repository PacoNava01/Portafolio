'''
Programa enfocado en ayudarme a renombrar las imagenes de algunas carpetas de mi conjuntos de datos de imagenes para segmentar en gimp posteriormente
'''

from pathlib import Path
from PIL import Image

# Usamos 'r' al inicio para que Windows lea la ruta literal sin problemas con las diagonales
'''Directorio = Path(r"G:\TESIS\Fotos segmentación\Rojo\Rojo_masks")

if Directorio.is_dir():
    print("Directorio disponible para trabajar\n")
else:
    print("Directorio no disponible para trabajar, revisa la ruta")
    exit() # Detiene el programa si la ruta está mal'''

# ----------------------------------------------------------------------------------------------------------------
def Renombrador(directorio_path, prefijo, formato):
    '''
    Funcion optimizada para renombrar archivos uno a uno sin saturar la RAM.
    '''
    contador = 1
    
    # .glob() busca solo los archivos con el formato que tú le pidas (ej. ".jpg")
    # Usar el generador asegura memoria O(1)
    for elemento in directorio_path.glob(f"*{formato}"):
        
        # 1. Creamos el nuevo nombre (Muy bien pensado el uso de zfill!)
        nombre_nuevo = f"{prefijo}_{str(contador).zfill(3)}{formato}"
        
        # 2. Definimos la ruta completa con el nuevo nombre
        nueva_ruta = elemento.with_name(nombre_nuevo)
        
        # 3. Validamos para evitar conflictos si el archivo ya se llama así
        if elemento == nueva_ruta:
            contador += 1
            continue
            
        try:
            # 4. Ejecutamos el renombrado
            elemento.rename(nueva_ruta)
            print(f"Renombrado: {elemento.name} -> {nombre_nuevo}")
            contador += 1
            
        except Exception as e:
            print(f" No se pudo renombrar {elemento.name}: {e}")
            
    print("\n Proceso de renombrado finalizado con éxito.")
# ----------------------------------------------------------------------------------------------------------------

def comprobador(Directorio_path):
    #Iteramos directamente sobre el generador para no saturar la memoria RAM con listas no tan necesarias
    for archivo in Directorio_path.glob("*.jpg"):
         try:
            with Image.open(archivo) as img:
                ancho,alto = img.size

                if ancho != 640 or alto != 640:
                    print(f"{archivo.name} Incorrecto ({ancho}x{alto})")
    
         except Exception as e:
             print(f"No se pudo leer el archivo {archivo.name}: {e}")

Directorio = Path(r"G:\TESIS\Fotos segmentación\Azul")

if __name__ == '__main__':
    Renombrador(Directorio,prefijo= "azul",formato= ".jpg")
    #comprobador(Directorio)