from django.contrib import admin
from django_admin_listfilter_dropdown.filters import RelatedDropdownFilter

from parsers.models import TweetLikes, TweetCountComments, TweetText, \
    TwitterFollowers, RedditFollowers, TwitterComment, MarketcapData, \
    GitHub, GitHubForks, GitHubCommit, GitHubStars, GitHubWatchers
from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter



class TweetLikesAdmin(admin.ModelAdmin):
    list_display = ['date', 'coin', 'likes', 'date_update', 'url']
    search_fields = ['coin__title', 'likes', 'url', 'tweet_id']
    ordering = ['-date']
    readonly_fields = ('date', 'likes', 'date_update', 'url')
    list_filter = (('coin', RelatedDropdownFilter), 'date_update',  ('date', DateRangeFilter))


class TweetCountCommentsAdmin(admin.ModelAdmin):
    list_display = ['date', 'coin', 'count_comments', 'date_update', 'url']
    search_fields = ['coin__title', 'count_comments', 'url', 'tweet_id']
    ordering = ['-date']
    readonly_fields = ('date', 'count_comments', 'date_update', 'url')
    list_filter = (('coin', RelatedDropdownFilter),  'date_update',  ('date', DateRangeFilter))


class TweetTextAdmin(admin.ModelAdmin):
    list_display = ['date', 'coin', 'date_update', 'url']
    search_fields = ['coin__title', 'text', 'url', 'tweet_id']
    ordering = ['-date']
    readonly_fields = ('date', 'text', 'date_update', 'url')
    list_filter = (('coin', RelatedDropdownFilter), 'date_update', ('date', DateRangeFilter))


class TwitterFollowersAdmin(admin.ModelAdmin):
    list_display = ['date', 'coin', 'count_followers', 'url']
    search_fields = ['coin__title', 'url']
    ordering = ['-date']
    readonly_fields = ('date', 'coin', 'count_followers', 'url')
    list_filter = (('coin', RelatedDropdownFilter), ('date', DateRangeFilter))


class RedditFollowersAdmin(admin.ModelAdmin):
    list_display = ['date', 'coin', 'count_today', 'count_all', 'url']
    search_fields = ['coin__title', 'url']
    ordering = ['-date']
    readonly_fields = ('date', 'coin', 'count_today', 'count_all', 'url')
    list_filter = (('coin', RelatedDropdownFilter), ('date', DateRangeFilter))


class TweetVaderAdmin(admin.ModelAdmin):
    list_display = ['sentence', 'date', 'negative_value', 'compound_value', 'neutral_value', 'coin', 'url']
    search_fields = ['coin__title', 'sentence', 'tweet_id', 'comment_id']
    ordering = ['-date']
    list_filter = (('coin', RelatedDropdownFilter), ('date', DateRangeFilter))
    #readonly_fields = ('sentence', 'date', 'negative_value', 'compound_value', 'neutral_value')


class MarketcapDataAdmin(admin.ModelAdmin):
    list_display = ['date', 'coin', 'open', 'high', 'low', 'close', 'volume', 'market_cap']
    search_fields = ['coin__title']
    ordering = ['-date']
    list_filter = (('coin', RelatedDropdownFilter), 'date', ('date', DateRangeFilter))
    readonly_fields = ('coin', 'date', 'open', 'high', 'low', 'close', 'volume', 'market_cap')
 # # for ordinary fields
 #        ('a_charfield', DropdownFilter),
 #        # for related fields
 #        ('a_foreignkey_field', RelatedDropdownFilter),

class GitHubAdmin(admin.ModelAdmin):
    list_display = ['date', 'coin', 'repos_id', 'url']
    search_fields = ['coin__title', 'url']
    ordering = ['-date']
    list_filter = (('coin', RelatedDropdownFilter),
                   'date', ('date', DateRangeFilter))
    readonly_fields = ('date', 'coin', 'repos_id')


class GitHubDetailAdmin(admin.ModelAdmin):
    list_display = ['date', 'coin', 'repos_url']
    search_fields = ['coin__title', 'github__url']
    ordering = ['-date']
    list_filter = (('coin', RelatedDropdownFilter),
                   'date', ('date', DateRangeFilter))
    readonly_fields = ('date', 'coin')

    def repos_url(self, instance):
        return instance.github.url

    repos_url.short_description = "Repos URL"
    repos_url.admin_order_field = 'repos_url'


class GitHubWatchersAdmin(admin.ModelAdmin):
    list_display = ['date', 'coin', 'repos_url']
    search_fields = ['coin__title', 'github__url']
    ordering = ['-date']
    list_filter = (('coin', RelatedDropdownFilter),
                   'date', ('date', DateRangeFilter))
    readonly_fields = ('date', 'coin')

    def repos_url(self, instance):
        return instance.github.url

    repos_url.short_description = "Repos URL"
    # host_location.admin_order_field = 'host__location'


class GitHubCommitAdmin(admin.ModelAdmin):
    list_display = ['date', 'coin', 'sha', 'repos_url']
    search_fields = ['coin__title', 'github__url', 'sha']
    ordering = ['-date']
    list_filter = (('coin', RelatedDropdownFilter),
                   'date', ('date', DateRangeFilter))
    readonly_fields = ('date', 'coin')

    def repos_url(self, instance):
        return instance.github.url

    repos_url.short_description = "Repos URL"
    repos_url.admin_order_field = 'repos_url'



admin.site.register(TweetLikes, TweetLikesAdmin)
admin.site.register(TweetCountComments, TweetCountCommentsAdmin)
admin.site.register(TweetText, TweetTextAdmin)
admin.site.register(TwitterFollowers, TwitterFollowersAdmin)
admin.site.register(RedditFollowers, RedditFollowersAdmin)
admin.site.register(TwitterComment, TweetVaderAdmin)
admin.site.register(MarketcapData, MarketcapDataAdmin)
admin.site.register(GitHub, GitHubAdmin)
admin.site.register(GitHubForks, GitHubDetailAdmin)
admin.site.register(GitHubCommit, GitHubCommitAdmin)
admin.site.register(GitHubStars, GitHubDetailAdmin)
admin.site.register(GitHubWatchers, GitHubWatchersAdmin)
