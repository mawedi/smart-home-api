from django.urls import path
from .views import DorListCreateViewSet, DorRetrieveUpdateDestroyViewSet

urlpatterns = [
    # URL for listing and creating a dor
    path('', DorListCreateViewSet.as_view({'get': 'list', 'post': 'create'}), name='dor-list-create'),
    
    # URL for retrieving, updating, and deleting a specific dor
    path('<str:pk>', DorRetrieveUpdateDestroyViewSet.as_view({
        'get': 'retrieve',   # Retrieve an individual Dor by ID
        'put': 'update',     # Update an individual Dor by ID
        'delete': 'destroy'  # Delete an individual Dor by ID
    }), name='dor-retrieve-update-destroy'),
]
