import requests
from rest_framework import views, status, permissions
from rest_framework.response import Response

from newsfeed.settings import API_KEY, ALL_NEWS
from utils.custom_responses import prepare_error_response


class AllNewsAPIView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        url = f'{ALL_NEWS}{API_KEY}'
        news = requests.get(url).json()
        if not news:
            return Response(prepare_error_response('Your API key is invalid or incorrect.'))
        return Response(news, status=status.HTTP_200_OK)
