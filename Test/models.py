from django.db import models

# Create your models here.
class TourApi(models.Model):
    title = models.CharField(max_length=255)
    contentid = models.CharField(max_length=255)
    firstimage = models.CharField(max_length=255, blank=True, null=True)
    firstimage1 = models.CharField(max_length=255, blank=True, null=True)
    addr1 = models.CharField(max_length=255, blank=True, null=True)
    overview = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tour_api'
        
class User(models.Model):
    username = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    
    def __str__(self):
        return self.username

    class Meta: #메타 클래스를 이용하여 테이블명 지정
        db_table = 'test_user'