from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """User to update their own Profile"""

    def has_object_permission(self, request, view, obj):
        """Check for user is trying to update own profile."""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id


class UpdateOwnStatus(permissions.BasePermission):
    """Updating own status by users"""

    def has_object_permission(self, request, view, obj):
        """Check if user is updating own status"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile.id == request.user.id
