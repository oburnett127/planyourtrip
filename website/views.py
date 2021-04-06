from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'website/home.html')

def cities(request):
    return render(request, 'website/cities.html')

questions = ['Do you like modern Skyscrapers or prefer old architecture?', 'Would you ratehr go clubbing or visit a museum?', 'Do you like sports?',
'Do you speak English or prefer to speak other languages?', 'Do you enjoy nature-made wonders?']

answers = [['I like SkyScrapers', 'I enjoy old architecture more', 'I would go to a city that has both'],
           ['I would rather go clubbing', 'I find museums a better place to spend my time at'],
           ['Yes, I love sports', 'Not really'],
           ['I want to speak English ONLY', 'I do speak English and I like learning new languages too'],
           ['who does not?', 'I do enjoy nature, but I am more interested in men-made objects', 'Meh']
                                                                                                           ]
def questions():
    for my_questions, my_answers in zip(questions, answers)

