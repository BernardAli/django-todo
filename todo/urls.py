from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('create_todo', views.create_todo, name='create_todo'),
    path('todo/<int:id>', views.todo_detail, name='todo_detail'),
    path('todo_delete/<int:id>', views.todo_delete, name='todo_delete'),
    path('todo_edit/<int:id>', views.todo_edit, name='todo_edit'),
]