from django.urls import path
from .views import signupfunc,loginfunc, listfunc,logoutfunc,detailfunc, goodfunc, readfunc, BoardCreate, commentfunc, FirstSet, myprofilefunc, DetailProfile, UpdateProfile

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
    path('myprofile/', myprofilefunc, name='myprofile'),
    path('firstset/',FirstSet.as_view(), name='firstset'),
    path('UpdateProfile/<int:pk>', UpdateProfile.as_view(), name='UpdateProfile'),
    path('DetailProfile/<int:pk>', DetailProfile.as_view(), name='DetailProfile'),

]