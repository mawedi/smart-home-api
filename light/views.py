from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Light
from .serializers import LightSerializer

class LightListCreateViewSet(viewsets.GenericViewSet, viewsets.mixins.ListModelMixin, viewsets.mixins.CreateModelMixin):
    queryset = Light.objects.all()
    serializer_class = LightSerializer

    def get_queryset(self):
        # Retrieve the home id from the query parameters
        home_id = self.request.query_params.get('home')
        
        if home_id is not None:
            # Filter the Light instances based on the home ID
            return Light.objects.filter(home_id=home_id)
        
        else:
            # If no home ID is provided, return all Light instances
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": "The id of the home is not provided"})


class LightRetrieveUpdateDestroyViewSet(viewsets.GenericViewSet, viewsets.mixins.RetrieveModelMixin, 
                                       viewsets.mixins.UpdateModelMixin, viewsets.mixins.DestroyModelMixin):
    queryset = Light.objects.all()
    serializer_class = LightSerializer
