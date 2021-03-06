from django.urls import re_path
from . import views
app_name = "students"
urlpatterns = [
re_path(r'^api/$', views.home),
re_path(r'^api/students/$', views.students_list),
re_path(r'^api/students/(?P<pk>\d+)$', views.students_detail),
]
