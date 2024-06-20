from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'Dz_1/home.html')


def about(request):
    return render(request, 'Dz_1/about.html')


def contact(request):
    return render(request, 'Dz_1/contact.html')


def services(request):
    return render(request, 'Dz_1/services.html')
