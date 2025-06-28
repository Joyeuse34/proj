from django.urls import path 
from . import views

app_name = 'file_upload' 
urlpatterns = [ path('', views.upload_and_process, name='upload_and_process'), ]