from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)

    REGIONS = [
        ('Addis Ababa', 'አዲስ አበባ'),
        ('Diredawa', 'ድሬደዋ'),
        ('Oromia', 'ኦሮሚያ'),
        ('Amhara', 'አምራ'),
        ('Tigrai', 'ትግራይ'),
        ('Afar', 'አፋር'),
        ('Harari', 'ሀረሪ'),
        ('Sidama', 'ሲዳማ'),
        ('South Nations', 'ደቡብ ክልል'),
        ('Gambella', 'ጋምቤላ'),
        ('Benishangul Gumuz', 'ቤኒሻንጉል ጉሙዝ'),
    ]

    # address
    
    region = models.CharField(choices=REGIONS, max_length=30)
    town = models.CharField(max_length=30)
    address = models.CharField(max_length=300)
    
    photo_1 = models.ImageField(upload_to='home/')
    photo_2 = models.ImageField(upload_to='home/')
    photo_3 = models.ImageField(upload_to='home/')
    photo_4 = models.ImageField(upload_to='home/')
    

    # detailed description

    body = models.TextField()
    CAT = [
        ('studio', 'ስቱድዮ'),
        ('apartment', 'አፓርታማ'),
        ('condominium', 'ኮንዶሚኒየም'),
        ('office', 'ቢሮ'),
        ('other', 'ሌላ')
    ]
    category = models.CharField(max_length=50, choices=CAT)
    rental_rate = models.IntegerField()

    # landloard

    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )    
    
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(get_user_model(), related_name="post_likes")
    
    def number_of_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('view', args=[str(self.id)])

    
class Comment(models.Model):
    ad = models.ForeignKey(
        Post, on_delete=models.CASCADE,
        related_name='comments',
    )
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    
    comment = models.CharField(max_length=250)
    
    written_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse('view',  args=[str(self.ad.id)])
