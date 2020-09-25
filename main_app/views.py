from django.shortcuts import render, redirect
from .models import Widget, WidgetForm
from django.views.generic.edit import DeleteView, CreateView
from django.views.generic import ListView

# Create your views here.
def home(request):
    return render(request, 'home.html', {'widgets': Widget.objects.all()})

class WidgetList(ListView):
  model = Widget
  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['widget_form'] = WidgetForm()
      return context

class WidgetCreate(CreateView):
  model = Widget
  fields = '__all__'

class WidgetDelete(DeleteView):
  model = Widget
  success_url = '/'
