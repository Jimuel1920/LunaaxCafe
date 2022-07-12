from django.db import models
from datetime import datetime
from django .utils import timezone
import os, random
from django.utils.html import mark_safe

# Create your models here.

now = timezone.now()


def image_path(instance, filename):
    basefilename, file_extension = os.path.splitext(filename)
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghjklmnopqrstuvwxyz1234567890'
    randomstr = ''.join((random.choice(chars)) for x in range(10))
    _now = datetime.now()

    return 'profile_pic/{year}-{month}-{imageid}-{basename}-{randomstring}{ext}'.format(imageid=instance,
                                                                                        basename=basefilename,
                                                                                        randomstring=randomstr,
                                                                                        ext=file_extension,
                                                                                        year=_now.strftime('%Y'),
                                                                                        month=_now.strftime('%m'),
                                                                                        day=_now.strftime('%d'))

#----- users
class user(models.Model):
    user_image = models.ImageField(upload_to=image_path, default='profile_pic/image.jpg')
    user_uid = models.IntegerField( max_length=500, verbose_name='UID')
    user_fname = models.CharField(max_length=200, verbose_name='First name')
    user_lname = models.CharField(max_length=200, verbose_name="Last name")
    user_position = models.CharField(max_length=200, verbose_name='Position')
    user_username = models.CharField(unique=True,max_length=200, verbose_name="Username")
    user_password = models.CharField(max_length=200, verbose_name="Password")
    pub_date = models.DateField(default=now)

    def __str__(self):
        return self.user_username

    def image_tag(self):
        return mark_safe('<img src ="/backend/media/%s" width ="50" height="50"/>' % (self.user_image))



#----- Comments
class Comment(models.Model):
    user_com =models.ForeignKey(user, on_delete=models.CASCADE, related_name='comments')
    name     = models.CharField(max_length=100)
    email    = models.EmailField(default='null')
    body     = models.TextField(default='null')
    created_on  = models.DateTimeField('date commented')
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'comment {} by {} '.format(self.body, self.name)

#--- porduct
class Product(models.Model):
    pro_image = models.ImageField(upload_to=image_path, default='profile_pic/image.jpg',null=True, blank= True)
    pro_id = models.CharField(max_length=50, verbose_name="Product id")
    pro_name =models.CharField(max_length=200, null=False, verbose_name="Product name")
    pro_price = models.DecimalField(max_digits=10, decimal_places=2)
    pro_size = models.CharField(max_length=200, verbose_name="Size")
    Catergoty = models.CharField(max_length=200, verbose_name="Catergory")
    digital =models.BooleanField(default=False, null=True, blank=False)


    def __str__(self):
        return self.pro_name

    def image_tag(self):
        return mark_safe('<img src ="/backend/media/%s" width ="50" height="50"/>' % (self.pro_image))
    
   


 #meatproduct

class Meat(models.Model):
    m_image = models.ImageField(upload_to=image_path, default='profile_pic/image.jpg')
    m_id = models.CharField(max_length=50, unique=True, verbose_name="Product id")
    m_name =models.CharField(max_length=200, null=False, verbose_name="Product name")
    m_price = models.DecimalField(max_digits=10, decimal_places=2)
    m_size = models.CharField(max_length=200, verbose_name="Size")
    m_cat = models.CharField(max_length=200, verbose_name="Catergory")

    def __str__(self):
        return self.m_id

    def image_tag(self):
        return mark_safe('<img src ="/backend/media/%s" width ="50" height="50"/>' % (self.m_image))


# product meat



