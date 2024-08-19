from django.shortcuts import render
from django.core.mail import EmailMessage,send_mail
from django.conf import settings 
from django.template.loader import render_to_string
from .models import Contact

# Create your views here.
def contact(request):
    thank = False
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        thank = True

        template1=render_to_string('contactemail.html',{'name':name,})

        email = EmailMessage('your query is submitted', template1, to=[email])
        email.send()

    return render(request, 'contact.html', {'thank': thank})