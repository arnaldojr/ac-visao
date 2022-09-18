#!/usr/bin/python
# -*- coding: utf-8 -*-

# Programa simples com camera webcam e opencv

import cv2
import os,sys, os.path
import numpy as np
min_contrast = 150
max_contrast = 250
kernel = np.ones((3,3),np.uint8)


def processa_imagem(img):
    """
    a imagem da webcam é processada aqui. 
    """
    img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    edges = cv2.Laplacian(img, cv2.CV_8U, ksize=5)
    ret, mask = cv2.threshold(edges, 100, 255, cv2.THRESH_BINARY_INV)
    


    return mask


# Define a webcam para captura de video, normalmente 0, mas pode ser 1,2...
vc = cv2.VideoCapture(2)

# testa se a camera esta funcionando.
if vc.isOpened(): 
    rval, frame = vc.read()    # captura um frame de video
else:
    rval = False

# loop infinito do programa.
while rval:
    
    # chama a função que vai processar a imagem.
    img = processa_imagem(frame)

    # Exibe a imagem após o processamento.
    cv2.imshow("img", img)
    cv2.imshow("preview", frame)
    # captura o proximo frame de video.
    rval, frame = vc.read()
    key = cv2.waitKey(20)
    if key == 27: # aperte ESC para fechar o programa
        break

cv2.destroyWindow("preview")
vc.release()