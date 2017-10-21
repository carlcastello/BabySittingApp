from django.conf.urls import url

from customer_portal.views.CustomerPortal import HomeView
from customer_portal.views.Authentication import SignUp

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^user/register$', SignUp.as_view(), name='register'),
]