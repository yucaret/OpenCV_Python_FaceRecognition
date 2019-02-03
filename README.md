# Código Fuente para Reconocimiento Facial con Python y OpenCV

Les presento el código fuente de reconocimiento facial que he desarrollado, la lógica no es nada del otro mundo, el modelo sigue la misma estructura que cualquier modelo de predicción, es decir, al modelo le das los valores X para que devuelva los Y prediction, en este caso los X son las distintas caras del usuario y el Y es el nombre, espero lo disfruten.

## Requerimientos

- Python 3.6
- Anaconda 3
- OpenCV para Pyhton
- OpenCV_Contrib para Python
- Tener un sistema de archivos de la siguiente manera:

    - FaceRecognition (i)
        - dataset (ii)
            - claudia_caceres (iii)
                - U1_ClaudiaCaceres_1.jpg (iv)
                - U1_ClaudiaCaceres_2.bmp
                - ...
                - U1_ClaudiaCaceres_30.jpg
            - jorge_vicente
                - U2_JorgeVicente_1.jpg
                - U2_JorgeVicente_2.jpg
                - ...
                - U2_JorgeVicente_50.bmp
            - Nombre_Apellido3
            - ...
            - Nombre_ApellidoN
        - output
            - aquí se descargará el video
        - Face_Recognition_Train.py (v)
        - Face_Recognition_Video.py (vi)
        - haarcascade_frontalface_default.xml  (vii)
        - usuarios.txt (viii)
        - usuarios.yml (ix)
      
    Descripción:
    1) Carpeta Principal.
    2) Carpeta que contendrá todas las imágenes de las personas que se quiere reconocer, recomiendo unas 50 imagenes por persona.
    3) El nombre de la carpeta debe de tener el formato "Nombre_Apellido".
    4) El nombre de la imágen debe de tener el formato "U#IdentificadorUnico_NombreApellido_#NumeroConsecutivo".
    5) Archivo que entrenará el algoritmo.
    6) Archivo que levantará el video, utilizará el algoritmo entrenado, detectará y reconocerá los rostros.
    7) Archivo entrenado que servirá para detectar los rostro de las imágenes, propio del OpenCV.
    8) Archivo que se creará y contendrá los nombres de las personas a las que se quiere reconocer, con el #IdentificadorUnico como ID.
    9) Archivo que se creará después de ejecutar el file Face_Recognition_Train.py, este archivo contiene los valores entrenados para reconocer el rostro de las personas.
      
## Pasos

 1) Levantar el file Face_Recognition_Train.py en su IDE predilecto, en mi caso es Spyder, y darle play, el proceso cargará todas las imagenes y creara un archivo output entrenado para reconocer rostro, además creará un archivo banco de datos con los nombres de las personas a reconocer.
 2) Levantar el file Face_Recognition_Video.py, este creará un video en línea, el programa detectará y reconocerá el rostro de la persona que sale en el video y lo guardará en la carpeta "output" cuando presiones "q".
 3) Disfruta del código :).
