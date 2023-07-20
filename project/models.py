from django.db import models

# Create your models here.
#Modelo para los Personajes 
class Avatar(models.Model):
    name = models.CharField(max_length=100)
    movie = models.ManyToManyField('Movies', related_name='movie', blank=True)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name 

#Modelo para los Planetas
class Planets(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

#Modelo para las Peliculas
class Movies(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    planet = models.ManyToManyField('Planets', related_name='planet', blank=True)
    image = models.ImageField(upload_to='images/movies')
    avatar = models.ManyToManyField('Avatar', related_name='avatar', blank=True)
    productor = models.ManyToManyField('Productors', related_name='productor', blank=True)
    director = models.ManyToManyField('Director', related_name='director', blank=True)

    def __str__(self):
        return '{} {} {} '.format(self.title, self.planet, self.avatar)

#Modelo para los Productores
class Productors(models.Model):
    name = models.CharField(max_length=100)
    the_movie = models.ManyToManyField('Movies', related_name='the_movie', blank=True)

    def __str__(self):
        return self.name 

#Modelo para los Directores
class Director(models.Model):
    name = models.CharField(max_length=100)
    movies = models.ManyToManyField('Movies', related_name='movies', blank=True)

    def __str__(self):
        return self.name
