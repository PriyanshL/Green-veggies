from django.shortcuts import render


# Create your views here.
def pre_home(request):
    return render(request, 'pre_home.html')

def home(request):
    return render(request, 'home.html')
