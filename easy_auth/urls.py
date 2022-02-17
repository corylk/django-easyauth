from django.urls import path

from .views import EasyAuthLoginView


urlpatterns = [
    path('', EasyAuthLoginView.as_view(), name="login"),
]
