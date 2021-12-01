from django.urls import path, include
from django.views.generic import CreateView

from .views import TodoListView, TodoDetailView, TodoCreateView, TodoUpdateView,TodoDeleteView

urlpatterns = [
    path('',TodoListView.as_view(),name='home'),
    path('todo/new/', TodoCreateView.as_view(), name='todo_add'),
    path('todo/<int:pk>/',TodoDetailView.as_view(),name='detail'),
    path('todo/<int:pk>/update/', TodoUpdateView.as_view(), name='update'),
    path('todo/<int:pk>/delete/', TodoDeleteView.as_view(), name='delete')


]
