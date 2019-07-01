from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """User to update their own Profile"""

    def has_object_permission(self, request, view, obj):
        """Check for user is trying to update own profile."""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id
