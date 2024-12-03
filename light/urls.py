from django.urls import path
from .views import LightListCreateViewSet, LightRetrieveUpdateDestroyViewSet

urlpatterns = [
    # URL for listing and creating ligths of the home
    path('', LightListCreateViewSet.as_view({'get': 'list', 'post': 'create'}), name='ligth-list-create'),
    
    # URL for retrieving, updating, and deleting a specific light
    path('<str:pk>', LightRetrieveUpdateDestroyViewSet.as_view({
        'get': 'retrieve',   # Retrieve an individual Dor by ID
        'put': 'update',     # Update an individual Dor by ID
        'delete': 'destroy'  # Delete an individual Dor by ID
    }), name='light-retrieve-update-destroy'),
]
