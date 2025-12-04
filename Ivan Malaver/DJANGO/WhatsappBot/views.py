from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from twilio.twiml.messaging_response import MessagingResponse

@csrf_exempt
def whatsapp_webhook(request):
    if request.method == "POST":
        # Twilio envía los mensajes en request.POST
        incoming_msg = request.POST.get("Body", "").lower()

        # Crear respuesta Twilio
        resp = MessagingResponse()
        msg = resp.message()

        # Respuesta simple
        msg.body(f"Su mensaje es: {incoming_msg}")

        return HttpResponse(str(resp), content_type="text/xml")

    return HttpResponse("METHOD NOT ALLOWED")



#https://averagely-gemeled-lekisha.ngrok-free.dev/whatsapp/
#Esta es la url