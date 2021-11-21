import requests
from rest_framework import views, status, permissions
from rest_framework.response import Response
from django.conf import settings

from utils.services import api_endpoint


class FilterByCountryNewsAPIView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        url = api_endpoint(settings.ROOT_URL, settings.FILTER_BY_COUNTRY, settings.API_KEY)
        country = self.request.query_params.get('country', None)
        if country:
            url += '&country=' + country
        news = requests.get(url).json()
        return Response(news, status=status.HTTP_200_OK)


class FilterBySourceNewsView(views.APIView):

    def get(self, request):
        url = api_endpoint(settings.ROOT_URL, settings.NEWS_BY_SOURCE, settings.API_KEY)
        source = self.request.query_params.get('source', None)
        if source:
            url += '&sources=' + source
        news = requests.get(url).json()
        return Response(news, status=status.HTTP_200_OK)
