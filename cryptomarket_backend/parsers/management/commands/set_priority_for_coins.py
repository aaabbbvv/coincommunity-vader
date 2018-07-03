from django.core.management import BaseCommand

from workers.models import Coin


class Command(BaseCommand):
    def handle(self, *args, **options):
        coins = Coin.objects.all().order_by('pk')
        i = 0
        for coin in coins:
            if i < 30:
                coin.parsing_day = 0
            elif i < 60:
                coin.parsing_day = 1
            elif i < 90:
                coin.parsing_day = 2
            elif i < 120:
                coin.parsing_day = 3
            elif i < 150:
                coin.parsing_day = 4
            elif i < 180:
                coin.parsing_day = 5
            else:
                coin.parsing_day = 6
            i += 1
            coin.save()
