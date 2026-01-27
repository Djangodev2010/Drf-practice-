from rest_framework import permissions

class IsUserOrReadOnly(permissions.BasePermission):
    """Create custom permissions for users"""

    def has_object_permission(self, request, obj, view):
        #Read permissions are allowed for every request
        #so we'll allow only GET, HEAD, etc. requests

        if request.method in permissions.SAFE_METHODS:
            return True
        
        #Only allow write requests for authenticated users and that too of related cars
        return obj.user == request.user
