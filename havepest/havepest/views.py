from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse
from home.models import Content

def index(request):
	info = {}
	
	info['phone_number'] = Content.objects.get(pk=1)
	info['content'] = Content.objects.get(pk=2)
	info['address'] = Content.objects.get(pk=3)
	
	return render(request, 'homepage/index.html', { 'info': info })

def contact(request):
	message = ""
	if request.method == "POST":
		name = request.POST['name']
		phone = request.POST['phone']
		address = request.POST['address']
		zip = request.POST['zip']
		email = request.POST['email']
		preferred = request.POST['preferred']
		msg = 'Name: ' + name + '\nPhone: ' + phone + '\nAddress: ' + address + '\nZip: ' + zip + '\nEmail: ' + email + '\nPreferred Day/Time: ' + preferred + '\n\nMessage: \n' + request.POST['message']
		
		recipients = ['alan@alanbeam.net', 'sales@havepest.net']
		
		send_mail('HavePest.net Contact Message from ' + name, msg, email, recipients)
		
		message = "Your message has been successfully sent." 
	return HttpResponse(message, content_type="application/plaintext")

