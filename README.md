# Codigo Fuente para Reconocimiento Facial con Python y OpenCv


## Requerimientos

- Python 3.6
- OpenCV para Pyhton
- OpenCV_Contrib para Python
- Tener un sistema de archivos de la siguiente manera

    +FaceRecognition (1)
      +dataset (2)
          +claudia_caceres (3)
              -U1_ClaudiaCaceres_1.jpg (4)
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
      -Face_Recognition_Train.py (5)
      -Face_Recognition_Video.py (6)
      -haarcascade_frontalface_default.xml  (7)
      -usuarios.txt (8)
      -usuarios.yml (9)
      
    Descripción:
    (1) Carpeta Principal.
    (2) Carpeta que contendra todas las imagenes de las personas que se quiere reconocer, recomiendo unas 50 imagenes por persona.
    (3) El nombre de la carpeta debe de tener el formato "Nombre_Apellido".
    (4) El nombre de la imagen debe de tener el formato "U#IdentificadorUnico_NombreApellido_#NumeroConsecutivo".
    (5) Archivo que entrenará el algoritmo.
    (6) Archivo que levantará el video, utilizará el algoritmo entrenado, detectará y reconocerá los rostros.
    (7) Archivo entrenado que servirá para detectar los rostro de las imagenes, propio del OpenCV.
    (8) Archivo que se creará y contendrá los nombres de las personas a las que se quiere reconocer, con el #IdentificadorUnico como ID.
    (9) Archivo que se creará después de ejecutar el file Face_Recognition_Train.py, este archivo contiene los valores entrenados para reconocer el rostro de las personas.
      
## Pasos

 1) Levantar el file Face_Recognition_Train.py en su IDE predilecto, en mi caso es Spyder, y darle play, el proceso cargará todas las imagenes y creara un archivo output entrenado para reconocer rostro, además creara un archivo banco de datos con los nombres de las personas a reconocer.
 2) Levantar el file Face_Recognition_Video.py, este creara un video en linea detectando y reconociendo el rostro de la persona que sale en el video.
 3) Disfruta del código :)
