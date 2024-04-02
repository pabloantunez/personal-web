from django.contrib import admin
from .models import Certification

class CertificationAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

admin.site.register(Certification, CertificationAdmin)

