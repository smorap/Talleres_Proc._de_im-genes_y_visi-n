#* main.py *****************************************************************
#*                                                                         *
#*                               Taller 1                                  *
#*                    Proc. de Imágenes y Visión-PUJ                       *
#***************************************************************************

#***************************************************************************
#*                                                                         *
#*   FECHA           RESPONSABLE           OBSERVACION                     *
#*   ----------------------------------------------------------------------*
#*   Agosto 16/20    S. Mora Pradilla      Implementación inicial.         *
#***************************************************************************

from colorImage import *         #llamado a la clase colorImage

#imprime solicitud de dirección de archivo
path=input("Inserte la dirección de ubicación de la imágen con el nombre y su extensiónal final")

#Constructor
imagen = colorImage(path)        #contructor de la imágen

#métodos
imagen.displayProperties()       #método que muestra las dimensiones de la imágen
imagen.makeGray()                #método que cambia la imágen original a una escala de grises
imagen.colorizeRGB('red')        #método que cambia la imágen original a una escala de rojos
imagen.makeHue()                 #método  que resalta los tonos de la imágen

#muestreo
imagen.show_Image(imagen.img,'imagen normal')            #muestra la imágen original en ventana
imagen.show_Image(imagen.imgGray,'Escala de grises')     #muestra la imágen en escala de grises en ventana
imagen.show_Image(imagen.imgRed,'Rojiza')                #muestra la imágen en escala de rojos en ventana
imagen.show_Image(imagen.imgHSV2BGR,'tonos resaltaados') #muestra la imágen con tonos resaltados

#C:\Users\marra\OneDrive\Escritorio\Proc_ Imagens\clase_2\lena.png
#C:\Users\marra\OneDrive\Escritorio\wallpapers\animu\622431.jpg


