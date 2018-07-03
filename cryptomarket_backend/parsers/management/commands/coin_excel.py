import datetime
import os
import xlrd
from django.core.management import BaseCommand
import urllib
from workers.models import Coin
from core.settings.base import MEDIA_ROOT
import time

def check_value(short_name):
    try:
        Coin.objects.get(short_name=short_name)
        return False
    except Exception:
        return True


def check_url(string):
    if string.find('?') >= 0:
        return string.split('?')[0]
    if string.find('http') < 0:
        return None
    return string


def get_image(url):
    if url is None:
        return None
    slug = url.replace('https://s2.coinmarketcap.com/static/img/coins/32x32/', '')
    if os.path.exists('%s/%s' % (MEDIA_ROOT, slug)) is False:
        urllib.request.urlretrieve(url.replace('32x32', '128x128'), '%s/%s' % (MEDIA_ROOT, slug))
        return slug


def get_info(obj_list, g):
    for i in g.doc.select('//div[@class="org-repos repo-list"]/li/div/h3/a/@href').selector_list:
        # time.sleep()
        g.go('https://github.com%s' % i.text())
        a = g.doc.select('//span[@class="num text-emphasized"]').selector_list
        obj_list.append([i.text(), a[0].text()])
    return obj_list


class Command(BaseCommand):
    def handle(self, *args, **options):
        # from workers.models import Coin
        # from parsers.scrapers.twitter_comments_vader import scrapped_twitter_comment_vader
        # from parsers.scrapers.github import scrapped_github_repositories
        # from parsers.scrapers.github_forks import scrapped_github_fork_for_date
        coin = Coin.objects.get(title='Litecoin')
        from core.settings.base import ACCESS_TOKEN_GITHUB_COMMITS
        from core.settings.base import ACCESS_TOKEN_GITHUB_FORKS
        # HEADERS = {
        #     'Authorization': 'token %s' % ACCESS_TOKEN_GITHUB_FORKS,
        # }

        # from grab import Grab
        # i = 1
        # url_main = 'https://github.com/ethereum?page=%s' % i
        #
        # g = Grab(timeout=90, connect_timeout=90)
        # # g.setup(headers=HEADERS)
        # g.go(url_main)
        # z = len(g.doc.select('//div[@class="pagination"]/a'))
        # obj_list = []
        # obj_list = get_info(obj_list, g)
        # while True:
        #     if i > z:
        #         break
        #     time.sleep(10)
        #     i += 1
        #     g.go('https://github.com/ethereum?page=%s' % i)
        #     obj_list = get_info(obj_list, g)
        #
        # print('end')
        from parsers.scrapers.twitter_followers_socialblade import scrapped_twitter_followers_socialblade
        for i in Coin.objects.all():
            scrapped_twitter_followers_socialblade(i.id)




#########
        # folder = os.path.dirname(os.path.dirname(__file__))
        # book = xlrd.open_workbook('%s/2__205.xlsx' % folder)
        # sh = book.sheet_by_index(0)
        # i = 0
        # for rx in range(sh.nrows):
        #     i += 1
        #     if i > 1:
        #         if check_value(sh.row(rx)[2].value):
        #             Coin.objects.create(
        #                 title=sh.row(rx)[0].value,
        #                 short_name=sh.row(rx)[2].value,
        #                 website_url=sh.row(rx)[4].value,
        #                 twitter_url=check_url(sh.row(rx)[5].value),
        #                 reddit_url=check_url(sh.row(rx)[6].value),
        #                 github_url=check_url(sh.row(rx)[7].value),
        #                 coinmarketcap_url=check_url(sh.row(rx)[3].value),
        #                 # official_forum=sh.row(rx)[8].value,
        #                 # telegram=sh.row(rx)[9].value,
        #                 picture=get_image(check_url(sh.row(rx)[1].value))
        #             )
