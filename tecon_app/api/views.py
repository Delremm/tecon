from rest_framework import viewsets, permissions
from rest_framework import views
from rest_framework.response import Response
from tecon_app.api.serializers import TrialSerializer
from tecon_app.models import Trial


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
        file_obj = request.FILES.values()[0]

        print file_obj
        # ...
        # do some staff with uploaded file
        # ...
        return Response(str(request.POST), status=202)

    def get(self, request, *args, **kwargs):
        print 'hett'
        return Response(str(request.POST), status=203)
