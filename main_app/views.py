from venv import create
from .models import Widget
from django.db.models import Sum
from django.forms import widgets
from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView
from .forms import WidgetForm

# Create your views here.

def index(request):
    widgets = Widget.objects.all()
    widget_form = WidgetForm()
    total_quantity = Widget.objects.all().aggregate(Sum('quantity')).get('quantity__sum')
    
    return render(request, 'index.html', {'widgets': widgets, 'widget_form': widget_form,'total_quantity':total_quantity })

class WidgetCreate(CreateView):
    model = Widget
    fields = "__all__"
    success_url = "/"

class WidgetDelete(DeleteView):
  model = Widget
  success_url = '/'