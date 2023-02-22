from django.shortcuts import render, HttpResponse
from apps.platform_health.models import PersonData
from django.db.models.aggregates import Avg

def home(request):
    try:
        person_data = PersonData.objects.get(id=4).beats.all().aggregate(media=Avg('beat'))
        print(person_data)
        return HttpResponse(person_data['media'])
    except:
        return HttpResponse('Home')