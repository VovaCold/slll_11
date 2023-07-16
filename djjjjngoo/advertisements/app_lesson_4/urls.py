from django.urls import path
from .views import index, top_sellers

urlpatterns = [
    path('lll', index, name='main-page'),
    path('top-sel', top_sellers, name='top-sellers'),
]