from django.shortcuts import render, HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Task


class TodoListView(ListView):
    model = Task
    template_name = 'home.html'


class TodoDetailView(DetailView):
    model = Task
    template_name = 'detail.html'


class TodoCreateView(CreateView):
    model = Task
    template_name = 'add.html'
    fields = ['title','description']


class TodoUpdateView(UpdateView):
    model = Task
    template_name = 'update.html'
    fields = ['title','description']


class TodoDeleteView(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('home')