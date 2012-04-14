from django.contrib.auth.models import User
from django.template import RequestContext
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import render_to_response


def new(request):
    return render(request, 'new.html', {})

def init_game(request):
    return HttpResponse("html")