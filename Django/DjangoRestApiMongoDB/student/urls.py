from django.conf import settings
from django.urls import path,  include
from student import views
urlpatterns = [
    path(r'^api/student$', views.student_list),
    path(r'^api/student/(?P<pk>[0-9]+)$', views.student_detail),
    # path(r'^api/student/published$', views.student_list_published)
]
