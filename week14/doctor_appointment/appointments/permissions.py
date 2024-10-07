from rest_framework import permissions

class AppointmentsPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        elif request.method == "POST":
            return request.user.has_perm("appointments.add_appointment")
        elif request.method in ["PUT", "PATCH"]:
            return request.user.has_perm("appointments.change_appointment")
        elif request.method == "DELETE":
            return request.user.has_perm("appointments.delete_appointment")
        return False

    def has_object_permission(self, request, view, obj):
        if request.method in ["PUT", "PATCH"]:
            return request.user == obj.created_by
        elif request.method == "DELETE":
            return request.user == obj.created_by
        return False