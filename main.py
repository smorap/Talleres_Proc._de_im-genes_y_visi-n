#* main.py *****************************************************************
#*                                                                         *
#*                               Taller 2                                  *
#*                    Proc. de Imágenes y Visión-PUJ                       *
#***************************************************************************

#***************************************************************************
#*                                                                         *
#*   FECHA           RESPONSABLE           OBSERVACION                     *
#*   ----------------------------------------------------------------------*
#*   Agosto 31/20    S. Mora Pradilla      Implementación inicial.         *
#***************************************************************************

from imageShape import *         #llamado a la clase imageShape

#imprime solicitud de dirección de archivo
ancho=input('Ingrese el ancho')
alto=input('ingrese el alto')
imagen=imageShape(int(ancho),int(alto))
imagen.generateShape(1,1)
imagen.showShape()
figura=imagen.whatShape(imagen.shape)
print(figura)

