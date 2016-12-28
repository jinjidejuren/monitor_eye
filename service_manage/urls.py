from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^service_manage.html', views.service_index),
]
