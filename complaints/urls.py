from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^details/(?P<id>\d+)/$', views.details, name='details'),
    url(r'^form$', views.complaint_form, name='complaints'),
    url(r'^ajax/submit_complaints', views.ajax_form),
    url(r'^success$', views.success, name='success_form'),
    url(r'^complaint_status$', views.complaint_status, name='complaint_status'),

]