# Codigo Fuente para Reconocimiento Facial con Python y OpenCv


## Requerimientos

- Python 3.6
- OpenCV para Pyhton
- OpenCV_Contrib para Python
- Tener un sistema de archivos de la siguiente manera

    +FaceRecognition (Carpeta Principal)
      +dataset (Carpeta que contendra todas las imagenes de las personas que se quiere reconocer, recomiendo unas 50 por persona)
          +claudia_caceres (El nombre de la carpeta debe de tener el formato Nombre_Apellido)
              -U1_ClaudiaCaceres_1.jpg (El nombre de la imagen debe de tener el formato U#Identificador_NombreApellido_#Consecutivo)
              -U1_ClaudiaCaceres_2.bmp
              - ...
              -U1_ClaudiaCaceres_30.jpg
          +jorge_vicente
              -U2_JorgeVicente_1.jpg
              -U2_JorgeVicente_2.jpg
              - ...
              -U2_JorgeVicente_50.bmp
          +Nombre_Apellido3
          ...
          +Nombre_ApellidoN
      +output
          - aquí se descargará el video
      -Face_Recognition_Train.py (archivo que entrenara el algoritmo)
      -Face_Recognition_Video.py (archivo que levantara el video, utilizara el algoritmo entrenado y detectara y reconocera los rostros)
      -haarcascade_frontalface_default.xml  (Archivo entrenado para detectar rostro, propio del OpenCV)
      -usuarios.txt (Archivo que se creará y contendra los nombres de las personas a las que se quiere reconocer)
      -usuarios.yml (Archivo que se creará después de ejecutar el file Face_Recognition_Train.py, este archivo contiene los valores entrenados para reconocer el rostro de las personas que estan en la carpeta dataset)
      
## Pasos

 1) Levantar el file Face_Recognition_Train.py en su IDE predilecto, en mi caso es Spyder, y darle play, el proceso cargará todas las imagenes y creara un archivo output entrenado para reconocer rostro, además creara un archivo banco de datos con los nombres de las personas a reconocer.
 2) Levantar el file Face_Recognition_Video.py, este creara un video en linea detectando y reconociendo el rostro de la persona que sale en el video.
 3) Disfruta del código :)
