from django.db.models import Sum

from parsers.models import TwitterFollowers, TwitterComment, TweetLikes


def get_twitter_follower_value(coin, last_parsing_date, date_ago):
    """
    :param coin: object
    :param last_parsing_date: datetime
    :param date_ago: datetime
    :return: int, count followers
    """
    check = TwitterFollowers.objects.filter(coin=coin)
    if not check:
        return None
    count_twitter_followers_info_v1 = TwitterFollowers.objects.filter(coin=coin, date__lte=last_parsing_date).order_by('date').last()

    count_twitter_followers_info_v2 = TwitterFollowers.objects.filter(coin=coin, date__gte=date_ago).order_by('date').first()
    if count_twitter_followers_info_v2:
            count_twitter_followers = count_twitter_followers_info_v1.count_followers - \
                                      count_twitter_followers_info_v2.count_followers
    else:
        count_twitter_followers = 0
    return count_twitter_followers


def get_twitter_likes_value(coin, last_parsing_date, date_ago):
    """
    :param coin: object
    :param last_parsing_date: datetime
    :param date_ago: datetime
    :return: int, count followers
    """
    check = TweetLikes.objects.filter(coin=coin)
    if not check:
        return None

    value = TweetLikes.objects.filter(coin=coin, date__lte=last_parsing_date,
                                      date__gte=date_ago).aggregate(Sum('likes'))

    if value.get('likes__sum') is None:
        result = 0
    else:
        result = value.get('likes__sum')
    return result


def get_value_for_vader(coin, last_parsing_date, date_ago):
    """
    :param coin:
    :param last_parsing_date:
    :param date_ago:
    :return:
    """
    check = TwitterComment.objects.filter(coin=coin)
    if not check:
        return None

    value = TwitterComment.objects.filter(coin=coin, date__lte=last_parsing_date,
                                          date__gte=date_ago).aggregate(Sum('compound_value'))
    if value.get('compound_value__sum') is None:
        result = 0
    else:
        result = value.get('compound_value__sum')
    return result
