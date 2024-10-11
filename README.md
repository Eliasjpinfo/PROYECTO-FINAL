# Proyecto desarrollado en python

## Descripción

Comprende un blog orientado a noticias y artículos

## Estructura del proyecto

```

├── blog-repo/					<--- Carpeta del Repositorio
│ ├── blog/					    <--- Carpeta del proyecto Django
│ │ ├── apps/					<--- Aplicaciones Django
│ │ │ ├── post/
│ │ │ │ ├── __pycache__/	    **Ignorada en el .gitignore**
│ │ │ │ ├── migrations/		    **Ignorada en el .gitignore**
│ │ │ │ ├── __init__.py
│ │ │ │ ├── admin.py
│ │ │ │ ├── apps.py
│ │ │ │ ├── models.py
│ │ │ │ ├── tests.py
│ │ │ │ ├── urls.py
│ │ │ │ └── views.py
│ │ │ ├── user/
│ │ │ │ ├── __pycache__/	    **Ignorada en el .gitignore**
│ │ │ │ ├── migrations/		    **Ignorada en el .gitignore**
│ │ │ │ ├── __init__.py
│ │ │ │ ├── admin.py
│ │ │ │ ├── apps.py
│ │ │ │ ├── models.py
│ │ │ │ ├── tests.py
│ │ │ │ ├── urls.py
│ │ │ │ └── views.py
│ │ │ └── ...
│ │ ├── blog/
│ │ │ ├── __pycache__/		    **Ignorada en el .gitignore**
│ │ │ ├── configurations/	    <--- Configuraciones django (opcional)
│ │ │ │ ├── __pycache__/	    **Ignorada en el .gitignore**
│ │ │ │ ├── local.py		    <--- Configuraciones para desarrollo local
│ │ │ │ ├── production.py	    <--- Configuraciones para produccion
│ │ │ │ ├── base.py		    <--- Configuraciones base
│ │ │ │ └── ...
│ │ │ ├── __init__.py
│ │ │ ├── asgi.py
│ │ │ ├── settings.py
│ │ │ ├── urls.py
│ │ │ ├── wsgi.py
│ │ │ └── ...
│ │ ├── media/				    <--- Archivos multimedia - **Podria ser ignorada en el .gitignore**
│ │ │ ├── post/
│ │ │ │ ├── post_default.jpeg
│ │ │ │ └── ...
│ │ │ ├── user/
│ │ │ │ ├── user_default.png
│ │ │ │ └── ...
│ │ │ └── ...
│ │ ├── static/				    <--- Archivos estáticos
│ │ │ ├── assets/
│ │ │ │ ├── img/
│ │ │ │ ├── svg/
│ │ │ │ ├── favicon.ico
│ │ │ │ └── ...
│ │ │ ├── css/
│ │ │ │ ├── style.css
│ │ │ │ └── ...
│ │ │ ├── js/
│ │ │ │ ├── main.js
│ │ │ │ └── ...
│ │ │ └── ...
│ │ ├── templates/			    <--- Archivos templates
│ │ │ ├── auth/
│ │ │ │ ├── auth_login.html
│ │ │ │ ├── auth_register.html
│ │ │ │ └── ...
│ │ │ ├── errors/
│ │ │ │ ├── not_found.html
│ │ │ │ ├── internal_error.html
│ │ │ │ └── ...
│ │ │ ├── components/
│ │ │ │ ├── base.html
│ │ │ │ ├── footer.html
│ │ │ │ ├── header.html
│ │ │ │ └── ...
│ │ │ ├── post/
│ │ │ │ ├── post_delete.html
│ │ │ │ ├── post_detail.html
│ │ │ │ ├── post_list.html
│ │ │ │ ├── post_new.html
│ │ │ │ ├── post_update.html
│ │ │ │ └── ...
│ │ ├── db.sqlite3			    <--- Base de datos - **Ignorada en el .gitignore**
│ │ ├── manage.py
│ │ └── ...
│ ├── entorno/						<--- Carpeta del entorno - **Ignorada en el .gitignore** 
│ │ ├── Scripts/
│ │ │ ├── activate.bat
│ │ │ ├── deactivate.bat
│ │ │ └── ...
│ │ └── ...
│ ├── .gitignore
│ │ │ ├── user/
│ │ │ │ ├── user_profile.html
│ │ │ │ ├── user_update.html
│ │ │ │ └── ...
│ │ │ ├── index.html
│ │ │ └── ...
│ │ ├── db.sqlite3			    <--- Base de datos - **Ignorada en el .gitignore**
│ │ ├── manage.py
│ │ └── ...
│ ├── entorno/						<--- Carpeta del entorno - **Ignorada en el .gitignore** 
│ │ ├── Scripts/
│ │ │ ├── activate.bat
│ │ │ ├── deactivate.bat
│ │ │ └── ...
│ │ └── ...
│ ├── .gitignore
│ ├── README.md				    <--- Archivo README.md - Describe el proyecto
│ ├── requeriments.txt		    <--- Archivo requeriments.txt - Enlista los paquetes
| └── ...
└── ...

```

