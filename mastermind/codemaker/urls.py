from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.GameList.as_view()),
    path('<int:pk>/', views.GameDetail.as_view()),
    url(r'^newgame$', views.GameCreate.as_view(), name='create'),
]