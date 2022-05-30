# blogdehoryan
Proyecto Final Horacio San Martín - CoderHouse

### 0. EXPLICACION DE LA PAGINA WEB
LINK VIDEO YOUTUBE: https://youtu.be/HWXVEFgOXSQ

pagina web de reviews de videojuegos y noticias de juegos, para correrla entrar a cd blog
admin: hory
contraseña: qwerty123

otros usuarios: maxi, fabi, valen, fran
contraseña: narniaesreal123

Se pueden editar, borrar, agregar cosas, se pueden editar los perfiles, registrar usuarios nuevos, agregar avatar o incluso cambiarlos
Además, se agregó un inbox con la posibilidad de mandar mensajes entre usuarios


### 1. CREANDO REPOSITORIO, MVT, APP
- unimos al repositorio online
- empezamos el proyecto blog
django-admin startproject blog

- creamos la app donde estará todo lo interesante
python manage.py startapp App

### 2. CREACION MODELOS

- crearemos un proyecto que tendrá  los siguientes modelos:
    - juegos (titulo (nombre), subtitulo, categoria, texto (ckeditor), imagen, fecha, autor)
    - noticias (titulo, subtitulo, genero, texto, imagen, fecha, autor)
    - integrantes (nombre, apellido, email, cargo): equipo del blog, periodistas, informáticos, etc
    - sugerencias (nombre, categoria)

nota: fecha y autor, las dejé de manera manual por dos motivos: 1) en una publicación de un blog de reviews no hay periocidad de tiempo tan seguida, son en general publicaciónes más prolongadas en tiempo (1 semanal), 2) me gusta que la persona que cree una publicación tenga la libertad de generar su nombre de usuario que considere mejor para si mismo (ya sea su nombre, usuario, o anónimo)

- creamos los modelos en App/models.py: juegos, noticias, integrantes, sugerencias
- agregamos la App en settings.py (INSTALLED_APPS)
- revisamos que esté bien la app:
python manage.py check App

-hacemos estructura de SQL:
python manage.py makemigrations
python manage.py sqlmigrate App 0001
python manage.py migrate 

(nota: cada vez que modifiquemos los modelos volvemos a hacer makemigrations y migrate!!)

### 3. CREAMOS VIEWS
- Partimos creando una view para cada modelo y pagina de inicio en views.py 
- creamos urls.py en la App, y linkeamos a urls de la pagina original

### 4.INSTALACIÓN TEMPLATES Y HERENCIAS
- utilizaremos la template de la entrega anterior ya que me gustó
- creamos carpeta App/static/App
- dentro de la carpeta ponemos los archivos del template

- creamos template padre con botones para cada sección de la página

- creamos block titulo y contenidoQueCambia para personalizar cada pagina
-agregamos view con url, template para el acerca de mi!


### 5. PANEL DE ADMINISTRACIÓN
- entramos a admin.py 
- creamos los modelos para acceder desde el panel de control, e importamos los modelos desde models.py

- creamos el usuario:
python manage.py createsuperuser
username: hory
mail: hory.san93@gmail.com
pass: qwerty123

### 6. Creando CRUD para reviess de videojuegos
Nota: para la entrega intermedia esta sección se dividía en 2 partes, primero el ingresar datos por formulario, haciendo que tuviesemos que crear dentro de la App los formularios, y luego utilizarlos para eliminar editar, etc. 
Acá en cambio, los haremos utilizando CRUD 

- Partimos creando un CRUD de Juegos ListView, DetailView, CreateView, Edit, delete, etc, que depende del modelo y template
- La idea es que dejando este OK el resto será más directo de realizar
- Vamos a URL paths y agregamos las 5 rutas de las views
- <pk> elige el id del objeto en cuestión
- creamos templates juego_confirm_delete, form, detalle, list que son necesarios
- se realizaron algunas configuraciones en los templates para que funcionen bien

#### 6.1 Agregando texto más cool 
-instalamos
pip install django-ckeditor
- lo agregamos a settings.py
- cambiamos el texto del modelo por textoenriquecido
- agregamos RichTextField para la reseña [ y funciona!:) ]

#### 6.2 agregamos las imagenes >:C
pip install pillow
- agregamos en settings el sitio de las imagenes
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

- luego a la url del proyecto (no de la app), le ponemos urls de medias, e importamos lo necesario
    from django.conf import settings
    from django.conf.urls.static import static 

- como modificamos tenemos que volver atirar el makemigrations
python manage.py makemigrations
python manage.py migrate

-agregué al template de juego_detalle la configuración necesaria
-para que funcionara fue necesario configurar bien el juego_form
<form style="color:white" method="post" enctype="multipart/form-data">
            {% csrf_token %}
            {{ form.as_p }}
            <input type="submit" value="ENVIAR" />
        </form>

#### 6.3 Enchular fecha y autor 
La idea sería que la fecha del posteo sea en la cual se realiza este de manera automática quizás, y por otra parte,
que la publicación esté linkeada al autor de esta. 

Por el momento tenemos las dos variables como fecha y autoría manual, pero la idea es posteriormente mejorarlo!
- El objetivo será hacer lo que se vio en clases de linkear el avatar con el usuario, pero linkeando el autor con el usuario que se crea

### 7 LOGIN, REGISTER, LOGOUT y CONTROL PERMISOS
#### 7.1 login
- Partimos creaqndo template login.html con un botón para iniciar sesión
- Agregamos url que nos llevará al template
- importamos paquetes en views, y agregamos la view login_request (para que no haya conflicto de nombre)
- agregamos a template padre que si la persona está logeada salga!

