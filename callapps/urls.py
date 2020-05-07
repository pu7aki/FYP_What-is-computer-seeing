from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('start/', views.start, name='start'),
    path('start1/', views.start1, name='start1'),
    path('newbie/', views.newbie, name='newbie'),
path('newbie2/', views.newbie2, name='newbie2'),
path('newbie3/', views.newbie3, name='newbie3'),
    path('answer/', views.answer, name='answer'),
    path('answer1/', views.answer1, name='answer1'),
    path('upload/', views.upload, name='upload'),
    path('message/', views.message, name='message'),
    path('score/', views.score, name='score'),
    path('Timeout/', views.Timeout, name='Timeout'),
    path('start2/', views.start2, name='start2'),
    path('start21/', views.start21, name='start21'),
    path('start3/', views.start3, name='start3'),
    path('start31/', views.start31, name='start31'),
    path('start4/', views.start4, name='start4'),
    path('start41/', views.start41, name='start41'),
    path('score1/', views.score1, name='score1'),
    path('random/', views.random, name='random'),
    path('randomeasyans/', views.randomeasyans, name='randomeasyans'),
path('middleans/', views.middleans, name='middleans'),
path('hardans/', views.hardans, name='hardans'),
]