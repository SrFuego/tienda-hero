# Python imports


# Django imports
from django.conf.urls import url


# Third party apps imports


# Local imports
from .views import Cloth, Index

# Create your tests here.


urlpatterns = [
    url(r'^$', Index.as_view(), name='index'),
    url(r'^detail/(?P<slug>[\w-]+)$', Cloth.as_view(), name='detail'),
]
