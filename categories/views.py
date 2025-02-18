from django.http import HttpResponse
from django.views import View


class CategoriesView(View):
  def get(self, request):
    return HttpResponse("result")