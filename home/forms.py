from django import forms
from .models import Booking

class DateInput(forms.DateInput):
    input_type = 'date'

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'
        # Indent this so it belongs to the Meta class!
        widgets = {
            'booking_date': DateInput(),
        }
        labels ={
    'p_name':"patient Name",
    'p_phone':"Phone number",
    'p_email':"Patiant email",
    'doc_name':"Doctor name",
    'booking_date':"Booking date",
  
    
        }