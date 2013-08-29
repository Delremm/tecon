from django.conf.urls import patterns, url, include
from rest_framework import routers

from tecon_app.api import views

router = routers.DefaultRouter()
router.register(r'tests', views.TestViewSet, base_name='test')

urlpatterns = patterns('',
    url(
        r'^upload_image/$',
        views.FileUploadView.as_view(), name="upload_image"),
    url(r'^', include(router.urls)),
)
