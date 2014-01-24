from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),  
)

urlpatterns += patterns('mysite.views',
    ('^hello/$', 'hello'),
    ('^time/$', 'current_datetime'),
    (r'^time/plus/(\d{1,2})/$', 'hours_ahead'),
    ('^meta/$', 'display_meta'),
    (r'^contact-form/$', 'contact_form'),
    (r'^contact/$', 'contact'), 
)

urlpatterns += patterns('books.views',
    (r'^search-form/$', 'views.search_form'),
    (r'^search/$', 'views.search'),
)