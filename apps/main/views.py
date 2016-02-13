# Python imports


# Django imports
from django.shortcuts import render
from django.views.generic import View


# Third party apps imports


# Local imports
from .models import Category


# Create your views here.
class IndexView(View):
    def get(self, request, *args, **kwargs):
        template = 'main/index.html'

        hombre_category = Category.objects.filter(gender='HOMBRE')
        niño_category = Category.objects.filter(gender='NIÑO')
        context = {
            'hombre': hombre_category,
            'niño': niño_category
        }
        return render(request, template, context)
