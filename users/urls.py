from django.urls import path
from .views import CustomUserRegister, BlacklistTokenUpdateView

app_name = 'users'

urlpatterns = [
    path('register/', CustomUserRegister.as_view(), name="create_user"),
    path('logout/blacklist/', BlacklistTokenUpdateView.as_view(), name='blacklist')
]