from django.urls import path
from .import views

urlpatterns = [
    path('new_event/', views.events, name='new_event'),
    path('manage_event/', views.manage_event, name='manage_event'),
    path('register_event/<int:id>/', views.register_event, name='register_event'), 
    path('event_participant/<int:id>/', views.event_participant, name='event_participant'), 
]