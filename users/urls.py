from django.urls import path
from .views import register_view, authorization_view,confirm_user_view

urlpatterns = [
    path('api/v1/users/registration/', register_view),
    path('api/v1/users/authorization/', authorization_view),
    path('api/v1/users/confirm/', confirm_user_view)
]