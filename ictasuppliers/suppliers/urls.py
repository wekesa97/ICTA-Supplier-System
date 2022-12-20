from django.urls import path
from .views import (
    SuppliersListView,SuppliersCreateView,
    SuppliersUpdateView,SuppliersDetailView,
    SuppliersDeleteView)

app_name = "suppliers"

urlpatterns = [
    path('', SuppliersListView.as_view(), name="suppliers-list"),
    path('create/', SuppliersCreateView.as_view(), name="suppliers-create"),
    path('<int:pk>/', SuppliersDetailView.as_view(), name="suppliers-detail"),
    path('<int:pk>/update/', SuppliersUpdateView.as_view(), name="suppliers-update"),
    path('<int:pk>/delete/', SuppliersDeleteView.as_view(), name="suppliers-delete"),
    
    
]
