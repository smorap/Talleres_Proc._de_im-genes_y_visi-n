# * imageShape.py **************************************************************
# *                                                                            *
# *                          Tratamiento de cpntorno                           *
# *                                                                            *
# ******************************************************************************

# ******************************************************************************
# *                                                                            *
# *   Registro de Revisiones:                                                  *
# *                                                                            *
# *   FECHA           RESPONSABLE         REVISION                             *
# *   -------------------------------------------------------------------------*
# *   Agosto 31/20    S. Mora Pradilla    Implementación inicial.              *
# ******************************************************************************

# Librerias de opencv
import cv2
import numpy as np


# Definicion de clase "colorImage"
class imageShape:
    # CONSTRUCTOR
    def __init__(self, width, height):
        # atributos de la case imageShape
        self.width = width  # Ancho de la imagen
        self.height = height  # Alto de la imagen
        self.type = 0  # Tipo de figura en la imagen (por defecto es 0)

    # METODOS
    def generateShape(self, rand, tipe):  # genera imagen con una figura adentro y fondo negro

        self.zerosMesh = np.zeros((self.height, self.width, 3), np.uint8)  # matriz de ceros con 3 canales
        if (rand == 1):
            self.type = np.random.randint(1, 5)  # Numero generado aleatoriamente entre 1 y 4
        else:
            self.type = tipe


        if self.type == 1:  # Caso 1, triangulo
            self.lado = min(self.width, self.height) / 2  # Valor minimo de un lado para que quepa según dimensiones
            triangleH = self.lado * np.sin(np.pi / 3)  # Longitud altura del triangulo
            triangleB = self.lado * np.sin(np.pi / 6)  # Longitud Base triangulo

            pt1 = ((self.width / 2), (self.height / 2) - triangleH / 2)  # coordenada punto 1
            pt2 = ((self.width / 2) + triangleB, (self.height / 2) + triangleH / 2)  # coordenada punto 2
            pt3 = ((self.width / 2) - triangleB, (self.height / 2) + triangleH / 2)  # coordenada punto 3
            vertexTriangle = np.array([pt1, pt2, pt3])  # Lista de coordenadas de vertices

            # dibuja contorno según lista de vertices y lo rellenade color cyan
            self.shape = cv2.drawContours(self.zerosMesh, [vertexTriangle.astype(int)], 0, (227, 160, 0), -1)

        if self.type == 2:  # Caso 2, poligono de 4 caras
            self.lado = min(self.width, self.height) / 2  # Valor minimo de un lado según dimensiones
            pt1 = ((self.width / 2), (self.height / 2) + self.lado / 2)  # coordenada punto 1
            pt2 = ((self.width / 2) + self.lado / 2, (self.height / 2))  # coordenada punto 2
            pt3 = ((self.width / 2), (self.height / 2) - self.lado / 2)  # coordenada punto 3
            pt4 = ((self.width / 2) - self.lado / 2, (self.height / 2))  # coordenada punto 4
            vertexTriangle = np.array([pt1, pt2, pt3, pt4])  # Lista de coordenadas de vertices

            # dibuja contorno según lista de vertices y lo rellenade color cyan
            self.shape = cv2.drawContours(self.zerosMesh, [vertexTriangle.astype(int)], 0, (227, 160, 0), -1)

        if self.type == 3:  # Caso 3, rectangulo
            self.lado = min(self.width, self.height) / 2  # Valor minimo de un lado según dimensiones
            pt1 = ((self.width / 2) - self.lado / 1.2, (self.height / 2) + self.lado / 2)  # coordenada punto 1
            pt2 = ((self.width / 2) + self.lado / 1.2, (self.height / 2) + self.lado / 2)  # coordenada punto 2
            pt3 = ((self.width / 2) + self.lado / 1.2, (self.height / 2) - self.lado / 2)  # coordenada punto 3
            pt4 = ((self.width / 2) - self.lado / 1.2, (self.height / 2) - self.lado / 2)  # coordenada punto 4
            vertexTriangle = np.array([pt1, pt2, pt3, pt4])

            # dibuja contorno según lista de vertices y lo rellenade color cyan
            self.shape = cv2.drawContours(self.zerosMesh, [vertexTriangle.astype(int)], 0, (227, 160, 0), -1)

        if self.type == 4:  # Caso 4, circulo
            self.radio = min(self.width, self.height) / 4  # Valor radio según dimensiones

            # dibuja un circulo
            self.shape = cv2.circle(self.zerosMesh, (int(self.width / 2), int(self.height / 2)), int(self.radio),
                                    (227, 160, 0), -1)
        if self.type >= 5:  # Caso 5, circulo
            print('parametro incorrecto')

    def showShape(self):  # muestra la imagen
        if (self.type == 0):  # Caso donde no se ha generado alguna figura
            self.zerosMesh = np.zeros((self.height, self.width, 3), np.uint8)  # Matriz de ceros con 3 canales
            cv2.imshow('no imagen', self.zerosMesh)  # Se muestra una imagen en negro
            k = cv2.waitKey(5000)  # Espera 5000 milisegundos
        else:
            cv2.imshow('imagen', self.shape)  # Se muestra la figura con fondo negro
            k = cv2.waitKey(5000)  # Espera 5000 milisegundos

    def getShape(self):
        if (self.type == 0):  # Caso donde no se ha generado alguna figura
            Print('No se ha generado ninguna figura')  # Mensaje de erro
        else:
            imageGenerate = self.shape.copy()  # Copia de la imagen con figura para ser retprnada
        if (self.type == 1):  # Caso triangulo
            name = 'triangulo'
        if (self.type == 2):  # Caso square
            name = 'square'
        if (self.type == 3):
            name = 'rectangulo'  # Caso rectangulo
        if (self.type == 4):
            name = 'circle'  # Caso circulo
        return imageGenerate, name  # retorna la copia de la imagen y su nombre respectivamente

    def whatShape(self,image):
        image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)                                            #escala de grises
        ret, Ibw_image = cv2.threshold(image_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)         #umbral
        contours_image, hierarchy = cv2.findContours(Ibw_image, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE) #genera contorno
        cont_image = contours_image[0]                                                                  #contorno
        ancho=self.width                                                                                #ancho
        alto=self.height                                                                                #alto
        #Genera el diccionario para comparar un triangulo
        I_triangulo = imageShape(ancho, alto)
        I_triangulo.generateShape(0, 1)
        # Genera el diccionario para comparar un square
        I_square = imageShape(ancho, alto)
        I_square.generateShape(0, 2)
        # Genera el diccionario para comparar rectangulo
        I_rectangulo = imageShape(ancho, alto)
        I_rectangulo.generateShape(0, 3)
        # Genera el diccionario para comparar circulo
        I_circulo = imageShape(ancho, alto)
        I_circulo.generateShape(0, 4)

        # tratamiento de contonno para diccionario circulo
        circulo_gray = cv2.cvtColor(I_circulo.shape, cv2.COLOR_BGR2GRAY)
        ret, Ibw_circulo = cv2.threshold(circulo_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        contours_circle, hierarchy = cv2.findContours(Ibw_circulo, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        cont_circle = contours_circle[0]
        #compara los dos contornos y retorna un valor, entre mas pequeño sea, mas parecidos son los contornos
        value_circle = cv2.matchShapes(cont_circle, cont_image, 1, 0.0)

        # tratamiento de contonno para diccionario square
        square_gray = cv2.cvtColor(I_square.shape, cv2.COLOR_BGR2GRAY)
        ret, Ibw_square = cv2.threshold(square_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        contours_square, hierarchy = cv2.findContours(Ibw_square, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        cont_square = contours_square[0]
        # compara los dos contornos y retorna un valor, entre mas pequeño sea, mas parecidos son los contornos
        value_square = cv2.matchShapes(cont_square, cont_image, 1, 0.0)

        # tratamiento de contonno para diccionario triangulo
        triangulo_gray = cv2.cvtColor(I_triangulo.shape, cv2.COLOR_BGR2GRAY)
        ret, Ibw_triangulo = cv2.threshold(triangulo_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        contours_triangulo, hierarchy = cv2.findContours(Ibw_triangulo, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        cont_triangulo = contours_triangulo[0]
        # compara los dos contornos y retorna un valor, entre mas pequeño sea, mas parecidos son los contornos
        value_triangulo = cv2.matchShapes(cont_triangulo, cont_image, 1, 0.0)

        # tratamiento de contonno para diccionario rectangulo
        rectangulo_gray = cv2.cvtColor(I_rectangulo.shape, cv2.COLOR_BGR2GRAY)
        ret, Ibw_rectangulo = cv2.threshold(rectangulo_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        contours_rectangulo, hierarchy = cv2.findContours(Ibw_rectangulo, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        cont_triangulo = contours_rectangulo[0]
        # compara los dos contornos y retorna un valor, entre mas pequeño sea, mas parecidos son los contornos
        value_rectangulo = cv2.matchShapes(cont_triangulo, cont_image, 1, 0.0)

        #Obtener valor minimo de todas las figuras comparadas, siendo esta la que mas se asemeja a la original
        value_min=min(np.array([value_circle, value_square, value_triangulo,value_rectangulo]))
        if (value_min == value_rectangulo ):
            return 'la imagen se asemeja a un rectangulo'
        elif (value_min == value_circle ):
            return 'la imagen se asemeja a un circulo'
        elif (value_min == value_square ):
            return 'la imagen se asemeja a un square'
        elif (value_min == value_triangulo ):
            return 'la imagen se asemeja a un triangulo'