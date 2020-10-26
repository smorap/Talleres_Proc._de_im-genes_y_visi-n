import cv2
import json
import os
from camera_model import *

if __name__ == '__main__':
    #lectura datos en archivos json
    file_name_json_cel_1 = 'json_cel_1.json'
    file_name_json_cel_2 = 'json_cel_2.json'
    path2 = r'D:\Datos\sergio\UNIVERSIDAD\2020\Proc_ Imagens\Talleres\Taller_5\Taller'
    json_file1 = os.path.join(path2, file_name_json_cel_1)
    json_file2 = os.path.join(path2, file_name_json_cel_2)

    with open(json_file1) as fp:
        json_data1 = json.load(fp)

    with open(json_file2) as fp:
        json_data2 = json.load(fp)


    # Parámetros intrínsecos json1
    width = 816
    height = 408
    K1 = np.array(json_data1['K']).reshape(3,3)

    # Parámetros intrínsecos json2
    K2 = np.array(json_data2['K']).reshape(3,3)

    # Parámetros extrínsecos json1
    d1 = json_data1['d']
    h1 = json_data1['h']
    tilt1 = json_data1['tilt']
    pan1 = json_data1['pan']
    R1 = set_rotation(tilt1, pan1, 0)
    t1 = np.array([0,-d1, h1])


    # Parámetros extrínsecos  json2
    d2 = json_data2['d']
    h2 = json_data2['h']
    tilt2 = json_data2['tilt']
    pan2 = json_data2['pan']
    R2 = set_rotation(tilt2, pan2, 0)
    t2 = np.array([0,-d2, h2])

    # creación camara 1 y 2
    camera1 = projective_camera(K1, width, height, R1, t1)
    camera2 = projective_camera(K2, width, height, R2, t2)

    #Coordenadas esquinas cubito 1
    L = 0.4
    cubito_3D = np.array([[L, L, 0], [L, -L, 0], [-L, -L, 0], [-L, L, 0],
                            [L, L, L], [L, -L, L], [-L, -L, L], [-L, L, L]])
    cubito_2D_1 = projective_camera_project(cubito_3D, camera1)

    #Dibuja los lados del cubito 1
    image_projective_1 = 255 * np.ones(shape=[camera1.height, camera1.width, 3], dtype=np.uint8)
    cv2.line(image_projective_1, (cubito_2D_1[0][0], cubito_2D_1[0][1]), (cubito_2D_1[1][0], cubito_2D_1[1][1]),
             (200, 1, 255), 3)
    cv2.line(image_projective_1, (cubito_2D_1[1][0], cubito_2D_1[1][1]), (cubito_2D_1[2][0], cubito_2D_1[2][1]),
             (200, 1, 255), 3)
    cv2.line(image_projective_1, (cubito_2D_1[2][0], cubito_2D_1[2][1]), (cubito_2D_1[3][0], cubito_2D_1[3][1]),
             (200, 1, 255), 3)
    cv2.line(image_projective_1, (cubito_2D_1[3][0], cubito_2D_1[3][1]), (cubito_2D_1[0][0], cubito_2D_1[0][1]),
             (200, 1, 255), 3)

    cv2.line(image_projective_1, (cubito_2D_1[0][0], cubito_2D_1[0][1]), (cubito_2D_1[4][0], cubito_2D_1[4][1]),
             (200, 1, 255), 3)
    cv2.line(image_projective_1, (cubito_2D_1[1][0], cubito_2D_1[1][1]), (cubito_2D_1[5][0], cubito_2D_1[5][1]),
             (200, 1, 255), 3)
    cv2.line(image_projective_1, (cubito_2D_1[2][0], cubito_2D_1[2][1]), (cubito_2D_1[6][0], cubito_2D_1[6][1]),
             (200, 1, 255), 3)
    cv2.line(image_projective_1, (cubito_2D_1[3][0], cubito_2D_1[3][1]), (cubito_2D_1[7][0], cubito_2D_1[7][1]),
             (200, 1, 255), 3)

    cv2.line(image_projective_1, (cubito_2D_1[4][0], cubito_2D_1[4][1]), (cubito_2D_1[5][0], cubito_2D_1[5][1]),
             (200, 1, 255), 3)
    cv2.line(image_projective_1, (cubito_2D_1[5][0], cubito_2D_1[5][1]), (cubito_2D_1[6][0], cubito_2D_1[6][1]),
             (200, 1, 255), 3)
    cv2.line(image_projective_1, (cubito_2D_1[6][0], cubito_2D_1[6][1]), (cubito_2D_1[7][0], cubito_2D_1[7][1]),
             (200, 1, 255), 3)
    cv2.line(image_projective_1, (cubito_2D_1[7][0], cubito_2D_1[7][1]), (cubito_2D_1[4][0], cubito_2D_1[4][1]),
             (200, 1, 255), 3)

    cv2.imshow("Image_cubito_1", image_projective_1)
    cv2.waitKey(5000)

    #Coordenadas esquinas cubito 2
    cubito_2D_2 = projective_camera_project(cubito_3D, camera2)

    # Dibuja los lados del cubito 2
    image_projective_2 = 255 * np.ones(shape=[camera2.height, camera2.width, 3], dtype=np.uint8)
    cv2.line(image_projective_2, (cubito_2D_2[0][0], cubito_2D_2[0][1]), (cubito_2D_2[1][0], cubito_2D_2[1][1]),
             (200, 1, 255), 3)
    cv2.line(image_projective_2, (cubito_2D_2[1][0], cubito_2D_2[1][1]), (cubito_2D_2[2][0], cubito_2D_2[2][1]),
             (200, 1, 255), 3)
    cv2.line(image_projective_2, (cubito_2D_2[2][0], cubito_2D_2[2][1]), (cubito_2D_2[3][0], cubito_2D_2[3][1]),
             (200, 1, 255), 3)
    cv2.line(image_projective_2, (cubito_2D_2[3][0], cubito_2D_2[3][1]), (cubito_2D_2[0][0], cubito_2D_2[0][1]),
             (200, 1, 255), 3)

    cv2.line(image_projective_2, (cubito_2D_2[0][0], cubito_2D_2[0][1]), (cubito_2D_2[4][0], cubito_2D_2[4][1]),
             (200, 1, 255), 3)
    cv2.line(image_projective_2, (cubito_2D_2[1][0], cubito_2D_2[1][1]), (cubito_2D_2[5][0], cubito_2D_2[5][1]),
             (200, 1, 255), 3)
    cv2.line(image_projective_2, (cubito_2D_2[2][0], cubito_2D_2[2][1]), (cubito_2D_2[6][0], cubito_2D_2[6][1]),
             (200, 1, 255), 3)
    cv2.line(image_projective_2, (cubito_2D_2[3][0], cubito_2D_2[3][1]), (cubito_2D_2[7][0], cubito_2D_2[7][1]),
             (200, 1, 255), 3)

    cv2.line(image_projective_2, (cubito_2D_2[4][0], cubito_2D_2[4][1]), (cubito_2D_2[5][0], cubito_2D_2[5][1]),
             (200, 1, 255), 3)
    cv2.line(image_projective_2, (cubito_2D_2[5][0], cubito_2D_2[5][1]), (cubito_2D_2[6][0], cubito_2D_2[6][1]),
             (200, 1, 255), 3)
    cv2.line(image_projective_2, (cubito_2D_2[6][0], cubito_2D_2[6][1]), (cubito_2D_2[7][0], cubito_2D_2[7][1]),
             (200, 1, 255), 3)
    cv2.line(image_projective_2, (cubito_2D_2[7][0], cubito_2D_2[7][1]), (cubito_2D_2[4][0], cubito_2D_2[4][1]),
             (200, 1, 255), 3)

    cv2.imshow("Image_cubito_2", image_projective_2)
    cv2.waitKey(0)

    cv2.imwrite(os.path.join(path2, 'Cubito_1.jpg'),image_projective_1)
    cv2.imwrite(os.path.join(path2, 'Cubito_2.jpg'), image_projective_2)


