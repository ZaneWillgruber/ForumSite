"""forumSite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from Discussion_Forum.views import *
from search.views import *
from userLogin.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', home, name='home'),
    path('<int:forum_id>/', detail, name='detail'),
    path('media/media/<str:filename>/', download_file, name='download_file'),
    path('addInForum/',addInForum, name='addInForum'),
    path('addInDiscussion/', addInDiscussion, name='addInDiscussion'),
    path('', include('userLogin.urls')),
    path('', include('activities.urls')),
    path('', include('shopping.urls')),
    path('', include('health.urls')),
    path('', include('search.urls')),
    path('', include('meeting.urls')),
    path('search/', search, name='search'),
    path('', include('cal.urls')),
    path('', include('chart.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
