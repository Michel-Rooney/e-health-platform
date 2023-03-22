from django.shortcuts import render, redirect, HttpResponse
from apps.platform_health.models import PersonData
from django.db.models.aggregates import Avg, Sum
from django.views.decorators.clickjacking import xframe_options_sameorigin
from .utils import contact_is_valid
from utils.utils import send_email
from django.contrib.auth.decorators import login_required
from .models import Doctor, Person, Note
from django.contrib import messages
from datetime import datetime
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt




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

    return render(request, 'pages/patient.html', {
        'person':person, 'data':person_data, 
        'doctor':doctor, 'beats':beats['media']
    })

@login_required(login_url='/auth/login')
@csrf_exempt
def patient_chart(request, id):
    person = PersonData.objects.filter(id=id).first()
    beats = [beat.beat for beat in person.beats.all().order_by('-id')]
    labels = list(range(len(beats[9::-1])))
    data = {'beats':beats[9::-1], 'labels':labels}
    return JsonResponse(data)
    

@login_required(login_url='/auth/login')
def del_note(request, id):
    note = Note.objects.filter(id=id).first()
    note.delete()
    messages.success(request, 'Nota deletada com sucesso')
    return redirect(f'/patient/{note.person.id}/')

@login_required(login_url='/auth/login')
def create_note(request, id):
    note = request.POST.get('note')

    notes = Note(person_id=id, note=note, date=datetime.now())
    notes.save()
    person = PersonData.objects.filter(person_id=id).first()
    person.notes.add(notes.id)
    return redirect(f'/patient/{notes.person.id}/')

@login_required(login_url='/auth/login')
def update_information(request, id):
    profile_picture = request.FILES.get('profile-picture')
    username = request.POST.get('username')
    email = request.POST.get('email')
    phone_number = request.POST.get('phone-number')
    adress = request.POST.get('adress')
    height = float(request.POST.get('height'))
    weight = float(request.POST.get('weight'))

    person = Person.objects.filter(id=id).first()    
    person.phone_number = phone_number
    person.address = adress

    if not person.profile_picture.url == '/media/profile_default.png':
        person.profile_picture.delete()
    person.profile_picture = profile_picture
    person.save()

    user = User.objects.filter(id=person.user.id).first()
    user.username = username
    user.email = email
    user.save()
    
    person_data = PersonData.objects.filter(person_id=id).first()
    person_data.height = height
    person_data.weight = weight
    person_data.save()
    
    messages.success(request, 'Informações atualizadas com sucesso')
    return redirect(f'/patient/{person.id}/')

@login_required(login_url='/auth/login')
def management_doctors(request):
    person = Person.objects.filter(user_id=request.user.id).first()
    people = Person.objects.filter(level='P')
    doctors = Person.objects.filter(level='D')
    return render(request, 'pages/management_doctors.html', {
        'person': person, 'people': people, 'doctors': doctors
    })

@login_required(login_url='/auth/login')
def management_doctors_add(request):
    if request.method == 'POST':
        people = request.POST.getlist('select-doctor')

        try:
            for id in people:
                person = Person.objects.filter(id=id).first()
                person.level = 'D'
                person.save()
                doctor = Doctor(person=person)
                doctor.save()
            messages.success(request, 'Tarefa realizada com sucesso')
            return redirect('/management/doctors')
        except:
            messages.error(request, 'Erro interno do sistema')
            return redirect('/management/doctors')

@login_required(login_url='/auth/login')
def management_doctors_remove(request):
    if request.method == 'POST':
        people = request.POST.getlist('select-person')

        try:
            for id in people:
                person = Person.objects.filter(id=id).first()
                person.level = 'P'
                person.save()
                doctor = Doctor.objects.filter(person=person).first()
                doctor.delete()
            messages.success(request, 'Tarefa realizada com sucesso')
            return redirect('/management/doctors')
        except:
            messages.error(request, 'Erro interno do sistema')
            return redirect('/management/doctors')
        
@login_required(login_url='/auth/login')
def management_patients(request):
    doctor = request.GET.get('select-doctor')
    if not doctor:
        doctor = Person.objects.first().id

    person = Person.objects.filter(user_id=request.user.id).first()
    if not person.level == 'A':
        messages.error(request, 'Apenas adiministradores podem acessar essa página')
        return redirect(f'/patient/{person.id}')

    people = PersonData.objects.filter(person__level='P', doctor=None)
    doctors = Person.objects.filter(level='D')
    try:
        patients = Doctor.objects.filter(person__id=doctor).first().patients.all()
    except:
        patients = []
    return render(request, 'pages/management_patients.html', {
        'person_id': person, 'people':people, 'doctors': doctors, 
        'id_doctor': int(doctor), 'patients': patients
    })

@login_required(login_url='/auth/login')
def management_patients_add(request, id):
    if request.method == 'POST':
        patients = request.POST.getlist('select-person')
        doctor = Doctor.objects.filter(person__id=id).first()


        try:
            for patient_id in patients:
                person = PersonData.objects.filter(id=patient_id).first()
                person.doctor = doctor
                person.save()
                doctor.patients.add(person.id)
                doctor.save()
            messages.success(request, 'Pacientes adicionados com sucesso')
            return redirect(f'/management/patients')
        except:
            messages.error(request, 'Erro interno do sistema')
            return redirect('/management/patients')

@login_required(login_url='/auth/login')
def management_patients_remove(request, id):
    if request.method == 'POST':
        patients = request.POST.getlist('select-patient')
        doctor = Doctor.objects.filter(person__id=id).first()

        try:
            for patient_id in patients:
                person = PersonData.objects.filter(id=patient_id).first()
                person.doctor = None
                person.save()
                doctor.patients.remove(person.id)
                doctor.save()
            messages.success(request, 'Pacientes removido com sucesso')
            return redirect('/management/patients')
        except:
            messages.error(request, 'Erro interno do sistema')
            return redirect('/management/patients')


@xframe_options_sameorigin
def page2(request):
    person_data = PersonData.objects.get(id=2).beats.all().aggregate(media=Sum('beat'))
    return render(request, 'page2.html', {'data':person_data['media']})