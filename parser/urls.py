from django.urls import path
from . import views

urlpatterns = [
    path('anime/', views.FilmView.as_view()),
    path('parser/', views.ParserView.as_view()),
    path('smartphones/', views.SmartphoneListView.as_view()),
    path('smartphones/<int:id>/', views.SmartphoneDetailView.as_view()),

]
