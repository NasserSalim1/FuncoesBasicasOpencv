import cv2

camera = cv2.VideoCapture(1)
camera.set(3, 640) # Largura
camera.set(4, 420) # Altura
camera.set(10, 200) # Brilho

while True:
    check, img = camera.read()

    cv2.imshow('Web Can', img)
    if cv2.waitKey(1) & 0xFF == ord('q'): # Código "0xFF" para ler o teclado
        break

"""

# Cortano uma imagem

img = cv2.imread('farol.jpg')
dim = cv2.selectROI("Selecione a area de recorte",img,False)
print(dim)
v1 = int(dim[0])
v2 = int(dim[1])
v3 = int(dim[2])
v4 = int(dim[3])

recorte = img[v2:v2+v4,v1:v1+v3]

cv2.imshow('Imagem', img)
cv2.imshow('Recorte',recorte)

cv2.waitKey(0)

#Abrindo vídeo

video = cv2.VideoCapture('runners.mp4')

while True:
    check, img = video.read()
    imgRedin = cv2.resize(img, (640, 420))
    cv2.imshow('video', imgRedin)
    cv2.waitKey(10)
"""

"""

#Abrindo uma imagem
    
img = cv2.imread('farol.jpg')
imgCinza = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
print(img.shape)
print(imgCinza.shape)
cv2.imshow('Imagem', img)
cv2.imshow('Imagem Cinza', imgCinza)
cv2.waitKey(0)

"""