from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Dor
from .serializers import DorSerializer

class DorListCreateViewSet(viewsets.GenericViewSet, viewsets.mixins.ListModelMixin, viewsets.mixins.CreateModelMixin):
    queryset = Dor.objects.all()
    serializer_class = DorSerializer

    def get_queryset(self):
        # Retrieve the home id from the query parameters
        home_id = self.request.query_params.get('home')
        
        if home_id is not None:
            # Filter the Dor instances based on the home ID
            return Dor.objects.filter(home_id=home_id)
        else:
            # If no home ID is provided, return all Light instances
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": "The id of the home is not provided"})


class DorRetrieveUpdateDestroyViewSet(viewsets.GenericViewSet, viewsets.mixins.RetrieveModelMixin, 
                                       viewsets.mixins.UpdateModelMixin, viewsets.mixins.DestroyModelMixin):
    queryset = Dor.objects.all()
    serializer_class = DorSerializer
