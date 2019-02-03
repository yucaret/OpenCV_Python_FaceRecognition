"""
Autor: Jorge Eduardo Vicente Hernandez
Creacion: 01-01-2019
Tema: Programa para entrenar reconocimiento de rostros
"""
from imutils import paths
import cv2
import os
import numpy as np
import json

def detect_face(image):
    # Convierte una imagen a imagen gris
    imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #imageGray = image
    
    #Cargo el detector de caras Harrcascade del OpenCV
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    #Detectamos los multiples rostros que pueden existir en la imagen que llega como parametros
    #y como resultado nos da una lista de rostros
    faces = face_cascade.detectMultiScale(imageGray, scaleFactor=1.2, minNeighbors=8);
    
    #Si el la lista no tiene rostros retorna nulo
    if (len(faces) == 0):
        return None, None
    
    #En este caso la lista solo tiene siempre un valor ya que es para entrenar cara de una persona determinada
    #Es por eso que solo utilizamos el valos primero de la lista de caras
    #Este valores contienen la coordenada x, y y tambien el ancho y largo de la cara detectada
    face = faces[0]
    (x, y, w, h) = face
    
    #retorna solo la parte de la imagen donde esta la cara y tambien el primer valor de la lista
    return imageGray[y:y+w, x:x+h], face

###############################################################################

usuarios = {}  
usuarios['usuarios'] = {}  

images = []
indexes =[]
names = []

index, indexAnt = None, None

# Metodo de reconocimiento
recognizer = cv2.face.LBPHFaceRecognizer_create()

# Paths de las imagenes
imagePaths = list(paths.list_images("dataset"))

# Variables de apoyo
cantidadImagesPaths = len(imagePaths)
caracterSeparator1 = os.path.sep
caracterSeparator2 = "_"

print("[INFO] Inicializando Loop de procesamiento de imagenes...")

# loop para cada paths de imagen
for (i, imagePath) in enumerate(imagePaths):
    
    print("[INFO] Procesando Imagen ",str(i + 1),"/",str(cantidadImagesPaths)," del Path ", imagePath)

    # Cargando las imagenes de entrenamiento
    imagefile = cv2.imread(imagePath)
    
    # Identificando el indice con el cual identificamos la imagen
    index = int(((imagePath.split(caracterSeparator1)[-1]).split(caracterSeparator2)[0]).replace("U", ""))
    print("Index: ",str(index))
    
    # Identificando el nombre
    name = imagePath.split(caracterSeparator1)[-2]
    
    # Obtenemos la imagen y el valor cara
    image, faceRect = detect_face(imagefile)
    
    print("image:",image)
    print("faceRect:",faceRect)
    
    if image is not None:
        
        imageResized = cv2.resize(image, (200,200), interpolation = cv2.INTER_AREA)
        imageNew = imageResized
        
        #agregamos la imagen de la cara a la lista de imagenes
        images.append(imageNew)
        #agregamos el indice de la imagen a la lista de indices
        indexes.append(index)
    
    # Si el index anterior es diferente al index detectado
    if index != indexAnt:
        # Si cumple la condición se agrega el diccionario de usuarios 
        usuarios['usuarios'].update({str(index): name})
        indexAnt = index

# La utpla de usuarios se guarda como un archivos json llamado usuarios.txt
with open('usuarios.txt', 'w') as outfile: json.dump(usuarios, outfile)

# Entremos nuestro modelo con las imagenes
recognizer.train(images, np.array(indexes))

# Guardamos el resultado en un archivo usuarios.yml 
recognizer.save("usuarios.yml");