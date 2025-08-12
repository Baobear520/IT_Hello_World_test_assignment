from django.urls import path

from .views import HeroListCreateView

urlpatterns = [
    path('hero',HeroListCreateView.as_view(), name='hero'),
]