from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView

class CategoriesView(TemplateView):
  template_name = "categories/categories.html"
