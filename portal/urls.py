from django.urls import path
from portal.views import user_view, news_view


urlpatterns = [
    # Auth API endpoint
    path('login/', user_view.UserLoginView.as_view(), name='login'),
    path('logout/', user_view.LogoutView.as_view(), name='logout'),
    path('profile/', user_view.ProfileView.as_view(), name='profile'),
    path('password-change/<int:pk>/', user_view.ChangePasswordView.as_view(), name='password_change'),
    path('registration/', user_view.RegisterView.as_view(), name='user_registration'),
    # News api endpoint start
    path('news/', news_view.AllNewsAPIView.as_view(), name='news_view'),
]
