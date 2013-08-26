# coding: utf-8

from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from tecon_app import views

urlpatterns = patterns(
    '',
    url(r'^$', views.TeconView.as_view(), name="main"),
    url(r'^create/$', views.CreateTestView.as_view(), name="create_test"),
    url(r'^my_tests/$', views.UserTestsView.as_view(), name="user_tests"),
    url(
        r'^successfully_created/$',
        TemplateView.as_view(template_name='tecon/successfully_created.html'),
        name='success_test_creation'),
)
