from workers.helpers.main import get_coin_stats
from workers.models import TempTotalValueByPeriod, TempGrowthValues, TempTrendingValue


def get_int_or_none_value(obj, time_type, sort_type):
    value = getattr(obj, '%s_%s' % (sort_type, time_type))
    if not value:
        return 0
    else:
        return int(value)


def check_exist_result(obj, time_type, sort_type):
    value = getattr(obj, '%s_%s' % (sort_type, time_type))
    if not value:
        return 0
    else:
        return 1


def set_community_size_ranks(coin, time_type, sort_type):
    twitter_follower = get_coin_stats(coin=coin, type_rating='twitter_followers')
    twitter_likes = get_coin_stats(coin=coin, type_rating='twitter_likes')
    reddit = get_coin_stats(coin=coin, type_rating='reddit_subscribers')
    vader = get_coin_stats(coin=coin, type_rating='vader_twitter_sentiment')
    try:
        result = int((get_int_or_none_value(twitter_follower, time_type, sort_type) +
                      get_int_or_none_value(twitter_likes, time_type, sort_type) +
                      get_int_or_none_value(reddit, time_type, sort_type) +
                      get_int_or_none_value(vader, time_type, sort_type)) / (
                         check_exist_result(twitter_follower, time_type, sort_type) +
                         check_exist_result(twitter_likes, time_type, sort_type) +
                         check_exist_result(reddit, time_type, sort_type) +
                         check_exist_result(vader, time_type, sort_type)))
        rank = get_coin_stats(coin=coin, type_rating='community_size')
        setattr(rank, '%s_%s' % (sort_type, time_type), result)
        rank.save()
    except ZeroDivisionError:
        rank = get_coin_stats(coin=coin, type_rating='community_size')
        setattr(rank, '%s_%s' % (sort_type, time_type), None)
        rank.save()


def set_github_total_ranks(coin, time_type, sort_type):
    github_forks = get_coin_stats(coin=coin, type_rating='github_forks')
    github_commits = get_coin_stats(coin=coin, type_rating='github_commits')
    github_stars = get_coin_stats(coin=coin, type_rating='github_stars')
    github_repos = get_coin_stats(coin=coin, type_rating='github_repository_creations')

    check = getattr(github_commits, '%s_%s' % (sort_type, time_type))
    if not check:
        result = None
    else:
        result = int((get_int_or_none_value(github_forks, time_type, sort_type) +
                      get_int_or_none_value(github_commits, time_type, sort_type) +
                      get_int_or_none_value(github_stars, time_type, sort_type) +
                      get_int_or_none_value(github_repos, time_type, sort_type)) / 4)
    rank = get_coin_stats(coin=coin, type_rating='github_total')
    setattr(rank, '%s_%s' % (sort_type, time_type), result)
    rank.save()


def set_market_divergence_value(coin, time_type, sort_type):
    market_size = get_coin_stats(coin=coin, type_rating='marketcap_size_usd')
    github_total = get_coin_stats(coin=coin, type_rating='github_total')
    community_size = get_coin_stats(coin=coin, type_rating='community_size')
    try:
        result = float(get_int_or_none_value(market_size, time_type, sort_type) - (
            get_int_or_none_value(github_total, time_type, sort_type) +
            get_int_or_none_value(community_size, time_type, sort_type)) / (
                           check_exist_result(community_size, time_type, sort_type) +
                           check_exist_result(github_total, time_type, sort_type)))
    except ZeroDivisionError:
        result = 0

    if sort_type == 'total':
        TempTotalValueByPeriod.objects.create(coin=coin, time_type=time_type,
                                              ranking_type='marketcap_size_usd_divergence',
                                              value=result)
    elif sort_type == 'growth':
        TempGrowthValues.objects.create(coin=coin, time_type=time_type,
                                        ranking_type='marketcap_size_usd_divergence',
                                        value=result)
    elif sort_type == 'trending':
        TempTrendingValue.objects.create(coin=coin, time_type=time_type,
                                         ranking_type='marketcap_size_usd_divergence',
                                         value=result)
    else:
        return False


def set_watch_list_ranks(coin, time_type, sort_type):
    market_divergence = get_coin_stats(coin=coin, type_rating='marketcap_size_usd_divergence')
    github_total = get_coin_stats(coin=coin, type_rating='github_total')
    community_size = get_coin_stats(coin=coin, type_rating='community_size')

    result = int((get_int_or_none_value(market_divergence, time_type, sort_type) +
                  get_int_or_none_value(github_total, time_type, sort_type) +
                  get_int_or_none_value(community_size, time_type, sort_type)
                  ) / (
                     check_exist_result(market_divergence, time_type, sort_type) +
                     check_exist_result(github_total, time_type, sort_type) +
                     check_exist_result(community_size, time_type, sort_type)))
    rank = get_coin_stats(coin=coin, type_rating='watch_list')
    setattr(rank, '%s_%s' % (sort_type, time_type), result)
    rank.save()
