import numpy as np
import cv2

def generar_simulador():
     # Configuración de la pantalla virtual donde rebotará nuestro objeto
     width, height = 800, 600
     nombre_ventana = "Simulador de seguimiento"
     cv2.namedWindow(nombre_ventana, cv2.WINDOW_AUTOSIZE)

     # Definición del color que queremos que tenga nuestro objeto (BGR)
     color_list = {
          "rojo" : (0, 0, 255),
          "rojo_claro" : (193, 16, 7),   
          "rojo_oscuro" : (128, 24, 5),
     }

     # Parámetros del polígono (un hexágono regular)
     radio_poligono = 40
     puntos_base = []

     for i in range(4):
          angulo = i * (np.pi / 2)
          x = int(radio_poligono * np.cos(angulo))
          y = int(radio_poligono * np.sin(angulo))
          puntos_base.append([x, y])
     puntos_base = np.array(puntos_base, dtype=np.int32)

     # Posición inicial del centro del polígono
     pos_x, pos_y = width // 2, height // 2

     # Velocidad de desplazamiento inicial en píxeles por frame
     vel_x, vel_y = 5, 2

     print("Simulador iniciado. Presiona 'Enter' o 'Esc' en la ventana para cerrar.")

     while True:
          # CORRECCIÓN: Matriz de 3 canales (Color) y dimensiones correctas (alto, ancho, canales)
          pantalla = np.zeros((height, width, 3), dtype=np.uint8)

          # Actualizamos la posición con física de rebote
          pos_x += vel_x
          pos_y += vel_y

          # Rebote en bordes laterales
          if pos_x - radio_poligono <= 0 or pos_x + radio_poligono >= width:
               vel_x = -vel_x
               pos_x += vel_x
          if pos_y - radio_poligono <= 0 or pos_y + radio_poligono >= height:
               vel_y = -vel_y
               pos_y += vel_y
               
          # Trasladar los puntos base del polígono a la posición actual
          puntos_transformados = puntos_base + [pos_x, pos_y]

          # Dibujar el polígono relleno a color
          cv2.fillPoly(pantalla, [puntos_transformados], color_list["rojo"])

          # Mostrar el frame en la pantalla
          cv2.imshow(nombre_ventana, pantalla)

          # Control de FPS (aprox 60 FPS con 16ms de espera)
          tecla = cv2.waitKey(16) & 0xFF
          if tecla == 13 or tecla == 27:
               break
               
     # CORRECCIÓN: Indentación alineada con el bloque de la función
     cv2.destroyAllWindows()
     
if __name__ == "__main__":
     generar_simulador()