# EJERCICIO 6_6 - LOGIN/LOGOUT GUIDO SAAVEDRA

# REQUERIMIENTOS:

1. Identifique dos grupos de usuarios de su aplicación.
2. En este sentido, debe crear dos usuarios de cada grupo.
3. Cada grupo tiene permisos diferenciados de acuerdo a sus características particulares. 
4. Es importante que en un archivo README.txt den cuenta de una reflexión que justifique los permisos diferenciados.
5. Los usuarios se deben crear de forma dinámica mediante un formulario,
para realizar esto, debe buscar la información necesaria en la documentación de Django y en las cápsulas de la sesión.
6. Verifique que los usuarios quedan registrados en la página de administración de Django.

Actualice su proyecto en GITHUB.

# APLICACION

1. Los grupos de usuarios de mi aplicacion son los siguientes:
    - Administrador
    - Usuario

2. Los usuarios de cada grupo son los siguientes:
    - Administrador
        - admin
        - admin2
    - Usuario
        - user
        - user2

3. Los permisos diferenciados de cada grupo son los siguientes:
    - Administrador
        - Puede ver la pagina de inicio
        - Puede ver la pagina de usuarios
        - Puede ver la pagina de administracion
        - Puede registrar mas administradores

    - Usuario
        - Puede ver la pagina de inicio
        - Puede ver la pagina de logout

4. La justificacion de los permisos diferenciados es la siguiente:

# Permiso del Administrador:

  - Ver la página de inicio: El administrador necesita acceder a la página de inicio
    para obtener una visión general del sistema y verificar el contenido mostrado.

  - Ver la página de usuarios: El administrador debe poder acceder a la lista de usuarios registrados
    para administrar cuentas, verificar información de usuarios y solucionar problemas relacionados con las cuentas.

  - Ver la página de administración: Esta página proporciona herramientas y funciones avanzadas para administrar el sistema,
    como la gestión de permisos, supervisión del rendimiento y configuración general.

  - Registrar más administradores: El administrador tiene el permiso para agregar y gestionar
    otros administradores en el sistema, asegurando suficiente personal autorizado para la administración del sistema.

 # Permiso del Usuario:

  - Ver la página de inicio: Los usuarios regulares necesitan acceder a la página de inicio para ver y utilizar
    el contenido y las funcionalidades generales del sistema.

  - Ver la página de cierre de sesión: Los usuarios deben tener acceso a la página de cierre de sesión para finalizar
    su sesión de manera segura y proteger su información personal.


5. Los usuarios se crean de forma dinamica mediante el siguiente formulario:
    /registration/signup.html
    /registration/susignup.htmml


#  CREDENCIALES

- Administrador
    - gpson
    - gpson123

    - admin2
    - letmeinforadmin

- Usuario
    - user
    - user123

    - testuser
    - letmeinfortest    

