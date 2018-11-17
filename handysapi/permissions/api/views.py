from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.exceptions import PermissionDenied
from . import permissions


class DummyListAPIView(GenericAPIView):
    permission_classes = (permissions.DummyListPermission,)

    def permission_denied(self, request, message=None):
        """
        Override the default status code in case of unauthenticated users
        from '401 Unauthorised' to '403 Forbidden'
        """
        raise PermissionDenied(detail=message)

    def get(self, request, *args, **kwargs):
        return Response({'success': True, 'message': '성공'})


class DummyViewAPIView(GenericAPIView):
    permission_classes = (permissions.DummyViewPermission,)

    def get(self, request, *args, **kwargs):
        return Response({'success': True, 'message': '성공'})


class DummyEditAPIView(GenericAPIView):
    permission_classes = (permissions.DummyEditPermission,)

    def permission_denied(self, request, message=None):
        """
        Override the default status code in case of unauthenticated users
        from '401 Unauthorised' to '403 Forbidden'
        """
        raise PermissionDenied(detail=message)

    def get(self, request, *args, **kwargs):
        return Response({'success': True, 'message': '성공'})


class DummyDeleteAPIView(GenericAPIView):
    permission_classes = (permissions.DummyDeletePermission,)

    def get(self, request, *args, **kwargs):
        return Response({'success': True, 'message': '성공'})
