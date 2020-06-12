from django.conf.urls import url, include
from . import views
# from .views import ChartData


urlpatterns = [
    url(r'^$', views.index),
    url(r'^weather$', views.weather),
    url(r'^gallery$', views.gallery),
    url(r'^video$', views.video),
    url(r'^_map$', views._map),
    url(r'^about$', views.about),
    url(r'^api/data$', views.get_data),

]