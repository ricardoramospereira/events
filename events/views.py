from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Event
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.contrib import messages
from django.http import Http404


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
        
@login_required
def manage_event(request):
    if request.method == "GET":
        name = request.GET.get('name')
        events = Event.objects.filter(creator=request.user)

        if name:
            events = events.filter(name__contains=name)

        return render(request, 'manage_event.html', {'events': events})
    
@login_required
def register_event(request, id):
    # validate login
    event = get_object_or_404(Event, id=id)
    if request.method == "GET":
        return render(request, 'register_event.html', {'event': event})
    elif request.method == "POST":
        event.participant.add(request.user)
        event.save()

        messages.add_message(request, constants.SUCCESS, "Inscrição realizada com sucesso")
        return redirect(f'/events/register_event/{id}/')
    
def event_participant(request, id):
    event = get_object_or_404(Event, id=id)
    if not event.creator == request.user:
        raise Http404('Esse evento não é seu')
    if request.method == "GET":
        participants = event.participant.all()[::3]
        return render(request, 'event_participant.html', {'event': event, 'participants': participants})
