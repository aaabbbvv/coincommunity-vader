from datetime import datetime
import requests
from simplejson import JSONDecodeError
import time
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

from grab import Grab
from core.celery import app
from workers.models import Coin
from parsers.models import TwitterComment
from bs4 import BeautifulSoup


def check_element(coin, tweet_id, comment_id, text):
    if tweet_id is None or comment_id is None or text is None:
        return False
    tweets = TwitterComment.objects.filter(coin=coin, tweet_id=tweet_id[1], comment_id=comment_id)
    if tweets.count() == 1:
        return False

    elif tweets.count() > 1:
        tweets.delete()

    return True


def get_part_url(coin):
    return coin.twitter_url.split('https://twitter.com/')[1]


# def grab_scrape(url):
#     g = Grab(timeout=90, connect_timeout=90)
#     g.go(url)
#     return g.doc.select('//li/@data-item-id').text()


def grab_scrape(url, coin):
    g = Grab(timeout=90, connect_timeout=90)
    g.go(url)
    data = g.doc.select('//li[@data-item-type="tweet"]').selector_list
    data_list = []
    for i in data:
        try:
            tweet_id = i.select('.//div/@data-item-id').text()
            slug = i.select('.//div/@data-permalink-path').text().split('/')[1]
            data_list.append([slug, tweet_id])
        except Exception:
            continue
    try:
        return data_list[-1][1], data_list
    except IndexError:
        return '', []


def get_comments_info(coin, tweet_id, analyzer):
    last_comment_id = ''
    last_comment_id_new = ''
    while True:
        r = requests.get('https://twitter.com/i/%s/conversation/%s?'
                         'include_available_features=1&include_entities=1&max_position=%s&'
                         'reset_error_state=false' % (tweet_id[0], tweet_id[1], last_comment_id))

        try:
            soup = BeautifulSoup(r.json()['items_html'], 'html5lib')
        except JSONDecodeError:
            break

        elements = soup.findAll('li', {'data-item-type': 'tweet'})
        for element in elements:
            try:
                last_comment_id_new = element.attrs.get('data-item-id')[-1]
            except Exception:
                last_comment_id_new = last_comment_id
            if len(last_comment_id_new) == 1:
                last_comment_id_new = element.attrs.get('data-item-id')
            comment_id = element.attrs.get('data-item-id')
            try:
                date = element.findChildren('small', {'class': 'time'})[0].find('a').attrs.get('title')
            except IndexError:
                continue
            date = datetime.strptime(date, '%I:%M %p - %d %b %Y')
            text = element.find('div', {'class': 'js-tweet-text-container'}).text.replace('\n', '')
            # text = str(text.encode('utf-8'))
            if check_element(coin, tweet_id, comment_id, text) is True:
                vs = analyzer.polarity_scores(text)
                TwitterComment.objects.create(date=date,
                                              tweet_id=tweet_id[1],
                                              coin=coin,
                                              url=coin.twitter_url,
                                              sentence=text,
                                              comment_id=comment_id,
                                              compound_value=vs.get('compound'),
                                              negative_value=vs.get('neg'),
                                              neutral_value=vs.get('neu'),
                                              positive_value=vs.get('pos')
                                              )

        if last_comment_id == last_comment_id_new:
            break
        else:
            last_comment_id = last_comment_id_new


def scrape(coin, url):
    if url.find('http') < 0:
        return None
    date_start = datetime.now()
    print('start scrapped_twitter_comment_vader(%s) %s' % (coin.title, date_start))

    last_tweets_id, tweets_id_list = grab_scrape(url, coin)
    while True:
        r = requests.get('https://twitter.com/i/profiles/show/%s/timeline/tweets?'
                         'include_available_features=1&include_entities=1&max_position=%s'
                         '&reset_error_state=false' % (get_part_url(coin), last_tweets_id))

        try:
            soup = BeautifulSoup(r.json()['items_html'], 'html5lib')
        except JSONDecodeError:
            break
        try:
            elements = soup.findAll('li', {'data-item-type': 'tweet'})
        except Exception:
            break
        for element in elements:
            try:
                path = element.find('div', {'class': 'tweet'}).attrs.get('data-permalink-path').split('/')
            except Exception:
                continue
            tweets_id_list.append([path[1], path[3]])
        try:
            tweets_id_list[-1][-1]
        except Exception:
            return None
        if last_tweets_id == tweets_id_list[-1][-1]:
            break
        else:
            last_tweets_id = tweets_id_list[-1][-1]

    analyzer = SentimentIntensityAnalyzer()
    for tweet_id in tweets_id_list:
        get_comments_info(coin, tweet_id, analyzer)
    date_end = datetime.now()
    print('start scrapped_twitter_comment_vader(%s) (%s)/(%s)' % (coin.title, date_start, date_end))


@app.task()
def scrapped_twitter_comment_vader(coin_id):
    coin = Coin.objects.get(id=coin_id)
    if coin.twitter_url is None:
        return None
    scrape(coin, coin.twitter_url)
