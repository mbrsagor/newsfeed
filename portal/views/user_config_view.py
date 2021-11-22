from rest_framework import views, viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from portal.serializer.user_config_serializer import CountrySerializer, UserConfigSerializer
from portal.models import Country, UserConfig
from utils.custom_responses import prepare_success_response, prepare_error_response
from utils.services import validate_country


class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = [IsAuthenticated, ]


class UserConfigAPIView(views.APIView):
    permission_classes = [IsAuthenticated, ]

    def post(self, request):
        validate_error = validate_country(request.data)
        if validate_error is not None:
            return Response(prepare_error_response(validate_error), status=status.HTTP_400_BAD_REQUEST)
        serializer = UserConfigSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(prepare_success_response(serializer.data), status=status.HTTP_200_OK)
        return Response(prepare_error_response(serializer.errors), status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        user_config = request.user.user_config
        serializer = UserConfigSerializer(user_config)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CountryOfNewsFilterView(views.APIView):
    def get(self, request):
        pass
