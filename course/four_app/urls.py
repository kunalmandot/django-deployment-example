from django.conf.urls import url
from . import views
from django.urls import path

# urlpatterns = [
#     url(r'^$', views.index, name='index'),
# ]

app_name = 'four_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='logout'),
    path('special/', views.special, name='special'),
]

