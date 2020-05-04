from django.urls import path, re_path
from d_react.students import views

urlpatterns = [
    re_path(r'students/$', views.students_list),
    re_path(r'students/(?P<pk>\d+)$', views.students_detail),
]
