from  django.urls import  path
from  . import views

urlpatterns = [
    path('client', views.client, name='client'),
    path('client/add', views.add_client, name='add_client'),
    path('client/edit/<int:id>', views.edit_client, name='edit_client'),
    path('client/delete/<int:id>', views.delete_client, name='delete_client'),
    path('client/print/<int:id>', views.print_client, name='print_client'),
    
    path('ville', views.ville, name='ville'),
    path('ville/add/', views.add_ville, name='add_ville'),
    path('ville/edit/<int:id>', views.edit_ville, name='edit_ville'),
    path('ville/delete/<int:id>', views.delete_ville, name='delete_ville'),
    
    path('tenue', views.tenue, name='tenue'),
    path('tenue/add/', views.add_tenue, name='add_tenue'),
    path('tenue/edit/<int:id>', views.edit_tenue, name='edit_tenue'),
    path('tenue/delete/<int:id>', views.delete_tenue, name='delete_tenue'),
    
    path('modelle', views.modelle, name='modelle'),
    path('modelle/add/', views.add_modelle, name='add_modelle'),
    path('modelle/edit/<int:id>', views.edit_modelle, name='edit_modelle'),
    path('modelle/delete/<int:id>', views.delete_modelle, name='delete_modelle'),
]