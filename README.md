# Tuits Monitor
Esta pequeña aplicación escrita en Python hace uso de la librería [Tweepy](https://github.com/tweepy/tweepy/) y permite recoger en tiempo real los tuit publicados en la red social Twitter que estén etiquetados con ciertos _hashtags_ predefinidos por el autor.

Para utilizar el script simplemente es necesario instalar Tweepy en tu entorno de ejecución Python (o virtualenv)

    pip install tweepy

configurar los distintos parámetros que contiene _consumer_key_, _consumer_secret_ y los _hashtags_ y redirigir la salida que produce a algún fichero de texto que guarde los tuits recolectados por el script del siguiente modo:

    python tuits-monitor.py > nombrefichero.txt


Nota: En futuras versiones públicas de este _crawler_ se integrará como funcionalidad el guardado en base de datos de los tuits recuperados
