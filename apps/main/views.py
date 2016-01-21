# Python imports


# Django imports
from django.views.generic.base import TemplateView


# Third party apps imports


# Local imports


# Create your views here.
class IndexView(TemplateView):
    template_name = 'main/index.html'
