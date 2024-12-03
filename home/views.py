from rest_framework import viewsets
from .models import Home
from .serializers import HomeSerializer

class HomeListCreateViewSet(viewsets.GenericViewSet, viewsets.mixins.ListModelMixin, viewsets.mixins.CreateModelMixin):
    queryset = Home.objects.all()
    serializer_class = HomeSerializer

class HomeRetrieveUpdateDestroyViewSet(viewsets.GenericViewSet, viewsets.mixins.RetrieveModelMixin, 
                                       viewsets.mixins.UpdateModelMixin, viewsets.mixins.DestroyModelMixin):
    queryset = Home.objects.all()
    serializer_class = HomeSerializer
