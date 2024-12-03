from django.urls import path
from .views import GasSensorListCreateViewSet, GasSensorRetrieveUpdateDestroyViewSet

urlpatterns = [
    # URL for listing and creating a gas line
    path('', GasSensorListCreateViewSet.as_view({'get': 'list', 'post': 'create'}), name='gas-list-create'),
    
    # URL for retrieving, updating, and deleting a specific home
    path('<str:pk>', GasSensorRetrieveUpdateDestroyViewSet.as_view({
        'get': 'retrieve',   # Retrieve an individual Dor by ID
        'put': 'update',     # Update an individual Dor by ID
        'delete': 'destroy'  # Delete an individual Dor by ID
    }), name='gas-retrieve-update-destroy'),
]
