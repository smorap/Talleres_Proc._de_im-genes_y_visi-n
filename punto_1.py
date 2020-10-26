import cv2
import glob
import os
import json
from camera_model import *

# Criterio
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# Preparacion de puntos para dibujar
objp = np.zeros((7 * 7, 3), np.float32)
objp[:, :2] = np.mgrid[0:7, 0:7].T.reshape(-1, 2)

# Arreglos para almacenar
objpoints = []  # 3d puntos
imgpoints = []  # 2d puntos

#imagenes tomadas desde el pc
#path = 'D:/Datos/sergio/UNIVERSIDAD/2020/Proc_ Imagens/Talleres/Taller_5/Fotos_originales/'

#imagenes tomadas desde el cel
path = 'D:/Datos/sergio/UNIVERSIDAD/2020/Proc_ Imagens/Talleres/Taller_5/Fotos_orignales_cel/'

#busqueda de imagenes
path_file = os.path.join(path, 'Foto_cel_*.jpg')
images = glob.glob(path_file)

#Recorrido de imagenes para dibujar los puntos en las esquinas de cada cuadrado del tablero
for fname in images:
    img = cv2.imread(fname)
    #Re size para que la función "findCheesboardCorners"  pueda procesar las imagenes del celular
    img=cv2.resize(img,(816,408),interpolation=cv2.INTER_CUBIC)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Busqueda de las esquinas del tablero de ajedrez
    ret, corners = cv2.findChessboardCorners(gray, (7, 7), None)

    # si encontró esquinas, dibuja los puntos
    if ret == True:
        objpoints.append(objp)

        corners2 = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
        imgpoints.append(corners2)

        # dibuja y muestra las esquinas
        img = cv2.drawChessboardCorners(img, (7, 7), corners2, ret)
        cv2.imshow('img', img)
        cv2.waitKey(100)

cv2.destroyAllWindows()

#parametros de calibracion de la camara
ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)

#ver información
print(mtx)
print(dist)

# Calculo de error
mean_error = 0
for i in range(len(objpoints)):
    imgpoints2, _ = cv2.projectPoints(objpoints[i], rvecs[i], tvecs[i], mtx, dist)
    error = cv2.norm(imgpoints[i], imgpoints2, cv2.NORM_L2) / len(imgpoints2)
    mean_error += error

print("total error: {}".format(mean_error / len(objpoints)))

# correcion de distorsion
path_file = os.path.join(path, 'Foto_cel_3.jpg')
img = cv2.imread(path_file)
h, w = img.shape[:2]
newcameramtx, roi = cv2.getOptimalNewCameraMatrix(mtx, dist, (w, h), 1, (w, h))

if True:
    dst = cv2.undistort(img, mtx, dist, None, newcameramtx)
else:
    mapx, mapy = cv2.initUndistortRectifyMap(mtx, dist, None, newcameramtx, (w, h), 5)
    dst = cv2.remap(img, mapx, mapy, cv2.INTER_LINEAR)

# cmuestra imagen con y sin distorsión
x, y, w, h = roi
dst = dst[y:y + h, x:x + w]
cv2.imshow('distorted', img)
cv2.imshow('calibresult', dst)
cv2.waitKey(0)

#Creación archivos json
file_name_pc = 'calibration_pc.json'
file_name_cel = 'calibration_cel.json'
path2= r'D:\Datos\sergio\UNIVERSIDAD\2020\Proc_ Imagens\Talleres\Taller_5\Taller'
json_file = os.path.join(path2, file_name_cel)

data = {
    'K': mtx.tolist(),
    'distorsion': dist.tolist()
}
#escribir datos en los archivos json
with open(json_file_cel, 'w') as fp:
    json.dump(data, fp, sort_keys=True, indent=1, ensure_ascii=False)

########################## PUNTO 2 ############################
#Creación de archivos json para el punto 2 con calibracion de la camara del celular
file_name_json_cel_1 = 'json_cel_1.json'
file_name_json_cel_2 = 'json_cel_2.json'
path2= r'D:\Datos\sergio\UNIVERSIDAD\2020\Proc_ Imagens\Talleres\Taller_5\Taller'
json_file1 = os.path.join(path2, file_name_json_cel_1)
json_file2 = os.path.join(path2, file_name_json_cel_2)


data_1 = {
    'K': mtx.tolist(),
    'd': 2,
    'h': 1,
    'pan': 5,
    'tilt': 0
}

data_2 = {
    'K': mtx.tolist(),
    'd': 3,
    'h': 2,
    'pan': 0,
    'tilt': 30
}

with open(json_file1, 'w') as fp1:
    json.dump(data_1, fp1, sort_keys=True, indent=1, ensure_ascii=False)

with open(json_file2, 'w') as fp2:
    json.dump(data_2, fp2, sort_keys=True, indent=1, ensure_ascii=False)
