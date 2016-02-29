# Python imports


# Django imports
from django.views.generic import DetailView, ListView


# Third party apps imports


# Local imports
from .models import Cloth


# Create your views here.
class Index(ListView):
    context_object_name = 'clothes'
    model = Cloth
    paginate_by = 1
    template_name = 'main/index.html'


class Cloth(DetailView):
    context_object_name = 'cloth'
    model = Cloth
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    template_name = 'main/detail.html'
