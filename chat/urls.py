from django.conf.urls import include, url
from . import views


urlpatterns = [
    url(r'^profile', views.profiles),
    url(r'^jobs', views.jobs),
    url(r'^questions', views.questions),

]
