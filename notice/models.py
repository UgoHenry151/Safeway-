from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Notice(models.Model):
    notice_by= models.ForeignKey(User, on_delete=models.CASCADE)
    topic= models.CharField(max_length=200, blank=True, null= True)
    slug= models.SlugField(unique=True, null=False)
    notification_detail = models.TextField()
    image= models.ImageField(upload_to ='notication', default='notification.jpg', blank=True, null=True)
    date =models.CharField(max_length=150)
    viewed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.topic

    class Meta:
        db_table = 'notice'
        managed = True
        verbose_name = 'Notice'
        verbose_name_plural = 'Notices'