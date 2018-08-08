from django.urls import path
from django.views.generic import TemplateView
from . views import newsList, detailList
 
urlpatterns = [
    path('api/', newsList.as_view()),
    path('api/<int:pk>', detailList.as_view()),
]