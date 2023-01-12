from django.urls import path
from . import views

urlpatterns = [
    path('Traveling/', views.Traveling_base, name='Traveling'),
    path('', views.Traveling_home, name='Traveling_home'),
    path('create/', views.Traveling_create, name='Traveling_create'),
    path('read/', views.Traveling_read, name='Traveling_read'),
    path('<int:pk>/details/', views.Traveling_details, name='Traveling_details'),
    path('<int:pk>/update/', views.Traveling_update, name='Traveling_update'),
    path('<int:pk>/delete/', views.Traveling_delete, name='Traveling_delete'),

]