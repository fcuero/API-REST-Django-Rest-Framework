import statistics
from urllib import response

from rest_framework import viewsets, permissions, filters
from .models import Avatar, Movies, Planets, Productors, Director
from .serializers import AvatarSerializer, MoviesSerializer, PlanetsSerializer, ProductorsSerializer, DirectorSerializer
from django_filters.rest_framework import DjangoFilterBackend

## Creamos las vistas para los modelos Avatar y Movies

#GET requests
class AvatarViewSet(viewsets.ModelViewSet):
    queryset = Avatar.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = AvatarSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]

    filterset_fields = ['name']
    search_filters = ['name']

class PlanetsViewSet(viewsets.ModelViewSet):
    queryset = Planets.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = MoviesSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]

    # A filter that allows us to filter the data by the name of the movie.
    filterset_fields = ['name']
    search_filters = ['name']

class MoviesViewSet(viewsets.ModelViewSet):

    queryset = Movies.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = MoviesSerializer


## POST requests
class AddProductorViewSet(viewsets.ModelViewSet):
    queryset = Productors.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ProductorsSerializer

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs) 

class AddDirectorViewSet(viewsets.ModelViewSet):
    queryset = Director.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = DirectorSerializer

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
   
class AddAvatarViewSet(viewsets.ModelViewSet):
    queryset = Avatar.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = AvatarSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return response

class AddMovieViewSet(viewsets.ModelViewSet):

    queryset = Movies.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = MoviesSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return response

class AddPlanetViewSet(viewsets.ModelViewSet):

    queryset = Planets.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = PlanetsSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return response

