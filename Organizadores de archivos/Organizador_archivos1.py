import matplotlib.pyplot as plt
import os
import numpy as np
import cv2

Archive_types = ['.png','.jpeg','.jpg','.mp3','.wav', '.mp4']
Carpetas = ['png','jpeg','jpg','mp3','wav','mp4']

os.chdir("E:\Material para videos\Videos para usar\Area 51")

print(os.getcwd())
contenido = os.listdir() #Asignamos una lista con los contenidos del directiorio a pulir
print(contenido)

#Mostramos una imagen de la lista de contenidos
#img=cv2.imread(contenido[0])
#plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
#plt.show()

agrupados = {tipo: [] for tipo in Archive_types} 

print(f"\n{agrupados}")

'''
Creamos diccionario donde cada clave es 
el nombre de la carpeta a la cual sera 
asignado el objeto
'''
for archivo in contenido: #itera entre los contenidos de la carpeta
    for tipo in Archive_types: #Itera entre los tipos de archivos que definimos
        if archivo.endswith(tipo):
            '''
            Si el archivo\contenido de la carpeta termina con 
            el tipo dde archivo en turno se almaacena el valor 
            en el diccionario

            Primera iteración:
            -> archivo = '323392.png'
                -> tipo de archivo = 'png'
                    -> 'archivo' termina con 'tipo de archivo'? SI
                        -> almacena 'archivo' en la clave tipo de archivo
            Segunda iteración:
                -> tipo de archivo = 'jpeg'
                    -> ....
            '''
            agrupados[tipo].append(archivo)

print(f"\n{agrupados}\n")

#Agrupados los archivos en un diccionario los podemos pasar a una carpeta
for tipo, archivos in agrupados.items():
    carpeta = tipo.replace('.','') # Pasamos de '.png' a 'png'

    if not os.path.exists(carpeta):
        os.mkdir(carpeta)

    for archivo in archivos:
        os.rename(archivo,os.path.join(carpeta,archivo))

