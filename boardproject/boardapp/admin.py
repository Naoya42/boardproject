from django.contrib import admin
from .models import BoardModel
# Register your models here.
#アプリでデータ読み込むためにはここにmodelsのクラスを書かねばならない
admin.site.register(BoardModel)