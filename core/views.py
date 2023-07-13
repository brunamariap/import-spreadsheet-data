from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from .models import Kit
# Create your views here.
class HomeView(CreateView):
    template_name = 'home.html'
    allow_empty = True
    queryset = Kit.objects.all()
    fields = []
    # ordering = ['-id']