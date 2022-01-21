from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addwidget/', views.WidgetCreate.as_view(), name='add_widget'),
    path('deletewidget/<int:pk>/', views.WidgetDelete.as_view(), name='delete_widget'),
    
]