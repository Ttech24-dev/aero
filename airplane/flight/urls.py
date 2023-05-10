from django.urls import path
from . import views

urlpatterns = [
    path('', views.flight, name='flight'),
    path('<int:flight_id>/', views.control, name='control'),
    path('<int:flight_id>/book/', views.book, name='book'),
]
    
