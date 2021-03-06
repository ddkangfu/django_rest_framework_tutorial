from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_rest_framework_tutorial.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include('snippets.urls')),

    url(r'^admin/', include(admin.site.urls)),
)


urlpatterns += patterns('',
    url(r'^api-auth/', include('rest_framework.urls',
                                namespace='rest_framework')),
)