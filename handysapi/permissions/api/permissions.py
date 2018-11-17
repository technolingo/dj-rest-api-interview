from rest_framework.permissions import BasePermission

'''
    1. DummyDeletePermission은 부모 관한이고 DummyEditPermission은 DummyDeletePermission의 자식입니다.
    2. DummyViewPermission은 DummyEditPermission의 자식이지만 DummyDeletePermission의 관한을 가지지 않습니다. (1 level만)
'''


class DummyDeletePermission(BasePermission):

    def has_current_level_permission(self, request, view):
        return request.user.has_perm('users.can_delete_dummy')

    def has_permission(self, request, view):
        return self.has_current_level_permission(request, view)

class DummyEditPermission(DummyDeletePermission):

    def has_current_level_permission(self, request, view):
        return request.user.has_perm('users.can_edit_dummy')

    def has_permission(self, request, view):
        sup = super(DummyEditPermission, self).has_current_level_permission(request, view)
        return sup or self.has_current_level_permission(request, view)

class DummyViewPermission(DummyEditPermission):

    def has_current_level_permission(self, request, view):
        return request.user.has_perm('users.can_view_dummy')

    def has_permission(self, request, view):
        sup = super(DummyViewPermission, self).has_current_level_permission(request, view)
        return sup or self.has_current_level_permission(request, view)

class DummyListPermission(DummyViewPermission):

    def has_current_level_permission(self, request, view):
        return request.user.has_perm('users.can_list_dummy')

    def has_permission(self, request, view):
        sup = super(DummyListPermission, self).has_current_level_permission(request, view)
        return sup or self.has_current_level_permission(request, view)
