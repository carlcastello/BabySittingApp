from django.conf.urls import url

from customer_portal.views.CustomerPortal import HomeView
from customer_portal.views.Authentication import SignUp
from customer_portal.views.ProfilePortal import ProfileView

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^user/register$', SignUp.as_view(), name='register'),
    url(r'^user/profile/(?P<profile_id>\w+)+$', ProfileView.as_view(), name='profile'),
    url(r'^user/services', HomeView.as_view(), name='services')

]