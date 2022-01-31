Pasos a seguir para correr el sistema:

1-Descargar o clonar el proyecto desde: https://github.com/Salvador-Ferrea/Proyecto
2-Instalar Python, preferentemente en su versión 3.10.0
3-Ejecutar desde consola el comando: pip install Django==3.2.8
4-Ejecutar desde consola el comando: pip install PyMySQL
5-Posicionarse desde la consola en la ruta "Proyecto\proyecto" y ejecutar el comando: python manage.py makemigrations
6-Posicionarse desde la consola en la ruta "Proyecto\proyecto" y ejecutar el comando: python manage.py migrate
7-Configurar en el archivo Proyecto\proyecto\proyecto\settings.py a partir de la linea 77 la información de la base de datos a la que se desea conectar
8-Posicionarse desde la consola en la ruta "Proyecto\proyecto" y ejecutar el comando: admin python manage.py createsuperuser (se pedirá luego el nombre de usuario y la contrseña, se creará el perfil del administrador y se accederá al mismo a travéz de http://127.0.0.1:8000/admin)
9-Posicionarse desde la consola en la ruta "Proyecto\proyecto" y ejecutar el comando: python manage.py runserver
10-Acceder al sistema a través de http://127.0.0.1:8000/
