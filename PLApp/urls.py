"""PLApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import include,url
from django.contrib import admin

from prelaunch.views import Index
from prelaunch import views as core_views

urlpatterns = [
	url(r'^admin/', admin.site.urls),
	url(r'^', include('prelaunch.urls')),

	#url(r'^prelaunch', include('prelaunch.urls')),
	#url(r'^$', Index.as_view()),
	# Python Social Auth URLs
	#url(r'^$', 'django_social_app.views.login'),
	#url('',       include('social.apps.django_app.urls', namespace='social')),
	#url('', include('django.contrib.auth.urls', namespace='auth')),
]
