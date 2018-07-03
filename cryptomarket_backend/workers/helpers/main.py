import datetime

from statistic.models import RankingStatistic
from workers.helpers.github import get_value_for_github
from workers.helpers.github_additional import get_value_for_github_forks, get_value_for_github_commits, \
    get_value_for_github_stars
from workers.helpers.marketcap import get_marketcap_value
from workers.helpers.reddit import get_reddit_subscribers_value
from workers.helpers.twitter import get_twitter_follower_value, get_twitter_likes_value, get_value_for_vader
from workers.helpers.values_period import get_twitter_follower_value_period, get_value_github_period, \
    get_reddit_subscribers_value_period, get_twitter_likes_value_period, get_value_for_vader_period, \
    get_value_for_market_cap_period, get_value_github_forks_period, get_value_github_stars_period, \
    get_value_github_commits_period


def set_places(data, type_rating, variable_name):
    """
    Set coins place by rating
    :param data: queryset
    :param type_rating: string
    :param variable_name: string
    :return:
    """
    place = 0
    temp_value = None
    for rank in data:
        ranking = get_coin_stats(coin=rank.coin, type_rating=type_rating)
        if temp_value != rank.value:
            place += 1
        setattr(ranking, variable_name, place)
        if rank.value is None:
            setattr(ranking, variable_name, None)
        ranking.save()
        temp_value = rank.value


def get_date_ago(from_date, count_days):
    """
    :param from_date: datetime, init day
    :param count_days: int, count day before from_date
    """
    day = from_date - datetime.timedelta(days=count_days)
    return day


def get_coin_stats(coin, type_rating):
    """
    Return a object  for set places
    :param type_rating:
    :param coin: object
    :return: object
    """
    rank = RankingStatistic.objects.filter(coin=coin, type=type_rating).last()
    if rank:
        return rank
    else:
        rank = RankingStatistic.objects.create(coin=coin, type=type_rating)
        return rank


def get_total_value_by_period(type_ranking, coin, date_ago):
    """
    Set total results
    :param type_ranking:
    :param coin:
    :param date_ago:
    :return:
    """
    if type_ranking == 'twitter_followers':
        return get_twitter_follower_value_period(coin, date_ago)
    elif type_ranking == 'github_repository_creations':
        return get_value_github_period(coin, date_ago)
    elif type_ranking == 'reddit_subscribers':
        return get_reddit_subscribers_value_period(coin, date_ago)
    elif type_ranking == 'twitter_likes':
        return get_twitter_likes_value_period(coin, date_ago)
    elif type_ranking == 'vader_twitter_sentiment':
        return get_value_for_vader_period(coin, date_ago)
    elif type_ranking == 'marketcap_size_usd':
        return get_value_for_market_cap_period(coin, date_ago)
    elif type_ranking == 'github_forks':
        return get_value_github_forks_period(coin, date_ago)
    elif type_ranking == 'github_stars':
        return get_value_github_stars_period(coin, date_ago)
    elif type_ranking == 'github_commits':
        return get_value_github_commits_period(coin, date_ago)
    else:
        return None


def get_growth_value_by_period(type_ranking, coin, date_ago, last_parsing_date):
    """
    Set growth results
    :param type_ranking:
    :param coin:
    :param date_ago:
    :return:
    """
    if type_ranking == 'twitter_followers':
        return get_twitter_follower_value(coin, last_parsing_date, date_ago)
    elif type_ranking == 'github_repository_creations':
        return get_value_for_github(coin, last_parsing_date, date_ago)
    elif type_ranking == 'reddit_subscribers':
        return get_reddit_subscribers_value(coin, last_parsing_date, date_ago)
    elif type_ranking == 'twitter_likes':
        return get_twitter_likes_value(coin, last_parsing_date, date_ago)
    elif type_ranking == 'vader_twitter_sentiment':
        return get_value_for_vader(coin, last_parsing_date, date_ago)
    elif type_ranking == 'marketcap_size_usd':
        return get_marketcap_value(coin, last_parsing_date, date_ago)
    elif type_ranking == 'github_forks':
        return get_value_for_github_forks(coin, last_parsing_date, date_ago)
    elif type_ranking == 'github_stars':
        return get_value_for_github_stars(coin, last_parsing_date, date_ago)
    elif type_ranking == 'github_commits':
        return get_value_for_github_commits(coin, last_parsing_date, date_ago)
    else:
        return None
