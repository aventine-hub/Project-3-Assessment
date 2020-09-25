from django.db import models
from django.urls import reverse
from django.forms import ModelForm

# Create your models here.
class Widget(models.Model):
   description = models.CharField(max_length=100)
   quantity = models.IntegerField()
   def __str__(self):
        return self.item
   def get_absolute_url(self):
        return reverse('home')

class WidgetForm(ModelForm):
  class Meta:
    model = Widget
    fields = ['description', 'quantity']