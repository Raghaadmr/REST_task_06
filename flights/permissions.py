from rest_framework.permissions import BasePermission
import datetime

class IsPassenger(BasePermission):
	message = "you are not a passenger."
	def has_object_permission(self, request, view, obj):
		if request.user.is_staff or (obj.user == request.user):
			return True
		else:
			return False

class IsDateValid(BasePermission):
	message = "you cannot change unless 3 days has passed."
	def has_object_permission(self, request, view, obj):
		if (obj.date - datetime.date.today()).days > 3:
			return True
		else:
			return False
