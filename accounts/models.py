from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
from django.urls import reverse
from django.utils.translation import gettext as _
from random import randint
# Create your models here.


# In Order to disable case sensitivity in emails

class LowercaseEmailField(models.EmailField):
    """
    Override EmailField to convert emails to lowercase before saving.
    """
    def to_python(self, value):
        """
        Convert email to lowercase.
        """
        value = super(LowercaseEmailField, self).to_python(value)
        # Value can be None so check that it's a string before lowercasing.
        if isinstance(value, str):
            return value.lower()
        return value
    
#
class CustomUser(AbstractUser):
    # email = models.EmailField(_('email address'), unique=True)
    email = LowercaseEmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username',)
    objects = CustomUserManager()
    
    REGIONS = [
        ('AA', 'አዲስ አበባ'),
        ('DDW', 'ድሬደዋ'),
        ('OR', 'ኦሮሚያ'),
        ('AM', 'አምራ'),
        ('TG', 'ትግራይ'),
        ('AF', 'አፋር'),
        ('HR', 'ሀረሪ'),
        ('SD', 'ሲዳማ'),
        ('SNNPE', 'ደቡብ ክልል'),
        ('GM', 'ጋምቤላ'),
        ('BG', 'ቤኒሻንጉል ጉሙዝ'),
    ]
    
    SEX = [
        ('M', 'ወንድ'),
        ('F', 'ሴት'),
    ]

    region = models.CharField(choices=REGIONS, max_length=5)
    sex = models.CharField(choices=SEX, max_length=1)
    phone = models.CharField(max_length=13)
    
    TYPE = [
        ('buyer', 'ቤት ፈላጊ'),
        ('seller', 'ደላላ'),
    ]
    user_type = models.CharField(max_length=6, choices=TYPE)
    profile = models.ImageField(default='profiles/avatar.png', upload_to='profiles/')
    joined_at = models.DateTimeField(auto_now_add=True)
    
    # favorite_posts = models.ForeignKey(
    #     'ads.Post', on_delete=CASCADE
        
    # )
    
    # def get_absolute_url(self):
    #     return reverse('login')
    about_me = models.CharField(max_length=500, null=True, blank=True)
    def __str__(self):
        return self.email
    
def set_username(sender, instance, **kwargs):
    if not instance.username:
        instance.username = f"{instance.first_name}_{randint(100000,9999999)}"
        
models.signals.pre_save.connect(set_username, sender=CustomUser)

