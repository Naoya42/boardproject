from django.urls import path
from .views import signupfunc,loginfunc, listfunc,logoutfunc,detailfunc, goodfunc, readfunc, BoardCreate, commentfunc, DetailProfile, UpdateProfile, FirstSet

urlpatterns = [
    path('signup/', signupfunc, name='signup'),
    path('login/',loginfunc, name='login'),
    path('list/', listfunc, name='list'),
    path('logout/', logoutfunc, name='logout'),
    path('detail/<int:pk>', detailfunc, name='detail'),
    path('good/<int:pk>', goodfunc, name='good'),
    path('read/<int:pk>', readfunc, name='read'),
    path('create/', BoardCreate.as_view(), name='create'),
    path('comment/<int:pk>', commentfunc, name='comment'),
    path('UpdateProfile/<int:pk>', UpdateProfile.as_view(), name='UpdateProfile'),
    path('DetailProfile/<int:pk>', DetailProfile.as_view(), name='DetailProfile'),
    path('FirstSet', FirstSet.as_view(), name='FirstSet'),
]