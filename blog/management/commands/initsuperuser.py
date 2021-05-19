"""Create a super user."""
import os
from django.conf import settings
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):

    def handle(self, *args, **options):
        email = os.environ.get('SUPER_USER_EMAIL', settings.SUPER_USER_EMAIL)
        username = os.environ.get('SUPER_USER_NAME', settings.SUPER_USER_NAME)
        password = os.environ.get('SUPER_USER_PASS', settings.SUPER_USER_PASS)
        user_model = get_user_model()
        super_user = user_model.objects.filter(username=username, is_superuser=True)
        if not super_user.count():
            user_model.objects.create_superuser(username, email, password)
            print('Created super user')
        else:
            super_user = super_user[0]
            setattr(super_user, super_user.EMAIL_FIELD, email)
            super_user.set_password(password)
            super_user.save()
            print('Updated super user')
