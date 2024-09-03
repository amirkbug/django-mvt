from django.urls import path
from .views import *


app_name="accounts"

urlpatterns = [
    path('login', login_view, name="login"),
    path('logout', logout_view, name="logout"),
    path('signup', signup, name="signup"),
    path('password_change', password_change, name="password_change"),
    path('password_reset', password_reset, name="password_reset"),
    path('password_reset_done', password_reset_done, name="password_reset_done"),
    path('password_reset_confirm/<str:token>', password_reset_confirm, name="password_reset_confirm"),
    path('password_reset_complete', password_reset_complete, name="password_reset_complete"),
]
