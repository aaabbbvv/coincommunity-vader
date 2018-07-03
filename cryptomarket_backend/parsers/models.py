from django.db import models
from datetime import datetime
from workers.models import Coin


class TweetLikes(models.Model):
    likes = models.IntegerField(verbose_name='Likes', null=True, blank=True, default=None)
    date = models.DateTimeField(verbose_name='Date')
    coin = models.ForeignKey(Coin, related_name='tweets_likes')
    date_update = models.DateTimeField(verbose_name='Date update', null=True)
    tweet_id = models.CharField(max_length=256, null=True, verbose_name='ID tweet')
    url = models.URLField(verbose_name='Url', null=True, blank=True)

    class Meta:
        verbose_name = 'Tweets likes'
        verbose_name_plural = 'Tweets likes'


class TweetCountComments(models.Model):
    count_comments = models.IntegerField(verbose_name='Count comments', null=True, blank=True, default=None)
    date = models.DateTimeField(verbose_name='Date')
    coin = models.ForeignKey(Coin, related_name='tweets_comments')
    date_update = models.DateTimeField(verbose_name='Date update', null=True, blank=True)
    tweet_id = models.CharField(max_length=256, null=True, verbose_name='ID tweet')
    url = models.URLField(verbose_name='Url', null=True, blank=True)

    class Meta:
        verbose_name = 'Count comments'
        verbose_name_plural = 'Count comments'


class TweetText(models.Model):
    text = models.TextField(verbose_name='Text')
    date = models.DateTimeField(verbose_name='Date')
    coin = models.ForeignKey(Coin, related_name='tweets_text')
    date_update = models.DateTimeField(verbose_name='Date update', null=True, blank=True)
    tweet_id = models.CharField(max_length=256, null=True, verbose_name='ID tweet')
    url = models.URLField(verbose_name='Url', null=True, blank=True)

    class Meta:
        verbose_name = 'Tweet text'
        verbose_name_plural = 'Tweets text'


class TwitterFollowers(models.Model):
    count_followers = models.IntegerField(verbose_name='Count followers', null=True, blank=True)
    date = models.DateTimeField(verbose_name='Date')
    coin = models.ForeignKey(Coin, related_name='twitter_followers')
    url = models.URLField(verbose_name='Url', null=True, blank=True)

    class Meta:
        verbose_name = 'Twitter followers'
        verbose_name_plural = 'Twitter followers'


class RedditFollowers(models.Model):
    date = models.DateTimeField(verbose_name='Date')
    count_all = models.IntegerField(null=True, verbose_name='Count of subscribers for all time')
    count_today = models.IntegerField(null=True, verbose_name='Count of subscribers for today')
    coin = models.ForeignKey(Coin, related_name='reddit_followers', null=True)
    url = models.URLField(verbose_name='Url', null=True, blank=True)

    class Meta:
        verbose_name = 'Reddit followers'
        verbose_name_plural = 'Reddit followers'


class TwitterComment(models.Model):
    date = models.DateTimeField(verbose_name='Date', null=True, blank=True)
    sentence = models.TextField(verbose_name='sentence', null=True, blank=True)
    negative_value = models.FloatField(verbose_name='Negative_value', null=True, blank=True)
    compound_value = models.FloatField(verbose_name='Compound value', null=True, blank=True)
    neutral_value = models.FloatField(verbose_name='Neutral value', null=True, blank=True)
    positive_value = models.FloatField(verbose_name='Positive value', null=True, blank=True)
    coin = models.ForeignKey(Coin, related_name='twitter_comment_vader', null=True)
    url = models.URLField(verbose_name='Url', null=True, blank=True)
    tweet_id = models.CharField(max_length=256, null=True, verbose_name='ID tweet')
    comment_id = models.CharField(max_length=256, null=True, verbose_name='ID comment')

    class Meta:
        verbose_name = 'Twitter comment vader'
        verbose_name_plural = 'Twitter comments vader'

    def __str__(self):
        return '%s' % self.sentence


class MarketcapData(models.Model):
    coin = models.ForeignKey(Coin, related_name='marketcap', null=True)
    date = models.DateTimeField(verbose_name='Date', null=True, blank=True)
    open = models.DecimalField(max_digits=15, decimal_places=10, null=True)
    high = models.DecimalField(max_digits=15, decimal_places=10, null=True)
    low = models.DecimalField(max_digits=15, decimal_places=10, null=True)
    close = models.DecimalField(max_digits=15, decimal_places=10, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    market_cap = models.BigIntegerField(null=True)

    class Meta:
        verbose_name = 'Marketcap Data'
        verbose_name_plural = 'Marketcap Data'

    def __str__(self):
        return self.coin.title


class GitHub(models.Model):
    date = models.DateTimeField(verbose_name='date', null=True, blank=True)
    coin = models.ForeignKey(Coin, related_name='github')
    # count_rep = models.IntegerField(verbose_name='Count of repositories', null=True)
    repos_id = models.IntegerField(verbose_name='ID of repositories', null=True)
    url = models.URLField(verbose_name='Url', null=True, blank=True)
    date_update = models.DateTimeField(null=True, blank=True, verbose_name='date update')

    class Meta:
        verbose_name = 'GitHub Data'
        verbose_name_plural = 'GitHub Data'

    def __str__(self):
        return self.url


class GitHubAdditional(models.Model):
    coin = models.ForeignKey(Coin)
    date = models.DateTimeField(null=True)
    # url = models.URLField(null=True)
    github = models.ForeignKey(GitHub, null=True, blank=True)
    # date_update = models.DateTimeField(default=datetime.now(), verbose_name='date update')

    class Meta:
        abstract = True

    def __str__(self):
        return self.coin.title


class GitHubStars(GitHubAdditional):
    id_user = models.IntegerField(verbose_name='ID user', null=True, blank=True, default=None)
    page_number = models.IntegerField(verbose_name='Page number', null=True, blank=True, default=None)

    class Meta:
        verbose_name = 'GitHubStars Data'
        verbose_name_plural = 'GitHubStars Data'


class GitHubCommit(GitHubAdditional):
    sha = models.CharField(max_length=200, null=True)

    class Meta:
        verbose_name = 'GitHubCommit Data'
        verbose_name_plural = 'GitHubCommit Data'


class GitHubForks(GitHubAdditional):
    id_fork = models.IntegerField()

    class Meta:
        verbose_name = 'GitHubForks Data'
        verbose_name_plural = 'GitHubForks Data'


class GitHubWatchers(GitHubAdditional):
    id_watchers = models.IntegerField(verbose_name='ID watchers', null=True, blank=True, default=None)
    page_number = models.IntegerField(verbose_name='Page number', null=True, blank=True, default=None)

    class Meta:
        verbose_name = 'GitHubWatchers Data'
        verbose_name_plural = 'GitHubWatchers Data'
