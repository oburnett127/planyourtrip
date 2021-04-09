from django.shortcuts import render
from .models import Question
from website.forms import Usr_answers
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext
from website.models import Question

def home(request, id_num):
    form = Usr_answers
    question = Question.objects.filter(id=id_num)
    if request.method == 'POST':
        if form.is_valid() and id_num < 10:
            id_num + 1
            HttpResponseRedirect("/home/{id}/".format(id=id_num), {'questions':question})
    else:
        return render(request, 'website/home.html', {'questions':question, 'ids':id_num})

    #context = RequestContext(request)
    #form_s = Usr_answers()
    #if request.method == 'POST':
        #form = usr_answer(request.POST)
        #if form.is_valid():
            #form.save()
            #return HttpResponseRedirect('/%s/', id_num+1 )
    #if request.method == 'GET':
        #return render(request, 'website/home.html', {'form':form_s, 'id_num':id_num}, context)


def cities(request):
    return render(request, 'website/cities.html')
