from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext, loader
# Create your views here.
from django.shortcuts import render_to_response
from letsdoit.models import Poll, Choice
from rest_framework import generics, permissions
from serializers import CategorySerializer
from .models import Category


def index(request):
    letsdoit_poll = Poll.objects.order_by('-pub_date')[:5]
    template = loader.get_template('index.html')
    context = RequestContext(request, {
        'letsdoit_poll': letsdoit_poll,
    })
    return HttpResponse(template.render(context))
    #return render_to_response('index.html')


def results(request, poll_id):
    return render_to_response('results.html')


def detail(request, poll_id):
    question = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'detail.html', {'question': question})
   # return render_to_response('detail.html')


def vote(request, poll_id):
    return render_to_response('vote.html')




