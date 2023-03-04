from django.shortcuts import render, HttpResponse
from apps.platform_health.models import PersonData
from django.db.models.aggregates import Avg, Sum
from django.views.decorators.clickjacking import xframe_options_sameorigin

def home(request):
    try:
        person_data = PersonData.objects.get(id=4).beats.all().aggregate(media=Avg('beat'))
        print(person_data)
        return HttpResponse(person_data['media'])
    except:
        return HttpResponse('Home')
    

def page1(request):
    return render(request, 'page1.html')

@xframe_options_sameorigin
def page2(request):
    person_data = PersonData.objects.get(id=2).beats.all().aggregate(media=Sum('beat'))
    return render(request, 'page2.html', {'data':person_data['media']})