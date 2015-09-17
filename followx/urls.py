from django.conf.urls import include, url, patterns
from django.contrib import admin
from app.views import Home
from django.conf import settings


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', Home.as_view(), name='home'),
]
