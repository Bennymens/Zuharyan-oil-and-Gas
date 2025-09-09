from django.shortcuts import render

def home(request):
	return render(request, 'main/home.html')

def about(request):
	return render(request, 'main/about.html')

def careers(request):
	return render(request, 'main/careers.html')

from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        subject = f"New Contact Form Submission from {name}"
        full_message = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

        # Send email to your company
        send_mail(
            subject,
            full_message,
            'your_email@gmail.com',  # Must match EMAIL_HOST_USER
            ['info@zuhayran.com'],   # Your company email
            fail_silently=False,
        )

        # Send confirmation to user
        send_mail(
            "Thank you for contacting Zuhayrān Oil & Gas",
            f"Dear {name},\n\nThank you for reaching out to Zuhayrān Oil & Gas. We have received your message and will get back to you as soon as possible.\n\nBest regards,\nThe Zuhayrān Team",
            'your_email@gmail.com',
            [email],
            fail_silently=False,
        )

        messages.success(request, "Your message has been sent! We'll get back to you soon.")
        return redirect('contact')
    return render(request, 'main/contact.html')
   
def services(request):
    return render(request, 'main/services.html')

# Create your views here.
