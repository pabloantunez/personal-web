from typing import Any
from django.shortcuts import render
from django.views.generic.list import ListView 
from django.views.generic.detail import DetailView
from .models import Project
from django.http import HttpResponse
from django.conf import settings

class PortfolioListView(ListView):
    model = Project

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['image'] = '/static/portfolio/images/portfolio_image.jpg'
        context['projects'] = self.get_queryset() # Obtengo los proyectos
        context['image_description'] = 'Portfolio Image'
        context['overlay_text'] = 'Portfolio'
        return context

class ProjectDetailView(DetailView):
    model = Project

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['is_project_view'] = True
        return context