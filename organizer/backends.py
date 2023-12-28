# from django.contrib.auth.backends import ModelBackend
# from django.contrib.auth.hashers import check_password
# from .models import Organizer

# class OrganizerBackend(ModelBackend):
#     def authenticate(self, request, username=None, password=None, **kwargs):
#         try:
#             user = Organizer.objects.get(username=username)
#         except Organizer.DoesNotExist:
#             return None

#         if check_password(password, user.password) and self.user_can_authenticate(user):
#             return user

#     def get_user(self, user_id):
#         try:
#             return Organizer.objects.get(pk=user_id)
#         except Organizer.DoesNotExist:
#             return None
