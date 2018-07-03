from django.db.models import Count

from parsers.models import GitHub


def get_value_for_github(coin, last_parsing_date, date_ago):
    """Set values for github repositories calculating"""
    check = GitHub.objects.filter(coin=coin)
    if not check:
        return None

    value = GitHub.objects.filter(coin=coin, date__lte=last_parsing_date,
                                  date__gte=date_ago).aggregate(Count('pk'))
    if value.get('pk__count') is None:
        result = 0
    else:
        result = value.get('pk__count')
    return result
