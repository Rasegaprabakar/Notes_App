from django.urls import path
from . import views
urlpatterns = [
#/todolist/
path('', views.index, name='index'),
#/todolist/add/
path('add/',views.add,name='add'),
#/todolist/delete/3/
path('delete/<int:todo_id>/',views.delete,name='delete'),
#/todolist/edit/3/
#path('edit/<int:todo_id>/',views.edit,name='edit'),

]