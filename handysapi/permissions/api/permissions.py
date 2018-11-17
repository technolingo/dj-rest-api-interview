from rest_framework.permissions import BasePermission


class DummyListPermission(BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated

class DummyViewPermission(DummyListPermission):

    def has_permission(self, request, view):
        # get_membership_int() will return 0, 1, or 2
        # indicating different levels of membership status
        sup = super(DummyViewPermission, self).has_permission(request, view)
        return sup and request.user.get_membership_int() > 0

class DummyEditPermission(BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated

class DummyDeletePermission(DummyEditPermission):

    def has_permission(self, request, view):
        sup = super(DummyDeletePermission, self).has_permission(request, view)
        return sup and request.user.get_membership_int() > 1
