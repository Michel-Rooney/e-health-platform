from django.http import HttpResponseBadRequest, HttpResponse, HttpResponseServerError
from apps.platform_health.models import PersonData
from apps.arduino.models import HeartRateData


def heart_rate(request):
    if request.method == "GET":
        code = request.GET.get('code')
        beat = request.GET.get('beat')

        if not (code or beat):
            '''400: Server cannot or will not process the request due to 
            something that is perceived to be a client error '''
            return HttpResponseBadRequest('Error 400')
        
        try:
            heart = HeartRateData(beat=beat)
            person_data = PersonData.objects.get(person__code=code)
            heart.save()
            person_data.beats.add(heart.id)
            person_data.save()
            return HttpResponse('Saved data')
        except:
            return HttpResponseServerError('Internal Erro')