from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Wentylator.views.home', name='home'),
    url(r'^$', 'obliczenia.views.major'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^input_parameters/$','obliczenia.views.parametry_poczatkowe_forms'),
    url(r'^result/$','obliczenia.views.results'),
    url(r'^projects/$','obliczenia.views.projects'),
    url(r'^ventilator/calculation$','obliczenia.views.calculations'),
)
