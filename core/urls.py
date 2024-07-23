
from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    # Add other paths here
    path("test/", views.index2, name="index2"),
    path("sections/<int:num>", views.section, name="section")
]
