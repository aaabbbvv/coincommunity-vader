import datetime
from celery.signals import task_success, task_failure
from celery.utils.log import get_task_logger

from core.celery import app
from workers.models import Coin, StatisticScrapper
from parsers.scrapers.twitter_comments_vader import scrapped_twitter_comment_vader

logger = get_task_logger(__name__)


@task_success.connect
def task_success_handler(sender=None, result=None, **kwargs):
    try:
        stats_worker = StatisticScrapper.objects.get(task_id=sender.request.id)
        stats_worker.status = 'finish'
        stats_worker.save()
    except StatisticScrapper.DoesNotExist:
        # TODO send error to sentry
        pass


@task_failure.connect
def task_error_handler(sender=None, result=None, **kwargs):
    try:
        stats_worker = StatisticScrapper.objects.get(task_id=sender.request.id)
        stats_worker.status = 'error'
        stats_worker.save()
    except StatisticScrapper.DoesNotExist:
        # TODO send error to sentry
        pass


@app.task()
def vader_scrapper():
    """ Vader scrapper """
    coins = Coin.objects.all()
    for coin in coins:
        task = scrapped_twitter_comment_vader.apply_async(args=[coin.pk], queue='vader')
        StatisticScrapper.objects.create(scrapper='twitter_vader', coin=coin, task_id=task.id)


