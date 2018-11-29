from blog.models import Rescatado
from rest_framework import viewsets
from blog.quickstart.serializers import RescatadoSerializer

class RescatadoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Rescatado.objects.all().order_by('-date_joined')
    serializer_class = RescatadoSerializer
