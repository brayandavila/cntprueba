# Aplicativo en funcionamiento: http://brayandavila95.pythonanywhere.com/

## Totalmente responsive, vista adecuada y cómoda en móviles

Versión de Python utilizada: 3.10.0

Framework utilizado: Django version 4.0.1

Instalar Django:

- Desde el CMD con permisos de administrador y Python instalado ejecutar la siguiente instrucción "pip install Django==4.0.1"

Nombre del proyecto: cntprueba

Conectado con MySQL Workbench version 8.0.26

Crear base de datos en MySQL

Hacer cambios pertinentes en el archivo "settings.py" que se encuentra en la carpeta "cntprueba"

**NOTA: EL PUERTO PUEDE SER DIFERENTE**
```python
DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.mysql',
	  	'HOST': 'localhost',
	  	'PORT': '3306',
	  	'USER': 'tu_usuario',
	  	'PASSWORD': 'tu_contraseña',
	  	'NAME': 'nombre_base_de_datos',
	  	'OPTIONS': {
	    		"init_command": "SET sql_mode='STRICT_TRANS_TABLES'"
	  	}
  	}
} 
 ```
Verificar instalación de MySQL en Django ejecutando la siguiente instrucción en la carpeta raíz del proyecto: "pip install mysqlclient pymysql"

Realizar migraciones con las siguientes instrucciones ejecutadas consecutivamente desde la carpeta raíz del proyecto: "python manage.py makemigrations" "python manage.py migrate"

Iniciar el servidor con la siguiente instrucción: "python manage.py runserver"

Ir al navegador iniciando por el localhost puerto 8000 "http://localhost:8000/"
