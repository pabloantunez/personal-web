from django.shortcuts import render
from django.views.generic.base import TemplateView

def home(request):
    context = {
        'image':'static/core/images/Desk_front.jpg',
        'about_image':'core/images/Hola.jpg',
        'contact_image':'core/images/Contact.jpg',
        'portfolio_image':'core/images/Portfolio.jpg',
        'certifications_image':'core/images/Test.jpg',
        'image_description':'Pablo Antúnez home',
        'overlay_text': 'Pablo Antúnez',
        }
    return render(request,'core/home.html', context)

def about(request):
    context = {
        'profile_image':'core/images/Me2.jpg'
    } 
    return render(request,'core/about-me.html', context)



