from django.db import models

# Create your models here.
class BoardModel(models.Model):#djangoはデフォルトではnullを受け付けない
	title = models.CharField(max_length=100)
	content = models.TextField()
	author = models.CharField(max_length=100)
	images = models.ImageField(upload_to='')#どこに画像を格納するか指定する。空欄だとsetingファイルで指定した場所になる
	good = models.IntegerField(null=True, blank=True, default=0)
	read = models.IntegerField(null=True, blank=True, default=0)
	readtext = models.CharField(max_length=100, null=True, blank=True, default='a')
	comment = models.CharField(max_length=200, null=True, blank=True, default='コメントしてね')
	Newcomment = models.CharField(max_length=200, null=True, blank=True, default='')
	commentuser = models.CharField(max_length=200, null=True, blank=True, default='')

class MyProfileModel(models.Model):#myprofile用のclass
	age = models.CharField(max_length=100, null=True, blank=True, default='a')#年齢
	hobby = models.CharField(max_length=100, null=True, blank=True, default='a')#趣味
	occupation = models.CharField(max_length=100, null=True, blank=True, default='a')#職業
	Residence = models.CharField(max_length=100, null=True, blank=True, default='a')#住処
	myimages = models.ImageField(upload_to='')
	author = models.CharField(max_length=100,null=True, blank=True)
	listofcreators = models.CharField(max_length=300,null=True, blank=True, default='a')




	
		