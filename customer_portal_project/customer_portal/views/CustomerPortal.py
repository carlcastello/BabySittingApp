from django.shortcuts import render

from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "customer_portal/home.html"


class ServicesView(TemplateView):
    template_name = "customer_portal/services.html"
