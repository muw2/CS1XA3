# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig
from django.http import JsonResponse


class AccountingBookConfig(AppConfig):
    name = 'accounting_book'


def success_json(data):
    dct = {
        "data": data,
        "info": {
            "code": 0,
            "error": False,
            "message": "ok",
        }
    }

    return JsonResponse(dct)


def error_json(message, code=-1):
    dct = {
        "data": '',
        "info": {
            "code": code,
            "error": True,
            "message": message,
        }
    }

    return JsonResponse(dct)

