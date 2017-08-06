from django.conf.urls import url
from . import views

urlpatterns = [   
  url(r'^form_render$', views.form_render),
  url(r'^form$', views.form),
  url(r'^index$', views.index),
  url(r'^create$', views.create),
]