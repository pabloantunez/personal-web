from django.shortcuts import render
from django.views.generic.base import TemplateView

def home(request):
    return render(request,'core/home.html',{
        'image_root':'core/images/Desk_front.jpg',
        'about_image':'core/images/Hola.jpg',
        'contact_image':'core/images/Contact.jpg',
        'portfolio_image':'core/images/Portfolio.jpg',
        'certifications_image':'core/images/Test.jpg'
        })


