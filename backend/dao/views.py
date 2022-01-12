from rest_framework import viewsets
from .serializer import NftProjectSerializer
from .models import NftProject

class NftProjectViewSet(viewsets.ModelViewSet):
    queryset = NftProject.objects.all()
    serializer_class = NftProjectSerializer