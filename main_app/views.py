from .models import Widget
from django.forms import widgets
from django.shortcuts import render

# Create your views here.

def index(request):
    widgets = Widget.objects.all()
    return render(request, 'index.html', {'widgets': widgets})