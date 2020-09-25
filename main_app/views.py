from django.shortcuts import render, redirect
from .models import Widget
from django.views.generic.edit import DeleteView

# Create your views here.
def home(request):
    return render(request, 'home.html', {'widgets': Widget.objects.all()})

