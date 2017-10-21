
from django.views import View
from django.shortcuts import render
from customer_portal.form.UserCreationForm import UserCreationForm


class SignUp(View):
    template_name = "auth/sign_up.html"

    def get(self, request, *args, **kwargs):
        form = UserCreationForm()
        return render(request, self.template_name, {'form': form})
