from django.contrib import admin
from .models import Poster,Patient,Doctor,DoctorDetails


admin.site.register(Poster)
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(DoctorDetails)



