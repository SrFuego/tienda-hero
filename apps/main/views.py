# Python imports


# Django imports
from django.views.generic import DetailView, ListView


# Third party apps imports


# Local imports
from .models import Clothes


# Create your views here.
class Index(ListView):
    context_object_name = 'prendas'
    model = Clothes
    paginate_by = 3
    template_name = 'main/index.html'


class Clothes(DetailView):
    model = Clothes
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    template_name = 'main/detail.html'
