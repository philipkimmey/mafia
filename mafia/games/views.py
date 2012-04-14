from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404

from games.models import Game


def new(request):
    return render(request, 'new.html', {})


def init_game(request):
    return HttpResponse("html")


def game(request, pk):
    game = get_object_or_404(Game, pk=pk)
    return render(request, 'games/game.html', {'game': game})
