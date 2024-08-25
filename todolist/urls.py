from django.urls import path
from todolist import views
# from . import views

app_name = 'urls_app_todo'

urlpatterns = [
    
    path('', views.index, name='urls_path_index'),
 # http://127.0.0.1:8000/
    path('delete/<int:id>', views.delete, name='urls_path_delete'),
    path('toggle_completed/<int:id>/', views.toggle_completed, name='toggle_completed'),
]
