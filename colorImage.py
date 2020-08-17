#* colorImage.py***************************************************************
#*                                                                            *
#*                Tratamiento de color de imágen estática                     *
#*                                                                            *
#******************************************************************************

#******************************************************************************
#*                                                                            *
#*   Registro de Revisiones:                                                  *
#*                                                                            *
#*   FECHA           RESPONSABLE         REVISION                             *
#*   -------------------------------------------------------------------------*
#*   Agosto 16/20    S. Mora Pradilla    Implementación inicial.              *
#******************************************************************************

#Librerias de opencv
import cv2


#Definicion de clase "colorImage"
class colorImage:
    #atributos de la case colorimage
    def __init__(self, path):
        self.path = path                    #Direccion de ubicación de la imágen en el directorio
        self.img = cv2.imread(self.path)    #atributo donde yace la imágen


    #Toma los valores de self.img, los convierte a escala de grises y los devuelve a self.imgGray
    def makeGray(self):
        self.imgGray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)   #pasa del formato BRG a escala de grises


    #Muestra los valores en X yY
    def displayProperties(self):
        print("\n Tamaño en eje y: ",self.img.shape[0])             #imprime la componente y (height) de la imágen
        print("\n Tamaño en eje x: ",self.img.shape[1])             #imprime la componente x (width) de la imágen
        #print("\n Canales de color: ",self.img.shape[2])           #imprime numero de canales de la imágen (depth)


    #crea una imágen esacala de rojo, azul o verde según el parámentrp "color"
    def colorizeRGB(self,color):
        self.imgGray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)   #pasa del formato BRG a escala de grises
        if color  == 'blue':
            self.imgBlue=self.img.copy()                #copia .img en .imgBlue
            self.imgBlue[:, :, 0] = self.imgGray[:, :]  #El componente azul (B) toma los valores de imgGray
            self.imgBlue[:, :, 1] = 0                   #El componente verde (G) es igualado en 0 en su totalidad
            self.imgBlue[:, :, 2] = 0                   #El componente rojo (R) es igualado en 0 en su totalidad
        elif color == 'green':
            self.imgGreen=self.img.copy()               #copia .img en .imgGreen
            self.imgGreen[:, :, 0] = 0                  #El componente azul (B) es igualado en 0 en su totalidad
            self.imgGreen[:, :, 1] = self.imgGray[:, :] #El componente verde (G) toma los valores de imgGray
            self.imgGreen[:, :, 2] = 0                  #El componente rojo (R) es igualado en 0 en su totalidad
        elif color == 'red':
            self.imgRed=self.img.copy()                 #copia .img en .imgRed
            self.imgRed[:, :, 0] = 0                    #El componente azul (B) es igualado en 0 en su totalidad
            self.imgRed[:, :, 1] = 0                    #El componente verde (G) es igualado en 0 en su totalidad
            self.imgRed[:, :, 2] = self.imgGray[:, :]   #El componente rojo (R) toma los valores de imgGray
        else:
            print ("color no valido \n ")               #mensaje de error por si no se cumplen las opciones anteriores


    #modifica la imágen con tonos aumentados
    def makeHue(self):
        self.imgBGR2HSV = cv2.cvtColor(self.img, cv2.COLOR_BGR2HSV)         #convierte de BGR a HSV y la guarda en imgBGR2HSV
        self.imgBGR2HSV[:, :, 1] = 255                                      #Componente S=255 en su totalidad
        self.imgBGR2HSV[:, :,2] = 255                                       #Componente V=255 en su totalidad
        self.imgHSV2BGR = cv2.cvtColor(self.imgBGR2HSV, cv2.COLOR_HSV2BGR)  #convierte de BGR a HSV y la guarda en imgBGR2HSV


    #muestra la imágen
    def show_Image(self, imagen, nombre):
        cv2.imshow(nombre, imagen)          #se muestra "imagen" en una ventana nombrada "nombre"
        k = cv2.waitKey(0)                  #Espera a que una tecla sea oprimida para continuar
