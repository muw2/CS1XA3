# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views import View
from apps import error_json, success_json
from models import User, Bill


# Create your views here.
class UserView(View):
    def get(self, request):
        if not request.session.get('is_login', None):
            return error_json(message='you have to login!')
        return success_json({
            "user_id": request.session.get('user_id', 0)
        })

    def post(self, request):
        user_name = request.POST.get("username")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if password1 != password2:
            return error_json(message='invalid password!')

        if User.objects.filter(name=user_name).exists():
            return error_json(message='repeat user name!')

        user = User(
            name=user_name,
            password=password1
        )
        user.save()
        request.session['is_login'] = True
        request.session['user_id'] = user.id
        request.session['user_name'] = user.name
        return success_json({
            "user_id": user.id
        })


def user_login(request):
    user_name = request.POST.get("username")
    password = request.POST.get("password")

    if request.session.get('is_login', None):
        return success_json(True)

    try:
        user = User.objects.get(name=user_name)
    except User.DoesNotExist as e:
        return error_json(message='invalid user name or password!')

    if user.password != password:
        return error_json(message='invalid user name or password!')

    request.session['is_login'] = True
    request.session['user_id'] = user.id
    request.session['user_name'] = user.name

    return success_json(True)


def user_logout(request):
    request.session.clear()
    return success_json(True)


class BillView(View):
    def get(self, request):
        if not request.session.get('is_login', None):
            return error_json(message='you have to login!')

        user_id = request.session.get('user_id')
        bills = Bill.objects.filter(user_id=user_id).all()
        result = []
        for bill in bills:
            result.append({
                "amount": bill.amount
            })
        return success_json(result)

    def post(self, request):
        if not request.session.get('is_login', None):
            return error_json(message='you have to login!')

        user_id = request.session.get('user_id')

        amount = request.POST.get("amount")
        desc = request.POST.get("desc")

        new_bill = Bill(
            amount=amount,
            desc=desc,
            user_id=user_id
        )

        new_bill.save()

        return success_json({
            "bill_id": new_bill.id
        })