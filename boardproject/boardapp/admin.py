from django.contrib import admin
from .models import BoardModel,MyProfileModel
# Register your models here.
#アプリでデータ読み込むためにはここにmodelsのクラスを書かねばならない
admin.site.register(BoardModel)
admin.site.register(MyProfileModel)