from django.db.models import Avg

from parsers.models import MarketcapData
from workers.models import Coin, TempGrowthValues


def get_value_for_market_cap(coin, last_parsing_date, date_ago):
    """
    :param coin:
    :param last_parsing_date:
    :param date_ago:
    :return:
    """
    value = MarketcapData.objects.filter(coin=coin, date__day=date_ago.day, date__month=date_ago.month,
                                         date__year=date_ago.year).last()
    if not value:
        result = 0
    else:
        result = value.market_cap
    return result


def get_marketcap_value(coin, date_ago, last_parsing_date):
    past_date_info = MarketcapData.objects.filter(coin=coin, date__day=date_ago.day, date__month=date_ago.month,
                                                  date__year=date_ago.year).last()
    present_info = MarketcapData.objects.filter(coin=coin, date__day=last_parsing_date.day,
                                                date__month=last_parsing_date.month,
                                                date__year=last_parsing_date.year).last()
    try:
        if present_info and past_date_info:
            return present_info.market_cap - past_date_info.market_cap
        else:
            return 0
    except Exception:
        return None
