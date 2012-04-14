from django.contrib.auth.models import User
from games.models import Game
from django.template import RequestContext
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_protect

from games.forms import GameForm

def new(request):
    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():
            game = Game.objects.create(
                                            max_participants=form.cleaned_data['num_participants']
                                            )
            print '#part.' + form.cleaned_data['num_participants']
            print '#part.' + game.max_participants
            return render(request, 'created.html', {'game': game})
    else:
        return render(request, 'new.html', {})


def init_game(request):
    return HttpResponse("html")


def game(request, pk):
    game = get_object_or_404(Game, pk=pk)
    return render(request, 'games/game.html', {'game': game})
