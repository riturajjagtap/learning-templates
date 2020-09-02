from django.conf.urls import url
from basicapp import views

# Template tagging
app_name = 'basicapp'

urlpatterns = [
    url(r'^relative/$', views.relative, name = 'relative'),
    url(r'^other/$', views.otherpage, name = 'other'),
]
