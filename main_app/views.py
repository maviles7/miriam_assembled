from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .models import Projects
from .models import Engineer
from .forms import ContactForm

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    engineer = Engineer.objects.all
    return render(request, 'about.html', {'engineer': engineer })

def projects_index(request):
    projects = Projects.objects.all()
    return render(request, 'projects/project_index.html', {'projects': projects}) 

def projects_detail(request, project_id):
    project = Projects.objects.get(id=project_id)
    return render(request, 'projects/project_detail.html', {'project': project})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            # Prepare the email
            subject = f"Contact Form Submission from {name}"
            body = f"Message from {name} ({email}):\n\n{message}"
            recipient_list = ['recipient@example.com']  # Replace with your recipient email
            
            # Send the email
            send_mail(subject, body, settings.EMAIL_HOST_USER, recipient_list)
            
            # Optionally, redirect or display a success message
            return render(request, 'contact/contact_success.html')  # A template for success message
    else:
        form = ContactForm()
    
    return render(request, 'contact/contact.html', {'form': form})  # Render the form template

def contact_success(request):
    return render(request, 'contact/contact_success.html')