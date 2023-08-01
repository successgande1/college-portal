from django.contrib.auth import get_user_model
from django.db import models
from PIL import Image
from phonenumber_field.modelfields import PhoneNumberField
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, Adjust, Transpose
from imagekit.models import ProcessedImageField
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
from datetime import datetime
from django.contrib.auth.models import AbstractUser, Group
from django.utils import timezone
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
User = get_user_model()

class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, username, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=255, unique=True)
    is_admin = models.BooleanField(default=False)
    is_rector = models.BooleanField(default=False)
    is_registrar = models.BooleanField(default=False)
    is_help_desk = models.BooleanField(default=False)
    is_applicant = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_graduate = models.BooleanField(default=False)
    last_updated = models.DateTimeField(auto_now_add=True)

    # Provide unique related names for groups and user_permissions fields
    groups = None
    user_permissions = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    



#Image file upload validator
@deconstructible
class FileExtensionValidator:
    def __init__(self, extensions):
        self.extensions = extensions

    def __call__(self, value):
        extension = value.name.split('.')[-1].lower()
        if extension not in self.extensions:
            valid_extensions = ', '.join(self.extensions)
            raise ValidationError(f"Invalid file extension. Only {valid_extensions} files are allowed.")

#Allowed Image extensions
image_extensions = ['jpeg', 'jpg', 'gif', 'png']



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    date_birth = models.DateField(blank=True, null=True)
    phone_number = models.CharField(max_length=11, blank=True, null=True)
    email = models.EmailField()
    phone = PhoneNumberField()
    image = ProcessedImageField(
                                    upload_to='profile_images',
                                    processors=[Transpose(), ResizeToFill(150, 200)],
                                    format='JPEG',
                                    options={'quality': 97},
                                    validators=[FileExtensionValidator(image_extensions)],
                                    default='avatar.jpg'
                                )
    last_updated = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user.email
    
class UserContact(models.Model):
    COUNTRY_CHOICES = [
        ('Nigeria', 'Nigeria'),
        ('Ghana', 'Ghana'),
        ('Niger', 'Niger'),
        ('Cameroon', 'Cameroon'),
        ('Chad', 'Chad'),
        ('Kenya', 'Kenya'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    country = models.CharField(max_length=20, choices=COUNTRY_CHOICES)
    contact_address = models.CharField(max_length=150, null=True, blank=True)
    home_address = models.CharField(max_length=150, null=True, blank=True)
    state_origin = models.CharField(max_length=36, null=True, blank=True)
    lga_origin = models.CharField(max_length=36, null=True, blank=True)
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user