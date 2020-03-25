from django.urls import path
from basicapp import views
from django.contrib import admin
# template urls

app_name = 'basicapp'

# url patterns

urlpatterns=[
    # url('',views.index,name='index'),
    # url('admin/', admin.site.urls),
    path('register/',views.register,name='register'),
    path('user_login/',views.user_login,name='user_login'),
]