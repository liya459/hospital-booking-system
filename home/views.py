from django.shortcuts import render
from django.http import HttpResponse
from .models import Department, Doctor
from .forms import BookingForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def booking(request):
    if request.method == "POST":
        form = BookingForm(request.POST) 
        if form.is_valid():
          
            appointment = form.save()
            
            
            return render(request, 'confirmation.html', {'appointment': appointment})
            
    else:
        form = BookingForm()
        
    dict_form = {
        'form': form
    }
    return render(request, 'booking.html', dict_form)

def doctor_view(request):
    dict_docs = {
        'doctors': Doctor.objects.all()
    }
    return render(request, 'doctors.html', dict_docs)

def department(request):
    dict_dept = {
        'dept': Department.objects.all()
    }
    return render(request, 'Department.html', dict_dept)

def condact(request):
    return render(request, 'condact.html')