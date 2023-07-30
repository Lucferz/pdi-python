import sys
import cv2
import numpy as np
import matplotlib.pyplot as plt

# uploaded = files.upload()

# Cambiar slash para windows a \ y usar / para linux
imagen = cv2.imread("images/onerice.bmp")

# descomentar para colab y comentar el de arriba
# imagen = imread('onerice.bmp')

# plt.imshow(imagen)
# plt.show()

cv2.imshow('Onerice', imagen)
#obtener datos de la imagen
def comoes(img):
  print('Los rasgos principales de la imagen son: ')
  # shape dice la dimension en pixeles de la imagen
  print('Dimension: ', img.shape)
  #Obtener el pixel de mayor y menor intensidad
  print('Max', np.max(img))
  print('Min', np.min(img))

comoes(imagen)

# Seleccion de la imagen considerando el primer canal

imm = imagen[:,:,0]
comoes(imm)
# Mapeo de la imagen original por el color gris
img_map_gray = cv2.applyColorMap(imm, cv2.IMREAD_GRAYSCALE)
cv2.imshow('mapeo al gris', img_map_gray)


# Segmentacion basada en umbrales
def segmentacion(x, t):
  (N,M)= x.shape
  Y = np.zeros((N,M))
  area = 0
  for i in range(N):
    for j in range(M):
      if x[i,j] > t:
        Y[i,j] = 255 #color blanco
        area = area + 1

  print('Resultado de la segmentacion: ', area)
  return Y


  # llamada a la funcion de segmentacion
#dato curioso, se debe utilizar la imagen con el primer canal, para que de resultado
# el tema es que tiene que tener mapeado al gris

imgSegmentada = segmentacion(imm, 115)
comoes(imgSegmentada)
cv2.imshow('imagen segmentada', imgSegmentada)