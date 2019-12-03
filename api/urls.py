from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

# TODO: add getById api or overload to the url view
urlpatterns = [
    path('urls/', views.UrlsView.as_view()),
    path('urls/<str:url>', views.UrlView.as_view()),
]
