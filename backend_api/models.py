from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


# Create your models here.
class UserProfileManager(BaseUserManager):
    """Manager for User profiles."""

    def create_user(self, email, name, password=None):
        """Creating new user profile"""

        if not email:
            raise ValueError("User must have an email address.")

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)

        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Create a new super user profile"""
        user = self.create_user(email, name, password)

        self.is_superuser = True
        self.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system."""
    # Defining attributes that our DB will have in the Model.
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # Creating Model Manager - For using Custom Model with Django CLI

    # A Class of Model Manager to manage our customized model in Django to Interact with users.
    objects = UserProfileManager()

    # overriding for customizing
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Retreive Full Name of user"""
        return self.name

    def get_short_name(self):
        """Retreive short name."""
        return self.name

    # Recommended for all the models. To convert user into meaningful string representation.
    def __str__(self):
        """Return String representation of the user."""
        return self.email
