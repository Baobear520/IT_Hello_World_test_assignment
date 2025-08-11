from django.urls import path

from .views import HeroListCreateView

urlpatterns = [
    path('',HeroListCreateView.as_view(), name='hero'),
]