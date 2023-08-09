from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_form, name='upload-form'),
    path('list', views.list_dogs, name='list-view'),
    path('delete/<int:pk>/', views.delete_image, name='delete-image')
    # Add more URL patterns here
]
