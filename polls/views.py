from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext,loader

from polls.models import Poll

def index(request):
    latest_poll_list = Poll.objects.order_by('-pub_date')[:5}
    template = loader.get_template('polls/index.html')
    context = RequestContext(requst,{'latest_poll_list':latest_poll_list,})

    return HttpResponse(template.render(context))

def detail(request,poll_id):
    return HttpResponse("you're looking at poll %s." %poll_id)

def results(request,poll_id):
    return HttpResponse("you're looking at results of poll %s." %poll_id)

def vote(request,poll_id):
    return HttpResponse("you're voting on poll %s." %poll_id)

