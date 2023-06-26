from django.urls import path
from . import views

app_name="blog"

urlpatterns=[
  path("",views.post_table,name="blog-post-table")
]