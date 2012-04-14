from django.contrib.auth.models import User
from django.template import RequestContext
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import get_object_or_404


def new(request):
    return render(request, 'new.html', {})


def init_game(request):
    return HttpResponse("html")


def game(request, pk):
    game = get_object_or_404(Game, pk=pk)
    return render(request, 'games/game.html', {'game': game})
