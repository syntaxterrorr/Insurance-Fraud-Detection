from django.urls import path,include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('claim', views.claim, name='claim'),
    path('buy', views.buy, name='buy'),
]
