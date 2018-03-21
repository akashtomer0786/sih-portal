from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^types/$', views.types_of_cb, name='types_of_cyber_bullying'),
    url(r'^types/trolling$', views.type_trolling, name='type_trolling'),
    url(r'^types/trickery$', views.type_trickery, name='type_trickery'),
    url(r'^types/outing$', views.type_outing, name='type_outing'),
    url(r'^types/harrassment$', views.type_harrassment, name='type_harrassment'),
    url(r'^types/frapping$', views.type_frapping, name='type_frapping'),
    url(r'^types/fakeprofile$', views.type_fakeprofile, name='type_fakeprofile'),
    url(r'^types/exclusion$', views.type_exclusion, name='exclusion'),
    url(r'^types/cyberstalking$', views.type_cyberstalking, name='type_cyberstalking'),
    url(r'^types/catphishing$', views.type_catphishing, name='type_catphishing'),
    url(r'^$', views.homepage, name='home'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)