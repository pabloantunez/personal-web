from django.urls import path
from .views import CertificationsListView

certification_patterns = ([
    path('',CertificationsListView.as_view(), name='certifications'),
], 'certifications')