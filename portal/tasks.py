from celery import shared_task
from .models import NewsFeed


@shared_task(time_limit=900)
def create_news_feed(author, title, description, url, urlToImage, content):
    """
    Here 900 means convert seconds to 15 minutes result will show 900 seconds.
    Every 15 minutes will generate new task.
    :param author:
    :param title:
    :param description:
    :param url:
    :param urlToImage:
    :param content:
    :return:
    """
    news_feed = NewsFeed.objects.create(
        author=author,
        title=title,
        description=description,
        url=url,
        urlToImage=urlToImage,
        content=content
    )
    news_feed.save()
