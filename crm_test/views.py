#from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
import json

@csrf_exempt
def whatsapp_webhook(request):
    print(f"Request body: {request.body}\n")
    if request.method == 'GET':
        # Verificación inicial de Facebook
        verify_token = 'this_is_not_my_real_token_123'
        if request.GET.get('hub.verify_token') == verify_token:
            return HttpResponse(request.GET.get('hub.challenge'), status=200)
        return JsonResponse({'error': 'Token invalido'}, status=403)

    elif request.method == 'POST':
        data = json.loads(request.body)

        # Ejemplo: capturar el mensaje recibido
        try:
            entry = data['entry'][0]
            print(entry)
            message_data = entry['changes'][0]['value']['messages'][0]
            phone = message_data['from']
            text = message_data['text']['body']
            # Aquí puedes guardar en tu modelo Contact / Interaction
        except KeyError:
            return JsonResponse({'error':'Mensaje no capturado'})  # mensaje no válido o delivery notification

        return JsonResponse({'status': 'recieved'}, status=200)
    else:
        return JsonResponse({'status':'recieved', 'method': request.method}, status=200)

