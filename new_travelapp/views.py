from django.shortcuts import render
from django.http import HttpResponse
from .models import Place, Team


# Create your views here.
def travel_fn(request):
    obj = Place.objects.all()
    team_obj = Team.objects.all()
    # return HttpResponse("haiii")
    return render(request, 'index.html', {'result': obj, 'team': team_obj})

