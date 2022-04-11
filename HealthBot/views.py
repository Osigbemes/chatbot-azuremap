from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Appointment
from .forms import AppointmentForm
# Create your views here.
def index(request):
    return render(request, 'HealthBot/HomePage.html')

def about(request):
    return render(request, 'HealthBot/about.html')

def contact(request):
    return render(request, 'HealthBot/contact.html')

def service(request):
    return render(request, 'HealthBot/service.html')

def doctor(request):
    return render(request, 'HealthBot/doctor.html')

def home(request):
    if request.method == 'POST':
        form = Appointment() # there is no need to put request.POST since it is not an instance of the model form
        if form:
            form.name=request.POST['firstName']
            form.lastName=request.POST['lastName']
            form.appointmentDate=request.POST['appointmentDate']
            form.sex=request.POST['sex']
            form.email=request.POST['email']
            form.comment=request.POST['comment']
            form.mobileNumber = request.POST['mobileNumber']
            form.save()
            messages.success(request, 'Your appointment was sent successfully!!')
            redirect ('homepage')

        if request.POST['firstName'] == '' or request.POST['email']  == '':
            messages.MessageFailure(request, 'Your appointment was not successfully, try again.')

    return render(request, 'HealthBot/HomePage.html')

def map(request):
    context={"latitude":6.5306624, "longitude":3.3816576, "query":"hospital"}
    return render(request, 'HealthBot/MapSearch.html', context)
