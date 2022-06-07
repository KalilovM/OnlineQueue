from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class CustomUserManager(BaseUserManager):
    
    def create_user(self, username, email, password):

        user = self.model(username=username,
                         email=email,
                         password=password)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username,email, password):
        
        user = self.create_user(
            username,
            email,
            password=password
        )
        user.is_superuser = True
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class NewUser(AbstractBaseUser):
    LANGUAGES = (
        ('English','English'),
        ('Russian','Russian')
    )
    username = models.CharField(max_length=50, unique=True, blank=False)
    name = models.CharField(max_length=50, blank=True, null=True)
    surname = models.CharField(max_length=50, blank=True)
    email = models.EmailField(null=True, blank=True)
    rating = models.FloatField(null=True, blank=True)
    profile_pic = models.ImageField(upload_to='images',default=None, null=True, blank=True)
    language = models.CharField(max_length=50, choices=LANGUAGES,null=True, blank=True)
    address = models.CharField(max_length=150,null=True, blank=True)
    start_date = models.DateTimeField(auto_now_add=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def __str__(self):
        return self.username
    
    def get_absolute_url(self):
        return '/user/%s/' % self.id
    