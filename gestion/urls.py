from  django.urls import  path
from  . import views

urlpatterns = [
    path('statistique', views.statistique, name='statistique'),
    
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
    
    
    path('post', views.post, name='post'),
    path('post/add/', views.add_post, name='add_post'),
    path('post/edit/<int:id>', views.edit_post, name='edit_post'),
    path('post/delete/<int:id>', views.delete_post, name='delete_post'),
    
    
    
    path('personnel', views.personnel, name='personnel'),
    path('personnel/add/', views.add_personnel, name='add_personnel'),
    path('personnel/edit/<int:id>', views.edit_personnel, name='edit_personnel'),
    path('personnel/delete/<int:id>', views.delete_personnel, name='delete_personnel'),
    
    
    path('commande', views.commande, name='commande'),
    path('commande/add/', views.add_commande, name='add_commande'),
    path('commande/edit/<int:id>', views.edit_commande, name='edit_commande'),
    path('commande/delete/<int:id>', views.delete_commande, name='delete_commande'),
    path('commande/items/<int:id>', views.items_commande, name='items_commande'),
    
    
    path('livraison', views.livraison, name='livraison'), 
    path('livraison/bon/<int:id>', views.bon_livraison, name='bon_livraison'),
    path('livraison/valide_livraison/<int:id>', views.valide_livraison, name='valide_livraison'),
]