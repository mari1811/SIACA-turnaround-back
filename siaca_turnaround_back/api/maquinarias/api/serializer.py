from rest_framework import serializers
from api.models import maquinaria, maquinaria_turnaround, categoria
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


class MaquinariaTuraroundDatosSerializer(serializers.ModelSerializer):
    class Meta:
        model = maquinaria_turnaround
        fields = '__all__'

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = categoria
        fields = ('nombre',)

class MaquinariaSerializer(serializers.ModelSerializer):
    fk_categoria = CategoriaSerializer()
    class Meta:
        model = maquinaria
        fields = '__all__'

class MaquinariaDatosSerializer(serializers.ModelSerializer):
    class Meta:
        model = maquinaria
        fields = '__all__'


class MaquinariaModificarSerializer(serializers.ModelSerializer):
    class Meta:
        model = maquinaria
        fields = '__all__'

class MaquinariaTuraroundSerializer(serializers.ModelSerializer):
    class Meta:
        model = maquinaria_turnaround
        fields = '__all__'