#### 7.2 register
- importamos también UserRegisterForm en views
- creamos forms.py con el registro de usuario
- importamos forms en views
- creamos la vista register
- creamos el template register
- agreamos el path!
- Creamos nuevo usuario:
maxi, maxi@maxi.cl,narniaesreal123 

#### 7.3 logout
- creamos template
-path
- configuramos plantilla padre para que incluya al usuario loggeado
- configuramos plantilla inicio para que solo salude si la persona está loggeada

#### 7.4 limitando permisos (dejando solo hacer algunas cosas a los loggeados)
- usamos mixin para vistas basadas en clases y decoradores para las vistas basadas en funciones
para las clases:
-importamos en views
from django.contrib.auth.mixins import LoginRequiredmixin

-agregamos LoginRequiredMixin para crear, editar y eliminar publicaciones
-si no estamos loggeados haremos que nos redirija a app/login
-vamos a settings.py y agregamos el LOGIN_URL el url de login

para las funciones: (editar usuario)
-importamos el paquete en views 
from django.contrib.auth.decorators import login_required

### 8. AVATAR USUARIOS
- partimos creando el modelo avatar
- importamos en modelos django... User
- la carpeta media ya la tenemos creada :D
- ruta de settings y urls lista :D
- como agregamos un modelo:
python manage.py makemigrations
python manage.py migrate
- agregamos en admin.py el modelo de avatar
- agregamos a inicio el avatar
(pendiente ver como achicar el avatar >:C)

- agregamos vista para agregar avatar
- agregamos path
- creamos template agregarAvatar

Nota: si nos metemos directo no tenemos problema
pero si vamos al app/inicio como tenemos linkeado el avatar se requiere estar loggeado :O! (arregaldo poniendo if)

### 10. mostrar últimas noticias en inicio
- agregamos en el template las últimas noticias y juegos en la view de inicio
- se corrigió el poner desde la publicación más reciente en el listado de juegos (utilizando object_list reversed)
- se corrigió que cuando la persona estaba en la página de inicio pero no tenía avatar, todo explotara
- agregamos que solo los administradores puedan eliminar publicaciones, editarlas, verlas y crearlas las pueden hacer los usuarios

### 11. agregar chat entre usuarios
Nota: para la creación de la aplicación de chat utilicé el siguiente video tutorial:
https://www.youtube.com/watch?v=oxrQdZ5KqW0&ab_channel=LegionScript

Si bien el ideal habría sido hacer la aplicación desde cero, y aunque creo que la guía del profesor me orientaba a lo que quería lograr, mi visión profesional se basa en saber encontrar material y aprender haciendo en el proceso, más que aprender desde cero. De hecho este tutorial fue el cuarto que apliqué (el primero era con channels y redis). Todos fallaron rotundamente, pero al menos iba aprendiendo sobre la marcha y, finalmente, con los conocimientos del ensayo y error y lo aprendido en el curso, pude adaptar el código presente para mi página web, haciéndola funcionar.

- Primero se creó la aplicación y se agregó a settings (igual que lo hicimos por App)
- Se crearon los 2 modelos que se utilizarían, importamos User, y hacemos las migraciones correspondientes
class ThreadModel(models.Model):
class MessageModel(models.Model):

python manage.py makemigrations
python manage.py migrate

-luego se crean 2 formularios
class ThreadForm(forms.Form):
class MessageForm(forms.Form):

-con lo anterior pasamos a las vistas, acá importamos algo que no habíamos utilizado (View)
 ListThreads(View)
 CreateThread(View)
 ThreadView(View)
 CreateMessage(View)

-agregamos los paths al url de chat, y agregamos los urls de chat al url del proyecto

-pasamos a trabajar con los templates, importamos desde la plantilla base padre de App
-tenemos que importar crispy_forms por que la utilizaremos!
-creamos carpeta templates dentro de chat, luego chat dentro de template, y de ahí 3 templates:
create_thread
inbox
thread

-teniendo todo listo corremos la página web y agregamos el inbox 
Nota: hay 1 bug que espero corregir para la siguiente actualización de la página, que pasa que cuanod uno quiere ingresar al usuario que le va a enviar un mensaje, te manda al inicio del inbox, pero si apretas enviar y está vacío te deja ingresarlo.

### 12. CRUDS noticias, sugerencias
Sabiendo que la página  funciona, podemos hacer el CRUD de noticias, además de la página de integrantes y sugerencias

- como los modelos están hechos, pasamos a hacer las views de Noticias (identicas a las de juegos pero con noticia)
- agregamos los paths en urls (idèntico a juegos!)
- creamos las plantillas de noticias (lo mismo de antes hecho en juegos)
- arreglamos la intro  

- repetimos y hacemos el proceso de CRUD para las sugerencias (vamos a tener todo pero solo mostraremos aslgunas cositas)
- hubo que hacer algunos cambios pequeños para que corriera pero está funcional



### 13. extras
- vamos a arrreglar lo del tener 2 avatas, si ponemos el código de la clase: avatarViejo=Avatar.objects.get....., sucede que si el usuario no tenía avatar previo, el código me explota, por lo que haremos un cambio pequeño
if (Avatar.objects.get(user=request.user)):         #Ponemos primero el if, si pasa, le damos
    avatarViejo=Avatar.objects.get(user=request.user)
    avatarViejo.delete()
PD: sigue chillando cuando el usuario no tenía avatar previo (por lo que para que funcione habría que agregar otro)

- se elimina modelo y todo lo relacionado con Integrantes, ya que no le encontré ninguna utilidad


### 14. subir a github
git add .
git commit -m "EL BLOG DE HORYAN"
git push origin main 

### 15. Proximamente
Posterior a la aprobación del proyecto, la idea es perfilar la página para convertirla en una 100% funcional.

