from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'website/home.html')

def cities(request):
    return render(request, 'website/cities.html')


def ss(request):
    return render(request, 'website/cities.html')

