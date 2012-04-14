from django.core.management.base import BaseCommand

from games.models import Game


class Command(BaseCommand):
    def handle(self, *args, **options):
        for i in range(5):
            Game.objects.create(public=True)
