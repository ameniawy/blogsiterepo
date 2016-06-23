"""blogsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from blog import views

urlpatterns = [
	url(r'^login/$', 'django.contrib.auth.views.login',name="my_login"),
	#url(r'^accounts/', include('registration.backends.hmac.urls'))
    url(r'^admin', admin.site.urls),
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^add/', views.add, name='addblog'),
    url(r'^add', views.add, name='addblog'),
    url(r'^blog/', views.post, name='showblog'),
    url(r'^blog', views.post, name='showblog'),
    
    url(r'^user', views.add_user, name='adduser'),
    url(r'^user/', views.add_user, name='adduser'),

    url(r'^succ/', views.new_user, name='usercreated'),
    url(r'^succ', views.new_user, name='usercreated'),
    #url(r'^', views.error, name='notfound'),
    url(r'^loginsucc', views.login, name='showblog'),
    url(r'^loginsucc/', views.login, name='showblog'),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login',
       {'template_name': 'admin/login.html'}),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout'),
    url(r'^accounts/profile/$', views.profile, name="showprofile"),
]
