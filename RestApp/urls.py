from django.conf.urls import include, url, patterns
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'api/', include('api.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
