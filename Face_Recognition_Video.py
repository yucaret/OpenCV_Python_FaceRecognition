"""
Autor: Jorge Eduardo Vicente Hernandez
Creacion: 02-01-2019
Tema: Programa para reconocer rostro en video
"""

from imutils.video import VideoStream
import imutils
import pickle
import time
import cv2
import json

font = cv2.FONT_HERSHEY_SIMPLEX

# Detectar Rostro
cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)

# Creamos el metodo de lectura
recognizer = cv2.face.LBPHFaceRecognizer_create() # Eigenface Recognizer
recognizer.read("usuarios.yml")

with open('usuarios.txt') as file: usuariosFile = json.load(file)


usuarios = usuariosFile['usuarios']


vs = VideoStream(src=0).start()
writer = None
time.sleep(2.0)


while True:
    
    # obtenemos la imagen del frame del video
    frame = vs.read()

    #Convertimos la imagen del frame de BGR a Gris
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
     # Lista de Caras Detectadas
    faces = faceCascade.detectMultiScale(rgb, scaleFactor=1.2, minNeighbors=8, flags = cv2.CASCADE_SCALE_IMAGE)

    # Por cada Cara Detectada
    for (x, y, w, h) in faces:
        
        # Obtenemos la imagen de la cara
        image = rgb[y: y + h, x: x + w]
        
        #Cambiamos el tamaño de la imagen a 200 por 200 
        imageResized = cv2.resize(image, (200,200), interpolation = cv2.INTER_AREA)
        imageNew = imageResized
        
        nbr_predicted, conf = recognizer.predict(imageNew)        
        
        nombre = "desconocido"
        
        if(conf < 48):
            
            colorcuadro = (0, 255, 0)
            colortexto = (255, 0, 0)
            nombre = usuarios.get(str(nbr_predicted))
            
        else:
            nbr_predicted = -1
            colorcuadro = (0, 0, 255)
            colortexto = (0, 0, 255)
        
        print("Index ",str(nbr_predicted)," is Correctly Recognized with confidence ", str(conf))
        
        cv2.putText(frame,nombre,(x,y - 50), font, 1, colortexto, 2, cv2.LINE_AA)
        cv2.putText(frame,"Conf: "+str(round(conf,5)),(x,y - 25), font, 0.5, colortexto, 2, cv2.LINE_AA)
        cv2.putText(frame,"w: "+str(w)+" h: "+str(h),(x,y - 5), font, 0.5, colortexto, 2, cv2.LINE_AA)
        cv2.rectangle(frame, (x, y), (x+w, y+h), colorcuadro , 2)
        

    # Empezando a grabar el frame del video en la ruta especificada
    if writer is None and "output/Lalo_Y_Claudia.avi" is not None:
        fourcc = cv2.VideoWriter_fourcc(*"MJPG")
        writer = cv2.VideoWriter("output/Lalo_Y_Claudia.avi", fourcc, 20, (frame.shape[1], frame.shape[0]), True)

    # Capturar la imagen del frame en el video
    if writer is not None:
        writer.write(frame)

    # Mostrar la imagen del frame como salida
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF

    # Si se escribe "q" salimos del while
    if key == ord("q"):
        break

# Destruimos todas las pantallas y cerramos
cv2.destroyAllWindows()
vs.stop()

# Se write en la ruta especificada
if writer is not None:
    writer.release()