from allauth.account.views import confirm_email
from django.urls import re_path as url
from django.contrib import admin
from django.urls import path, include,re_path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('account/', include('allauth.urls')),
    path('accounts-rest/registration/account-confirm-email/(?P<key>.+)/$', confirm_email, name='account_confirm_email'),
]
