from parsers.models import RedditFollowers


def get_reddit_subscribers_value(coin, last_parsing_date, date_ago):
    """
    :param coin: object
    :param last_parsing_date: datetime
    :param date_ago: datetime
    :return: int, count followers
    """

    check = RedditFollowers.objects.filter(coin=coin)
    if not check:
        return None

    past_date_info = RedditFollowers.objects.filter(coin=coin, date__gte=date_ago, date__lte=last_parsing_date).order_by('date').first()

    present_info = RedditFollowers.objects.filter(coin=coin, date__lte=last_parsing_date, date__gte=date_ago).order_by('date').last()

    if past_date_info and present_info:
        count_reddit_followers = present_info.count_all - past_date_info.count_all
    else:
        count_reddit_followers = 0
    return count_reddit_followers
