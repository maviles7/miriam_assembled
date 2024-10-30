import os
from django.shortcuts import render, redirect
from django.core.mail import send_mail
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
    prof_email = os.environ.get('EMAIL')
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Extract form data
            subject = f"Contact Miriam Form Submission: {form.cleaned_data['subject']}"
            from_email = form.cleaned_data['email']
            message_body = f"""
            new portfolio message from: {from_email}

            subject: {form.cleaned_data['subject']}

            message:
            {form.cleaned_data['message']}
            """
            
            # Sending the email
            send_mail(
                subject,
                message_body,
                from_email,
                [f"{prof_email}"],  # Replace with the recipient email
                fail_silently=False,
            )

            return redirect('contact_success')  # Redirect after successful submission
    else:
        form = ContactForm()
    
    return render(request, 'contact/contact.html', {'form': form})  # Render the form template

def contact_success(request):
    return render(request, 'contact/contact_success.html')