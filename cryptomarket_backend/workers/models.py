from django.db import models

SCRAPPERS_TYPES = (
    ('twitter_comments_vader', 'Twitter comments for vader'),
    ('twitter_comments', 'Twitter comments'),
    ('twitter_likes', 'Twitter likes'),
    ('twitter_followers', 'Twitter followers'),
    ('twitter_text', 'Twitter text'),
    ('reddit_subscribers', 'Reddit subscribers'),
    ('github_parser', 'Github repository creations number'),
    ('marketcap_scraper', 'Marketcap Scrapper'),

)

PRIORITY_TYPES = (
    (1, 'High priority'),
    (2, 'Normal priority'),
    (3, 'Low priority'),
)

STATUS_TYPE = (
    ('start', 'start'),
    ('finish', 'finish'),
    ('error', 'error'),
)

RATING_TYPE = (
    ('overall', 'overall'),
    ('growth', 'growth'),
    ('trending', 'trending'),
)


class DateInfo(models.Model):
    """
    Model use for statistic
    """
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Coin(DateInfo):
    title = models.CharField(max_length=255, verbose_name='Coin')
    short_name = models.CharField(max_length=255, null=True, blank=True)
    website_url = models.URLField(null=True, blank=True, max_length=500, verbose_name='Website')
    twitter_url = models.URLField(null=True, blank=True, max_length=500, verbose_name='Twitter')
    reddit_url = models.URLField(null=True, blank=True, max_length=500, verbose_name='Reddit')
    github_url = models.URLField(null=True, blank=True, max_length=500, verbose_name='Github')
    coinmarketcap_url = models.URLField(null=True, blank=True, max_length=500, verbose_name='Coinmarketcap')
    official_forum = models.URLField(null=True, blank=True, max_length=500, verbose_name='Official Forum')
    telegram = models.URLField(null=True, blank=True, max_length=500)
    picture = models.ImageField(null=True, blank=True)
    price_usd = models.CharField(null=True, blank=True, max_length=50)
    usd_percent = models.CharField(null=True, blank=True, max_length=50)
    price_btc = models.CharField(null=True, blank=True, max_length=50)
    btc_percent = models.CharField(null=True, blank=True, max_length=50)
    parsing_day = models.IntegerField(null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["title"]


class StatisticScrapper(DateInfo):
    coin = models.ForeignKey(Coin)
    scrapper = models.CharField(max_length=120, verbose_name='Scrapper')
    task_id = models.CharField(max_length=255, verbose_name='Task ID')
    status = models.CharField(max_length=50, default='start', choices=STATUS_TYPE)

    def __str__(self):
        return self.task_id


class DefaultInfoCalculating(models.Model):
    """
    Template for calculations models
    """
    coin = models.ForeignKey(Coin)
    time_type = models.CharField(max_length=150)
    ranking_type = models.CharField(max_length=100, null=True)

    class Meta:
        abstract = True


class TempTrendingValue(DefaultInfoCalculating):
    value = models.FloatField(null=True, blank=True)

    def __str__(self):
        return '%s' % self.coin.title


class TempGrowthValues(DefaultInfoCalculating):
    value = models.FloatField(null=True, blank=True)

    def __str__(self):
        return '%s' % self.coin.title


class TempTotalValueByPeriod(DefaultInfoCalculating):
    """  Set total values for period """
    value = models.FloatField(null=True, blank=True)

    def __str__(self):
        return '%s' % self.coin.title
