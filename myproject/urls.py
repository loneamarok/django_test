"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
import job.views
import homepage.views

admin.site.site_header = 'XR App store Admin'
admin.site.site_title = 'XR App Store'
admin.site.index_title = 'Upload and Download apps'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('count/', views.count, name="count"),
    path('hello/', views.hello, name="hello"),
    path('about/', views.about, name="about"),
    path('', homepage.views.homepage, name="homepage"),
    path('topology', homepage.views.topology, name="topology"),
    path('blog/', include('blog.urls')),
    path('apps/', include('apps.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
