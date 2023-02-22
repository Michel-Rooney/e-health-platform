from apps.platform_health.models import Doctor
from twilio.rest import Client
from decouple import config


def alert_the_doctor(person, message):
    account_sid = config('ACCOUNT_SID')
    auth_token = config('AUTH_TOKEN')
    twilio_phone_number = config('TWILIO_PHONE_NUMBER')

    try:
        doctor = Doctor.objects.get(id=person.doctor.id)
        doctor_phone_number = doctor.person.phone_number
    except:
        doctor_phone_number = person.person.phone_number

    client = Client(account_sid, auth_token)
    client.messages.create(from_=twilio_phone_number, body='teste', to=doctor_phone_number)