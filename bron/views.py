from django.shortcuts import render
from .models import Bron


def index(request):
    brons = Bron.objects.all()
    context = {'brons': brons}
    if request.user.is_superuser:
        if request.method == 'POST':
            confirm = request.POST.get('confirm')
            bron_id = request.POST.get('bron_id')
            bron = Bron.objects.get(pk=bron_id)
            if confirm == 'on':
                bron.admin_confirmed = True
                bron.save()
            else:
                bron.admin_confirmed = False
                bron.save()

    return render(request, 'home.html', context=context)
