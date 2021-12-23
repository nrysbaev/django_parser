from django.urls import path
from . import views

urlpatterns = [
    path('anime/', views.FilmView.as_view()),
    path('parser/', views.ParserAnimeView.as_view()),

]
