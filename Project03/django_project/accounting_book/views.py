# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.views import View


# Create your views here.
class UserView(View):
    def get(self, request):
        return HttpResponse("Hello, world. You're at the users get function")
    
    def post(self, request):
        user_name = request.POST.get("username")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if password1 != password2:
            pass

        return HttpResponse(user_name)

    
class BilldView(View):
    def get(self, request):
        pass

