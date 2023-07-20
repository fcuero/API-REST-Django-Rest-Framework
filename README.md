# API-REST-Star-Wars
Me Rechazaron xd
 <br>
<img src="https://i.ibb.co/Z1X97XF/code.png" alt="code" border="0">
<h4> TECNOLOGIAS UTILIZADAS </b><br>
Python / Django Rest Framework<br>
<hr>
<h4>Pasos Para Ejecutar</h4> <hr>
1 - Clonar Repositorio <code> git clone https://github.com/MaironDev/API-REST-Star-Wars_Gearplug.git </code> <br>
2 - Instalar requerimientos <code> pip install -r requirements.txt</code> <br>
3. Realizar las Migraciones <code> py manage.py migrate </code> <br>
4. Correr la API Rest <code> py manage.py runserver </code><br>
<hr>
<h4> Documentacion de la API Rest </h4><hr>
<h3> MODELOS </h3> <br>
El royecto tiene los siguientes modelos : <br>
 - <b>Avatar</b> (Modelo para los personajes) <br>
 - <b>Movies</b> (Modelo para las peliculas) <br>
  - <b>Planets</b> (Modelo para los planetas) <br>
  - <b>Director</b> (Modelo para los directores) <br>
  - <b>Productors</b> (Modelo para los productores) <br>
<h3>ENDPOINTS </h3><br>
<code > api/avatar</code>  - > Este endpoint permite ver la lista de todos los personajes de star wars y de igual manera permite filtrar por el "nombre" del personaje <br>
<code > api/addavatar</code>  - > Este endpoint permite agregar un nuevo personaje, enlazado con una o varias peliculas y tambien tiene una imagen <br>
<code > api/addmovie</code>  - > Este endpoint permite agregar peliculas, tiene campos como nombre, descripcion, una imagen, director, personajes, productor y planetas <br>
<code > api/addplanet</code>  - > Este endpoint permite agregar un nuevo planeta <br>
<code > api/productor</code>  - > Este endpoint permite agregar un productor y las peliculas relacionadas<br>
<code > api/director</code>  - > Este endpoint permite agregar un director y las peliculas relacionadas<br>
<h3> CREDENCIALES DJANGO-ADMIN</h3>
<b>User : </b> admin <br>
<b> Password :</b> admin <br>
<h3>TEST UNITARIOS </h3><br>
Se realizaron pruebas unitarias para cada uno de los endpoints con la libreria <b> TestCase </b> que provee <b>DRF</b> <br>
Todos estos tests se encuentran en la carpeta <b>tests</b> del proyecto <br>
<hr>
<h4>Recursos Utilizados </h4><hr>
https://www.djangoproject.com/ <br> https://www.django-rest-framework.org/ <br>  https://django-filter.readthedocs.io/en/stable/ <br>  https://drf-yasg.readthedocs.io/en/stable/readme.html <br>

<hr>



