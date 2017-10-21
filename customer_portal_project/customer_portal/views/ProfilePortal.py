
from django.views.generic import TemplateView


class ProfileView(TemplateView):
    template_name = "profile_portal/profile_view.html"