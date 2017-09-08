from django.contrib import admin
from .models import Journal, Conference, Faculty, Externalfp, Facultyifp, Studentifp

# Register your models here.
admin.site.register(Journal)
admin.site.register(Conference)
admin.site.register(Faculty)
admin.site.register(Externalfp)
admin.site.register(Facultyifp)
admin.site.register(Studentifp)
