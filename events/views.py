from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Event
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.contrib import messages


# Create your views here.
@login_required
def events(request):
    if request.method == "GET":
        return render(request, 'new_event.html')
    elif request.method == "POST":
        name         = request.POST.get('name')
        description  = request.POST.get('description')
        start_date   = request.POST.get('start_date')
        final_date   = request.POST.get('final_date')
        workload     = request.POST.get('workload')
        logo         = request.POST.get('workload')

        primary_color    = request.POST.get('primary_color')
        secondary_color  = request.POST.get('secondary_color')
        background_color = request.POST.get('background_color')

        logo = request.FILES.get('logo')

        event = Event(
            creator=request.user,
            name=name,
            description=description,
            start_date=start_date,
            final_date=final_date,
            workload=workload,
            logo=logo,
        )

        event.save()
        messages.add_message(request, constants.SUCCESS, "Empresa cadastrada com sucesso")
        return redirect('new_event')
        

def manage_event(request):
    if request.method == "GET":
        events = Event.objects.filter(creator=request.user)
        return render(request, 'manage_event.html', {'events': events})