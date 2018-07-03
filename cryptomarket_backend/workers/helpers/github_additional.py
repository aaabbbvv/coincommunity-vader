from django.db.models import Count, Avg

from parsers.models import GitHubForks, GitHubCommit, GitHubStars


def get_value_for_github_forks(coin, last_parsing_date, date_ago):
    """Set values for github forks calculating"""
    check = GitHubForks.objects.filter(coin=coin)
    if not check:
        return None

    value = GitHubForks.objects.filter(coin=coin, date__lte=last_parsing_date,
                                       date__gte=date_ago).aggregate(Count('pk'))
    if value.get('pk__count') is None:
        result = 0
    else:
        result = value.get('pk__count')
    return result


def get_value_for_github_commits(coin, last_parsing_date, date_ago):
    """Set values for github commits calculating"""
    check = GitHubCommit.objects.filter(coin=coin)
    if not check:
        return None

    value = GitHubCommit.objects.filter(coin=coin, date__lte=last_parsing_date,
                                        date__gte=date_ago).aggregate(Count('pk'))
    if value.get('pk__count') is None:
        result = 0
    else:
        result = value.get('pk__count')
    return result


def get_value_for_github_stars(coin, last_parsing_date, date_ago):
    """Set values for github stars calculating"""
    check = GitHubStars.objects.filter(coin=coin)
    if not check:
        return None

    value = GitHubStars.objects.filter(coin=coin, date__lte=last_parsing_date,
                                       date__gte=date_ago).aggregate(Count('pk'))
    if value.get('pk__count') is None:
        result = 0
    else:
        result = value.get('pk__count')
    return result
