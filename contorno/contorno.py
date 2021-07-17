from cv2 import cv2

imagen=cv2.imread('Z:\PYTHON\P_ReconocimientoImagenes\contorno\contorno.jpg')

# Transformar a escalas de grises la imagen
grises  = cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)

# Implementar umbral
_, umbral = cv2.threshold(grises,100,255,cv2.THRESH_BINARY)

# Obtener lista de contornos
contornos, jerarquia = cv2.findContours(umbral,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

# Dibujar los contornos en la imagen
cv2.drawContours(imagen, contornos,-1, (65,105,225),2)

#cv2.imshow('ImgGrises',grises)
#cv2.imshow('ImgUmbral',umbral)
cv2.imshow('Img',imagen)

cv2.waitKey(0)
cv2.destroyAllWindows()