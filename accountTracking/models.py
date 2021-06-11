from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

"""
This class is used to
"""
class accountManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError('This must be an email address')
        if not username:
            raise ValueError('This must be a username/domain')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
        )
        user.is_admin = True
        user.is_staff =True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser):
    email           =   models.EmailField(verbose_name="email", max_length=60, unique=True)
    username        =   models.CharField(max_length=30, unique=True)

    created_on      =   models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login      =   models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin        =   models.BooleanField(default=False)
    is_active       =   models.BooleanField(default=True)
    is_staff        =   models.BooleanField(default=False)
    is_superuser    =   models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    tracking = accountManager()

    def __str__(self):
        return self.email

    # Checking permissions as below to simplify all admins have all permissions
    def has_permission(self, perm, obj=None):
        return self.is_admin
    # Simplify the permission whether user has permission to view app or not (Always Yes)
    def has_module_permission(self, app_label):
        return True

