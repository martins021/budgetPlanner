from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView

class ManagerView(TemplateView):
    template_name = "manager/manager.html"