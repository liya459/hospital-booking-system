from django.contrib import admin
from .models import Department, Doctor, Booking

admin.site.register(Department)


class DoctorAdmin(admin.ModelAdmin):
    list_display = ('id', 'doc_name', 'dep_name')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        
        
        if request.user.is_superuser:
            return qs
            
        return qs.filter(admin_user=request.user)

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        if obj and obj.admin_user == request.user:
            return True
        return False

admin.site.register(Doctor, DoctorAdmin)



class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'p_name', 'p_phone', 'p_email', 'doc_name', 'booking_date', 'booked_on')
    search_fields = ('p_name', 'p_phone')
    list_filter = ('booking_date',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        
        if request.user.is_superuser:
            return qs
            
        try:
            current_doctor = Doctor.objects.get(admin_user=request.user)
            return qs.filter(doc_name=current_doctor)
        except (Doctor.DoesNotExist, AttributeError):
            return qs.none()

admin.site.register(Booking, BookingAdmin)