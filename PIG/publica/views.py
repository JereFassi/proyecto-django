from django.shortcuts import render
from .forms import ContactoForm
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from django.core.mail import send_mail

def index(request):
    if request.method == "POST":
        contacto_form = ContactoForm(request.POST)
        if contacto_form.is_valid():
            messages.info(request, "Datos enviados")

            nombre_contacto = contacto_form.cleaned_data['nombre_contacto']
            telefono = contacto_form.cleaned_data['telefono']
            email = contacto_form.cleaned_data['email']
            mensaje = contacto_form.cleaned_data['mensaje']
            asunto = 'Contacto Internet G3'

            from_email = settings.EMAIL_HOST_USER
            to_email = [settings.RECIPIENT_ADDRESS,email,]
            
            message_send = f"From: {nombre_contacto} <{email}> <{telefono}>\n Subject: {asunto}\n Message: {mensaje}"
            message_html = f"""
                <p>From: {nombre_contacto} <a href="mailto:{email}">{email}</a></p>
                <p>Subject: {asunto}</p>
                <p>Message: {mensaje}</p>
                """
            subject_send = "Email de Internet G3 - " + asunto
            send_mail(subject_send, message_send, from_email, to_email, fail_silently = False, html_message = message_html)
            messages.success(request,"Pronto nos pondremos en contacto... Gracias!")

            contacto_form = ContactoForm() # reset formulario
    else:
        contacto_form = ContactoForm()
    return render(request,'publica/index.html', {'contacto_form': contacto_form})
