from rest_framework.permissions import BasePermission


class IsCashier(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Касир').exists()


class IsConsultant(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Продавець-консультант').exists()


class IsAccountant(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Бухгалтер').exists()
