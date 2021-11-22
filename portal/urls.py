from django.urls import path
from rest_framework.routers import DefaultRouter

from portal.views import user_view, news_view, user_config_view

router = DefaultRouter()
router.register('country', user_config_view.CountryViewSet)

urlpatterns = [
    # Auth API endpoint
    path('login/', user_view.UserLoginView.as_view(), name='login'),
    path('logout/', user_view.LogoutView.as_view(), name='logout'),
    path('profile/', user_view.ProfileView.as_view(), name='profile'),
    path('password-change/<int:pk>/', user_view.ChangePasswordView.as_view(), name='password_change'),
    path('registration/', user_view.RegisterView.as_view(), name='user_registration'),
    # News api endpoint start
    path('country-news/', news_view.FilterByCountryNewsAPIView.as_view(), name='country_news_view'),
    path('source-news/', news_view.FilterBySourceNewsView.as_view(), name='source_news_view'),
    path('user-config/', user_config_view.UserConfigAPIView.as_view(), name='user_config'),
] + router.urls
