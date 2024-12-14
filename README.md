# Proyecto

Este proyecto demuestra el ciclo completo de desarrollo de una aplicación web, incluyendo pruebas automatizadas y despliegue.

La idea es tener una aplicación mínima en Flask que pasa por varias etapas: código, test y producción.

# Tecnologías utilizadas
- **[Flask](https://flask.palletsprojects.com/en/stable/)** desarrollado en [Python](https://www.python.org/)
- **[tox.ini](https://tox.wiki/en/latest/index.html)**
- **[Ansible](https://www.ansible.com/)**
- **[GitHub Actions](https://github.com/features/actions)**

# Contextualización:

- Se desarrolla una aplicación sencilla en Python utilizando el framework Flask, que permitirá crear una aplicación web básica pero funcional.
- Se añadirán pruebas automáticas para asegurar que el código respeta las convenciones del estilo PEP8, lo que garantiza un código legible y mantenible.
- El proyecto será alojado en GitHub, lo que nos permitirá gestionar el código y otras personas pueden contribuir al proyecto.
- Implementaremos Integración Continua (CI) mediante GitHub Actions o Workflows, lo que automatizará las pruebas del código cada vez que haya cambios. 
- Para el despliegue, se utilizará Ansible, con el cual se gestionará las dependencias, servicios y el entorno virtual de la aplicación. Para esto se han de crear varios roles que automatizarán la instalación de los servicios necesarios, la creación del entorno de Python y la instalación de las dependencias necesarias para el proyecto.
- Utilizaremos de servidor web Nginx. La aplicación en Flask se ejecutará en localhost y Nginx actuará también de proxy redirigiendo las peticiones.

# Funcionalidades
1. Página web básica con:
   - Inicio
   - ¿Quiénes somos?
   - Servicios
   - Contáctanos

