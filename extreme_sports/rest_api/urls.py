from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.LocationsList.as_view(), name='ExtremeSportsList'),
    path('<int:pk>', views.LocationDetail.as_view(), name='ExtremeSportsDetail'),
]
urlpatterns = format_suffix_patterns(urlpatterns)