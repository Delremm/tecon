import datetime
import os

from rest_framework import viewsets, permissions
from rest_framework import views
from rest_framework.response import Response
from tecon_app.api.serializers import TrialSerializer
from tecon_app.models import Trial

from django.conf import settings
from django.utils.encoding import force_unicode
from django.core.files.storage import default_storage

from filer.utils.files import get_valid_filename



class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Instance must have an attribute named `owner`.
        return obj.user == request.user


class TestViewSet(viewsets.ModelViewSet):
    permission_classes = (IsOwnerOrReadOnly,)
    serializer_class = TrialSerializer
    queryset = Trial.objects.all()


class FileUploadView(views.APIView):

    def post(self, request, *args, **kwargs):
        path = self.handle_uploaded_file(request.FILES.values()[0])
        return Response(str(path.replace(
            settings.MEDIA_ROOT, settings.MEDIA_URL)), status=202)

    def get(self, request, *args, **kwargs):
        return Response(str(request.POST), status=203)

    def handle_uploaded_file(self, file_obj):
        path = '%s%s' % (settings.MEDIA_ROOT, self.by_date(file_obj.name))
        file_path = default_storage.save(path, file_obj)
        return file_path

    def by_date(self, filename):
        datepart = force_unicode(datetime.datetime.now().strftime("%Y/%m/%d/%H/%M"))
        return os.path.join(datepart, get_valid_filename(filename))
