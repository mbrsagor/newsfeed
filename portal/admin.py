from django.contrib import admin
from portal.models import Country, Source, KeyWord, UserConfig, NewsFeed

admin.site.register(Country)
admin.site.register(Source)
admin.site.register(KeyWord)
admin.site.register(UserConfig)
admin.site.register(NewsFeed)
