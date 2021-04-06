from django.shortcuts import render
from .models import Question
# Create your views here.
def home(request):
    context = {
        'questions': Question.objects.all()
    }
    return render(request, 'website/home.html', context)

def cities(request):
    return render(request, 'website/cities.html')


