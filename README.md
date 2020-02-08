# Identicons Generator (Django)

Generador de imagenes aleatorias

## Generación de proyecto

Instalar Django con Pip

```command-line
pip3 install Django
```

Generar el proyecto con el CLI de Django

```command-line
django-admin startproject identicons
```

Cambiarnos de directorio al proyecto

```command-line
cd identicons
```

Iniciar el entorno virtual dentro del proyecto

```command-line
python3 -m venv <nombre_del_entorno>
```

Activar el entorno

```command-line
source <nombre_del_entorno>/bin/activate
```

Migrar la base de datos

```command-line
python manage.py migrate
```

Correr el servidor

```command-line
python manage.py runserver
```

## Crear una aplicación

Generar aplicación desde CLI de Django

```command-line
python manage.py startapp my_app
```

Registrarla en `proyecto/settings.py`

```python
INSTALLED_APPS = [
    ...,
    'my_app',
]
```

## Instalar requerimientos de un proyecto

```command-line
pip install -r requirements.txt
```
