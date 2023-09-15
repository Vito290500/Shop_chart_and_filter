from django.urls import path

from . import views

urlpatterns = [
    path("", views.HomePage.as_view(), name="home-page"),
    path("SearchResult", views.HomePageSearch.as_view(), name="search-homepage"),
    path("ListPrefer", views.Prefer.as_view(), name="list-prefer")
]