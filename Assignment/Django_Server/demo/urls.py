from django.conf.urls import url
from demo import  views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^links/$', views.LinksPageView.as_view()),
    url(r'^getDelhiPopu/$',views.Customers.getDelhiPopu),
]