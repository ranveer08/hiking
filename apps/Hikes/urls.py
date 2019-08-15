from django.conf.urls import url, include
from . import views
# from .views import ChartData


urlpatterns = [
    # url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^$', views.index),
    url(r'^weather$', views.weather),
    url(r'^gallery$', views.gallery),
    url(r'^video$', views.video),
    url(r'^_map$', views._map),
    url(r'^about$', views.about),
    url(r'^register$', views.register),
    url(r'^registerProcess$', views.registerProcess),
    url(r'^login$', views.login),
    url(r'^loginProcess$', views.loginProcess),
    url(r'^logout$', views.logout),
    url(r'^api/data$', views.get_data),
    # url(r'^api/chart/data$', ChartData.as_view()),
    url(r'^rattle$', views.rattle),
    url(r'^little$', views.little),

]