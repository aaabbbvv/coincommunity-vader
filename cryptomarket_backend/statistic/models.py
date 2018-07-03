from django.db import models

# Create your models here.
from workers.models import Coin

RANK_TYPE = (
    ('watch_list', 'Watch List Ranking'),
    ('community_size', 'Community Size Ranking'),
    ('github_total', 'Github Total'),
    ('marketcap_size_usd_divergence', 'MarketCap Size USD Divergence Ranking'),
    ('vader_twitter_sentiment', 'VADER Twitter Sentiment'),
    ('twitter_followers', 'Twitter Followers Ranking'),
    ('twitter_likes', 'Twitter Likes Ranking'),
    ('reddit_subscribers', 'Reddit Subscribers Ranking'),
    ('github_repository_creations', 'GitHub Repository Creations'),
    ('github_stars', 'Github Repository Stars'),
    ('github_forks', 'Github Repository Forks'),
    ('github_commits', 'Github Repository Commits'),
    ('marketcap_size_usd', 'MarketCap Size USD Ranking'),
)

SORT = (
    ('total', 'Total'),
    ('growth', 'Growth'),
    ('trending', 'Trending'),
)


class RankingStatistic(models.Model):
    coin = models.ForeignKey(Coin, null=True)
    type = models.CharField(choices=RANK_TYPE, max_length=100)
    total = models.CharField(blank=True, null=True, max_length=100)
    total_week = models.IntegerField(blank=True, null=True)
    total_month = models.IntegerField(blank=True, null=True)
    total_three_month = models.IntegerField(blank=True, null=True)
    total_six_month = models.IntegerField(blank=True, null=True)
    total_year = models.IntegerField(blank=True, null=True)
    trending_week = models.IntegerField(blank=True, null=True)
    trending_month = models.IntegerField(blank=True, null=True)
    trending_three_month = models.IntegerField(blank=True, null=True)
    trending_six_month = models.IntegerField(blank=True, null=True)
    trending_year = models.IntegerField(blank=True, null=True)
    growth_week = models.IntegerField(blank=True, null=True)
    growth_month = models.IntegerField(blank=True, null=True)
    growth_three_month = models.IntegerField(blank=True, null=True)
    growth_six_month = models.IntegerField(blank=True, null=True)
    growth_year = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return "%s %s" % (self.coin.title, self.type)
