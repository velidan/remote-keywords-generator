from django.urls import path
from . import views

# TODO: add getById api or overload to the url view
urlpatterns = [
    path('urls/', views.UrlsView.as_view()),
    path('urls/<str:url>', views.UrlView.as_view()),
]
