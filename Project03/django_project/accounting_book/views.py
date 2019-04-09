# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.views import View
from models import User, Bill


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

        user = User(
            name=user_name,
            password=password1
        )
        user.save()
        return HttpResponse(user.id)

    
class BillView(View):
    def get(self, request):
        user_id = request.GET.get('user_id')
        bills = Bill.objects.filter(user_id=user_id).all()
        return HttpResponse(len(bills))

    def post(self, request):
        amount = request.POST.get("amount")
        desc = request.POST.get("desc")
        user_id = request.POST.get("user_id")

        new_bill = Bill(
            amount=amount,
            desc=desc,
            user_id=user_id
        )

        new_bill.save()

        return HttpResponse(new_bill.id)


