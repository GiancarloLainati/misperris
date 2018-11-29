from blog.models import Rescatado
from rest_framework import serializers

class RescatadoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Rescatado
        fields = ('fotografia', 'nombre', 'raza', 'descripcion', 'estado',)
