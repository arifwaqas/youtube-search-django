from django.urls import path
from . import views
from search import views
urlpatterns = [
    path('', views.index, name='index'),
    path('test', views.postdata, name='test-data')
]


