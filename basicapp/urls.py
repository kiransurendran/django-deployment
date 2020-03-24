from django.conf.urls import url
from basicapp import views
from django.contrib import admin
# template urls

app_name = 'basicapp'

# url patterns

urlpatterns=[
    # url('',views.index,name='index'),
    # url('admin/', admin.site.urls),
    url('register/',views.register,name='register')
]