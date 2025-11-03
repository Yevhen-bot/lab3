from rest_framework import serializers
from .models import *

def getSerializer(modelToSer):
    class Meta:
        model = modelToSer
        fields = '__all__'

    serializer_class = type(f"{modelToSer.__name__}Serializer", (serializers.ModelSerializer,), {"Meta":Meta})
    return serializer_class