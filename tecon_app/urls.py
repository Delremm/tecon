# coding: utf-8

from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView, DeleteView
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
    url(
        r'^tests/(?P<test_id>\d+)/$',
        views.TestDetailView.as_view(), name="test_details"),
    # url(
    #     r'^category/(?P<category_id>\d+)/$',
    #     views.TestCategoryView.as_view(), name="test_category"),
    url(
        r'^tests/$',
        views.TestListView.as_view(), name="tests"),
    url(
        r'^tests/edit/(?P<test_id>\d+)/$',
        views.EditTestView.as_view(), name="edit_test"),
    url(
        r'^tests/delete/(?P<test_id>\d+)/$',
        views.DeleteTestView.as_view(), name="delete_test"),
)
