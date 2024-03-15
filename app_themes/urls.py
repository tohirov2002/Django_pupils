from django.urls import path

from .views import themes_list,themes_create,themes_edit,delete_themes

urlpatterns = [
    path('',themes_list,name='themes_list'),
    path('add/', themes_create, name='add_themes'),
    path('edit/<int:pk>/',themes_edit,name='themes_edit'),
    path('delete/<int:pk>/', delete_themes, name='delete_themes'),
]