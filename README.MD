# Sprint Final M6 - Awakelab

# REQUERIMIENTOS:

1. - Levantar al menos dos templates:
  Crea dos archivos HTML en la carpeta templates de tu proyecto Django. Por ejemplo, template1.html y template2.html. OK
  Diseña el contenido de cada template según tus necesidades. OK

2. - Manejar adecuadamente los archivos estáticos:

  Crea una carpeta llamada static en tu proyecto Django si aún no existe. OK 
  Coloca los archivos estáticos (CSS, JavaScript, imágenes, etc.) en la carpeta static. OK 
  Asegúrate de que la configuración de los archivos estáticos en settings.py sea correcta. OK

3. - Integrar Bootstrap y extender las plantillas con block-content:
  
  Descarga los archivos de Bootstrap desde su sitio web oficial o utiliza una CDN para enlazarlos en tu proyecto. OK
  Define un bloque {% block content %} en tus templates base y extiéndelos en los demás templates que lo necesiten utilizando {% extends 'base.html' %}. OK

4. - Configurar las URLs del proyecto por aplicación:

Crea un archivo urls.py en cada una de tus aplicaciones Django. OK
Define las URL para cada vista en los archivos urls.py correspondientes. OK

5. - Crear un archivo views.py con las vistas necesarias:

  Crea un archivo views.py en cada una de tus aplicaciones Django. OK
  Define las funciones de vista requeridas para manejar las solicitudes HTTP. OK

6. - Implementar un formulario utilizando Django Forms:

  Crea un archivo forms.py en una de tus aplicaciones Django. OK
  Define un formulario utilizando la funcionalidad proporcionada por Django Forms. OK

7. - Configurar un sistema de login-logout con permisos diferenciados:

  Utiliza la autenticación provista por Django para implementar un sistema de login-logout. OK  
  Define diferentes grupos de usuarios en el panel administrativo de Django y asigna permisos según tus necesidades. OK
  Asegúrate de que las vistas correspondientes estén protegidas y solo sean accesibles para los usuarios con los permisos adecuados. OK

8. - Implementar un sistema de registro de usuarios:

  Crea un formulario de registro de usuarios utilizando Django Forms. OK
  Agrega un campo en el formulario para que los usuarios seleccionen el grupo al que pertenecen. OK 
  Procesa el formulario de registro en una vista y crea nuevos usuarios con los grupos correspondientes. OK

9. - Actualizar tu repositorio en GitHub:

  Asegúrate de tener un repositorio Git inicializado en tu proyecto local. OK
  Agrega los archivos y realiza un commit de los cambios. OK
  Conéctate a tu repositorio remoto en GitHub y realiza un push de tus cambios. OK

