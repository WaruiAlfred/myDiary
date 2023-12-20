from django.urls import path

from . import views

urlpatterns = [
    path('', views.all_entries, name='all_entries'),
    path('entry/<int:entry_id>/', views.view_entry, name='view_entry'),
    path('entry/add/', views.add_or_modify_entry, name='add_entry'),
    path('entry/<int:entry_id>/edit/', views.add_or_modify_entry, name='edit_entry'),
    
     # Authentication URLs
    path('register/', views.register, name='user_register'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
]
