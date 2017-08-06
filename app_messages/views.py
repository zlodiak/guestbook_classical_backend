from django.shortcuts import render
from django.utils import timezone
from django.http import JsonResponse
from django.core import serializers
import json
from django.template.context_processors import csrf

from .models import Message


def form(request):
	token={}
	token.update(csrf(request))	
	print(token);
	print('--------------------------------');
	print(csrf(request));
	return render(request, 'app_messages/form.html', {'test': 'trrr', 'token': token})

def form_render(request):
	print('form_render--------------------')
	data = json.dumps({ 'example': 'exxample' , 'example2': 'exxample2' })
	return JsonResponse(data, safe=False)    

def index(request):
	messages = Message.objects.all()   
	messages_serialized = serializers.serialize('json', messages)
	return JsonResponse(messages_serialized, safe=False)     

def create(request):
		if (len(request.POST['message']) > 200) or (len(request.POST['name']) > 60):
			status = '0'
			error_message = 'Хакир штоль?'
		else:
			status = '1'
			error_message = ''
			m = Message(name=request.POST['name'], text=request.POST['message'], created_date_unix=request.POST['created_date_unix'], published_date=timezone.now(), created_date=timezone.now(),)
			m.save();

		data = json.dumps({ 'status': status , 'error_message': error_message })

		return JsonResponse(data, safe=False)  	