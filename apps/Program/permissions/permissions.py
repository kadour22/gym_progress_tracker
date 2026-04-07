from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsProgramOwner(BasePermission) :
    """
      custom permission that allow only object owners to access it
    """
    message = "next u try to access other users data ur account with closed" 
    def has_object_permission(self, request, view, obj) :
        return request.user == obj.user and request.user.is_authenticated
    