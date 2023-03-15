from django.shortcuts import render, redirect, HttpResponse
from apps.platform_health.models import PersonData
from django.db.models.aggregates import Avg, Sum
from django.views.decorators.clickjacking import xframe_options_sameorigin
from .utils import contact_is_valid
from utils.utils import send_email
from django.contrib.auth.decorators import login_required
from .models import Doctor, Person
from django.contrib import messages

# def home(request):
#     try:
#         person_data = PersonData.objects.get(id=4).beats.all().aggregate(media=Avg('beat'))
#         print(person_data)
#         return HttpResponse(person_data['media'])
#     except:
#         return HttpResponse('Home')
    

# def page1(request):
#     return render(request, 'page1.html')

# @xframe_options_sameorigin
# def page2(request):
#     person_data = PersonData.objects.get(id=2).beats.all().aggregate(media=Sum('beat'))
#     return render(request, 'page2.html', {'data':person_data['media']})

def home(request):
    if request.method == 'GET':
        return render(request, 'pages/home.html')
    elif request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        if not contact_is_valid(request, name, email, phone, message):
            return redirect('/')
        
        path_template = 'emails/contate_me.html'
        send_email(path_template, 'Contate-me', ['contatestedeteste30@gmail.com'], name=name, email=email, phone=phone, message=message)
        return redirect('/')
        
@login_required(login_url='/auth/login')
def patients(request):
    if request.method == 'GET':
        person = Person.objects.filter(user__id=request.user.id).first()
        if not person.level == 'D':
            messages.error(request, 'Apenas médicos podem acessar essa página')
            return redirect('/')
        
        doctor = Doctor.objects.filter(person=person).first()
        return render(request, 'pages/patients.html', {'patients': doctor.patients.all})
    
@login_required(login_url='/auth/login')
def patient(request, id):
    person = Person.objects.filter(id=id).first()
    if Person.objects.filter(user__id=request.user.id).first().level == 'D':
        doctor = True
    else:
        doctor = False
    person_data = PersonData.objects.filter(person=person).first()
    beats = PersonData.objects.get(person=person).beats.all().aggregate(media=Avg('beat'))
    return render(request, 'pages/patient.html', {'person':person, 'data':person_data, 'doctor':doctor, 'beats':beats['media']})