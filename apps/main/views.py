# Python imports


# Django imports
from django.views.generic import DetailView, ListView


# Third party apps imports


# Local imports
from .models import Cloth


# Create your views here.
class IndexListView(ListView):
    context_object_name = 'clothes'
    model = Cloth
    paginate_by = 1
    queryset = Cloth.objects.available()
    template_name = 'main/index.html'


class NationalListView(IndexListView):
    queryset = Cloth.objects.national()
    template_name = 'main/national.html'


class InternationalListView(IndexListView):
    queryset = Cloth.objects.international()
    template_name = 'main/international.html'


class ClothDetailView(DetailView):
    context_object_name = 'cloth'
    model = Cloth
    template_name = 'main/detail.html'
