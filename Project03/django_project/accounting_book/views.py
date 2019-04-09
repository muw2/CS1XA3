# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.views import View


# Create your views here.
class UserView(View):
    def get(self, request):
        return HttpResponse("Hello, world. You're at the users get function")
    
    def post(self, request):
        pass

    
class BilldView(View):
    def get(self, request):
        pass

