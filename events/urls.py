from django.urls import path
from .import views

urlpatterns = [
    path('new_event/', views.events, name='new_event'),
    path('manage_event/', views.manage_event, name='manage_event')
]