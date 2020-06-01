from django.conf.urls import url
from . import views
from django.urls import path

# urlpatterns = [
#     url(r'^$', views.index, name='index'),
# ]

# Template Tagging
app_name = 'third_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('other/', views.other, name='other'),
    path('relative/', views.relative, name='relative'),
]

