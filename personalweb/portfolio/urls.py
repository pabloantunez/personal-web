from django.urls import path
from .views import PortfolioListView, ProjectDetailView

portfolio_patterns = ([
    path('',PortfolioListView.as_view(), name='projects'),
    path('<int:pk>/<slug:project_slug>',ProjectDetailView.as_view(), name='project'),
], 'projects')