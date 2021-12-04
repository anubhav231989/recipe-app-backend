from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class CoreUserManager(BaseUserManager):
    '''
        CUSTOM USER MODEL MANAGER.
    '''

    def create_user_object(self, email, password=None, **extra_args):
        user = self.model(email=email, **extra_args)
        user.set_password(password)
        return user


    def create_user(self, email, password=None, **extra_args):
        if not email:
            raise ValueError("Email is a manadatory field.")

        email = self.normalize_email(email)
        user = self.create_user_object(email, password, **extra_args)
        user.save()

        return user

    def create_superuser(self, email, password):
        user = self.create_user_object(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):
    '''
        CUSTOM USER MODEL THAT SUPPORTS EMAIL AS THE UNIQUE IDENTIFIER INSTEAD OF USERNAME.
    '''

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CoreUserManager()

    USERNAME_FIELD = 'email'

