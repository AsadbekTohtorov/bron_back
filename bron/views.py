from django.shortcuts import render
from .models import Bron


def index(request):
    brons = Bron.objects.all()
    context = {'brons': brons}
    if request.user.is_superuser:
        if request.method == 'POST':
            if request.POST.get('form1'):
                confirm = request.POST.get('confirm')
                bron_id = request.POST.get('bron_id')
                bron = Bron.objects.get(id=bron_id)
                if confirm == 'on':
                    bron.admin_confirmed = True
                    bron.save()
                else:
                    bron.admin_confirmed = False
                    bron.save()

    if request.method == 'POST':
        if request.POST.get('form2'):
            origin = request.POST.get('origin')
            destination = request.POST.get('destination')
            date = request.POST.get('date')
            departure_time = request.POST.get('departure_time')
            arrival_time = request.POST.get('arrival_time')

            Bron.objects.create(
                origin=origin,
                destination=destination,
                date=date,
                departure_time=departure_time,
                arrival_time=arrival_time

            )
    return render(request, 'home.html', context=context)
