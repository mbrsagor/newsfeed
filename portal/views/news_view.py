import requests
from rest_framework import views, status, permissions
from rest_framework.response import Response
from django.conf import settings

from utils.services import make_url


class AllNewsAPIView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        _items = []
        url = make_url(settings.ROOT_URL, settings.ALL_NEWS, settings.API_KEY)
        print(url)
        source = self.request.query_params.get('source', None)
        country = self.request.query_params.get('country', None)
        if source:
            url += '&sources=' + source
        elif country:
            url += '&country=' + country
        news = requests.get(url).json()
        print(self.request.query_params.get('source', None))
        return Response(news, status=status.HTTP_200_OK)
