from django.urls import path

from .views import pupils_list,pupil_detail,pupils_create,pupils_edit,delete_pupil


urlpatterns = [
    path('pupils_list/',pupils_list,name='pupils_list'),
    path('<int:pk>/',pupil_detail,name='pupil_info'),
    path('edit/<int:pk>/',pupils_edit,name='edit_pupil'),
    path('delete/<int:pk>/', delete_pupil, name='delete_pupil'),
    path('add/', pupils_create, name='add_pupil'),
]