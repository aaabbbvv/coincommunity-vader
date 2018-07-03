import datetime

from statistic.models import RankingStatistic
from workers.helpers.difficult_types import set_community_size_ranks, set_market_divergence_value, \
    set_github_total_ranks, set_watch_list_ranks
from workers.helpers.values_period import percentage
from workers.helpers.main import get_date_ago, get_total_value_by_period, get_growth_value_by_period, get_coin_stats, \
    set_places
from workers.models import Coin,  TempGrowthValues, TempTotalValueByPeriod, TempTrendingValue

SIMPLE_RATING_TYPE_CALCULATIONS = ('twitter_followers', 'github_repository_creations', 'reddit_subscribers',
                                   'twitter_likes', 'vader_twitter_sentiment', 'github_forks', 'github_stars',
                                   'github_commits', 'marketcap_size_usd')


def calculate_rating(last_parsing_date):
    coins = Coin.objects.all()
    # delete old results
    clear_tables()
    # get dates
    week_ago = get_date_ago(last_parsing_date, 7)
    month_ago = get_date_ago(last_parsing_date, 30)
    three_month_ago = get_date_ago(last_parsing_date, 90)
    six_month_ago = get_date_ago(last_parsing_date, 180)
    year_ago = get_date_ago(last_parsing_date, 360)

    time_types = {'week': week_ago, 'month': month_ago, 'three_month': three_month_ago, 'six_month': six_month_ago,
                  'year': year_ago}

    # calculating values and save them for simple rating types
    for coin in coins:
        for simple_rating_type in SIMPLE_RATING_TYPE_CALCULATIONS:
            for key, value in time_types.items():
                # Total results for simple rating type
                result = get_total_value_by_period(simple_rating_type, coin, value)
                TempTotalValueByPeriod.objects.create(coin=coin, time_type=key, ranking_type=simple_rating_type,
                                                      value=result)
                # Save Total result for current moment
                if key == 'week':
                    result_total = get_total_value_by_period(simple_rating_type, coin, last_parsing_date)
                    statistic_rank = get_coin_stats(coin, simple_rating_type)
                    statistic_rank.total = result_total
                    statistic_rank.save()
                # Growth results for simple rating type
                growth_result = get_growth_value_by_period(simple_rating_type, coin, value, last_parsing_date)
                TempGrowthValues.objects.create(coin=coin, time_type=key, ranking_type=simple_rating_type,
                                                value=growth_result)
                # Trending results for simple rating type
                trending_value = percentage(growth_result,
                                            get_total_value_by_period(simple_rating_type, coin, week_ago))
                TempTrendingValue.objects.create(value=trending_value, coin=coin, time_type=key,
                                                 ranking_type=simple_rating_type)
    # calculating rating for simple type ratings
    for simple_rating_type in SIMPLE_RATING_TYPE_CALCULATIONS:
        for key, value in time_types.items():
            data = TempTotalValueByPeriod.objects.filter(time_type=key, ranking_type=simple_rating_type).order_by(
                '-value')
            set_places(data, simple_rating_type, 'total_%s' % key)

            data_growth = TempGrowthValues.objects.filter(time_type=key, ranking_type=simple_rating_type).order_by(
                '-value')
            set_places(data_growth, simple_rating_type, 'growth_%s' % key)

            data_trending = TempTrendingValue.objects.filter(time_type=key, ranking_type=simple_rating_type).order_by(
                '-value')
            set_places(data_trending, simple_rating_type, 'trending_%s' % key)

    # calculating rating for community size  and github total
    for coin in coins:
        for key, value in time_types.items():
            set_community_size_ranks(coin, key, 'total')
            set_community_size_ranks(coin, key, 'growth')
            set_community_size_ranks(coin, key, 'trending')

            set_github_total_ranks(coin, key, 'total')
            set_github_total_ranks(coin, key, 'growth')
            set_github_total_ranks(coin, key, 'trending')

    # calculating values for market_divergence
    for coin in coins:
        for key, value in time_types.items():
            set_market_divergence_value(coin, key, 'total')
            set_market_divergence_value(coin, key, 'growth')
            set_market_divergence_value(coin, key, 'trending')

    # calculating rating for  market_divergence
    for key, value in time_types.items():
        data = TempTotalValueByPeriod.objects.filter(time_type=key,
                                                     ranking_type='marketcap_size_usd_divergence').order_by(
            '-value')
        set_places(data, 'marketcap_size_usd_divergence', 'total_%s' % key)

        data_growth = TempGrowthValues.objects.filter(time_type=key,
                                                      ranking_type='marketcap_size_usd_divergence').order_by(
            '-value')
        set_places(data_growth, 'marketcap_size_usd_divergence', 'growth_%s' % key)

        data_trending = TempTrendingValue.objects.filter(time_type=key,
                                                         ranking_type='marketcap_size_usd_divergence').order_by(
            '-value')
        set_places(data_trending, 'marketcap_size_usd_divergence', 'trending_%s' % key)

    for coin in coins:
        for key, value in time_types.items():
            set_watch_list_ranks(coin, key, 'total')
            set_watch_list_ranks(coin, key, 'growth')
            set_watch_list_ranks(coin, key, 'trending')

    return True


def clear_tables():
    TempGrowthValues.objects.all().delete()
    TempTotalValueByPeriod.objects.all().delete()
    TempTrendingValue.objects.all().delete()
    RankingStatistic.objects.all().delete()
    return True
