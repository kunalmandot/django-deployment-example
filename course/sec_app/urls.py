from django.conf.urls import url
from sec_app import views
from django.urls import path

# urlpatterns = [
#     url(r'^$', views.index, name='index'),
# ]

urlpatterns = [
    path('', views.index, name='index'),
    path('form_page/', views.form_name_view, name='form_name'),
]

