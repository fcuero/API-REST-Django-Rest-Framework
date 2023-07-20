from rest_framework import serializers
from .models import Avatar, Movies, Planets, Productors, Director

## Creamos los Serializadores para los modelos Avatar y Movies
## Serializadores : Convierten las instancias de modelos tipos de datos nativos de Python 
## para que puedan ser renderizados en JSON, XML o cualquier otro formato de contenido 
## que el cliente pueda entender.

class AvatarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avatar
        fields = '__all__'

class MoviesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = '__all__'

class PlanetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planets
        fields = '__all__'

class ProductorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productors
        fields = '__all__'

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'