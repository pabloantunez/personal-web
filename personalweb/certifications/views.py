from typing import Any
from django.shortcuts import render
from .models import Certification
from django.views.generic.list import ListView 

class CertificationsListView(ListView):
    model = Certification

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['background_image'] = '/static/certifications/images/Certification.jpg'
        context['certifications'] = self.get_queryset()
        return context
