from django.conf.urls import url, include

from . import views

app_name="lifeline"

urlpatterns = [
    url(r'^$', views.index, name='index'),
        # ex: /lifeline/map/
	url(r'^map/$', views.map,name="map"),
	url(r'^item/(?P<item_id>[0-9]+)/$', views.item, name='item'),
	url(r'^create/$', views.create,name="create"),
	url(r'^submitted/$', views.submitted, name="submitted"),
    url('^', include('django.contrib.auth.urls'))
]
