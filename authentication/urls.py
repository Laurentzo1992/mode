from  django.urls import  path
from  . import views

urlpatterns = [
    path('', views.Login, name='login'),
    path('login_user', views.login_user, name="login_user"),
    path('auth/logout_user', views.Logout_user, name='logout_user'),
    path('auth/profile', views.profile, name='profile'),
    path('home', views.home, name='home'),
    # path('auth/add', views.add_user, name="add_user"),
    # path('auth/edit/<int:id>', views.edit_user, name="edit_user"),
    # path('auth/delete/<int:id>', views.delete_user, name="delete_user"),
    # path('auth/users', views.users, name="users"),
 
    
]
