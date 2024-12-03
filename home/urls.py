from django.urls import path
from .views import HomeListCreateViewSet, HomeRetrieveUpdateDestroyViewSet

urlpatterns = [
    # URL for listing and creating homes
    path('', HomeListCreateViewSet.as_view({'get': 'list', 'post': 'create'}), name='home-list-create'),
    
    # URL for retrieving, updating, and deleting a specific home
    path('<str:pk>', HomeRetrieveUpdateDestroyViewSet.as_view({
        'get': 'retrieve',   # Retrieve an individual Dor by ID
        'put': 'update',     # Update an individual Dor by ID
        'delete': 'destroy'  # Delete an individual Dor by ID
    }), name='home-retrieve-update-destroy'),
]
