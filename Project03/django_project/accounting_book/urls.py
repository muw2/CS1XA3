from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^user$', views.UserView.as_view()),
    url(r'^bill$', views.BillView.as_view()),
]