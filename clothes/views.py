# -*- coding: utf-8 -*-
# Python imports


# Django imports
from django.views import generic


# Third party apps imports


# Local imports
from .models import Cloth


# Create your views here.
class IndexListView(generic.ListView):
    context_object_name = 'clothes'
    model = Cloth
    paginate_by = 1
    queryset = Cloth.objects.availables()
    template_name = 'clothes/index.html'


class NationalListView(IndexListView):
    queryset = Cloth.objects.nationals()
    template_name = 'clothes/national.html'


class InternationalListView(IndexListView):
    queryset = Cloth.objects.internationals()
    template_name = 'clothes/international.html'


class ClothDetailView(generic.DetailView):
    context_object_name = 'cloth'
    model = Cloth
    template_name = 'clothes/detail.html'
