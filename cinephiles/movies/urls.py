from django.urls import path

urlpatterns = [
    path('', views.home, name="home"),
    path('movies/id', views.movie, name="movie"),
]