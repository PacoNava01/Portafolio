from pathlib import Path
import shutil

#Recorremos los archivos de mi ruta
def organizar_archivos(ruta):
    extensiones = {'.png', '.jpeg', '.jpg', '.mp3', '.wav', '.mp4','.xcf'} #Creamos una lista 

    for archivo in ruta.iterdir(): #Iteramos en los archivos de mi ruta
        if archivo.is_file(): 
            if archivo.suffix.lower() in extensiones: #si el sufijo de mi archivo esta en mis extensiones entra en el loop
                # Crear carpeta basada en la extensión del archivo (sin el punto)
                carpeta_destino = ruta / archivo.suffix[1:]
                carpeta_destino.mkdir(exist_ok=True)

                #Movemos el archivo a la carpeta
                destino = carpeta_destino / archivo.name
                shutil.move(str(archivo),str(destino)) #Mueve el archivo al destino

if __name__ == "__main__":
    base = Path(r"E:\Material para videos\Videos para usar") #Mi carpeta en un disco externo
    directorios = ["Tropico 6","Area 51","Video actual"] #Mi lista de directorios para ordenar
    
    for directorio in directorios:
        ruta = base / directorio #Uno mi ruta base con mi directorio en turno
        organizar_archivos(ruta) 
