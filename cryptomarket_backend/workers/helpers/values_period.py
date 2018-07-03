from django.db.models import Sum, Count

from parsers.models import GitHub, TwitterFollowers, TweetLikes, RedditFollowers, TwitterComment, MarketcapData, \
    GitHubForks, GitHubCommit, GitHubStars


def percentage(part, all):
    """Return percent"""
    try:
        if all == 0:
            return 0
        if not all:
            return None
        result = float(part) / float(all)
        return round(result * 100, 2)
    except Exception:
        return None


def get_value_github_period(coin, date_ago):
    """
    :param coin: object
    :param date_ago: datetime
    :return: int, count repos
    """
    check = GitHub.objects.filter(coin=coin)
    if not check:
        return None

    value = GitHub.objects.filter(coin=coin, date__lte=date_ago).aggregate(Count('pk'))
    if value.get('pk__count') is None:
        result = 0
    else:
        result = value.get('pk__count')
    return result


def get_reddit_subscribers_value_period(coin, date_ago):
    """
    :param coin: object
    :param date_ago: datetime
    :return: int, count followers
    """
    check = RedditFollowers.objects.filter(coin=coin)
    if not check:
        return None

    past_date_info = RedditFollowers.objects.filter(coin=coin, date__day=date_ago.day, date__month=date_ago.month,
                                                    date__year=date_ago.year).order_by('date').last()
    if not past_date_info:
        past_date_info = RedditFollowers.objects.filter(coin=coin, date__lte=date_ago).order_by('date').last()

    if past_date_info:
        return past_date_info.count_all
    else:
        return 0


def get_twitter_likes_value_period(coin, date_ago):
    """
    :param coin: object
    :param date_ago: datetime
    :return: int, twitter likes
    """
    check = TweetLikes.objects.filter(coin=coin)
    if not check:
        return None

    value = TweetLikes.objects.filter(coin=coin, date__lte=date_ago,
                                      ).aggregate(Sum('likes'))

    if value.get('likes__sum') is None:
        result = 0
    else:
        result = value.get('likes__sum')
    return result


def get_value_for_vader_period(coin, date_ago):
    """
    :param coin:
    :param date_ago:
    :return: float
    """
    check = TwitterComment.objects.filter(coin=coin)
    if not check:
        return None

    value = TwitterComment.objects.filter(coin=coin, date__lte=date_ago,
                                          ).aggregate(Sum('compound_value'))
    if value.get('compound_value__sum') is None:
        result = 0
    else:
        result = value.get('compound_value__sum')
    return result


def get_twitter_follower_value_period(coin, date_ago):
    """
    :param coin: object
    :param date_ago: datetime
    :return: int, count followers
    """
    check = TwitterFollowers.objects.filter(coin=coin)
    if not check:
        return None

    count_twitter_followers_info_v2 = TwitterFollowers.objects.filter(coin=coin, date__lte=date_ago).order_by('date').last()
    if count_twitter_followers_info_v2:
        return count_twitter_followers_info_v2.count_followers

    else:
        return 0


def get_value_for_market_cap_period(coin, date_ago):
    value = MarketcapData.objects.filter(coin=coin, date__day=date_ago.day, date__month=date_ago.month,
                                         date__year=date_ago.year).last()
    if value is None:
        result = 0
    else:
        result = value.market_cap
    return result


def get_value_github_forks_period(coin, date_ago):
    """
    :param coin: object
    :param date_ago: datetime
    :return: int, count forks
    """
    check = GitHubForks.objects.filter(coin=coin)
    if not check:
        return None

    value = GitHubForks.objects.filter(coin=coin, date__lte=date_ago).aggregate(Count('pk'))
    if value.get('pk__count') is None:
        result = 0
    else:
        result = value.get('pk__count')
    return result


def get_value_github_commits_period(coin, date_ago):
    """
    :param coin: object
    :param date_ago: datetime
    :return: int, count commits
    """
    check = GitHubCommit.objects.filter(coin=coin)
    if not check:
        return None

    value = GitHubCommit.objects.filter(coin=coin, date__lte=date_ago).aggregate(Count('pk'))
    if value.get('pk__count') is None:
        result = 0
    else:
        result = value.get('pk__count')
    return result


def get_value_github_stars_period(coin, date_ago):
    """
    :param coin: object
    :param date_ago: datetime
    :return: int, count stars
    """

    check = GitHubStars.objects.filter(coin=coin)
    if not check:
        return None

    value = GitHubStars.objects.filter(coin=coin, date__lte=date_ago).aggregate(Count('pk'))
    if value.get('pk__count') is None:
        result = 0
    else:
        result = value.get('pk__count')
    return result
