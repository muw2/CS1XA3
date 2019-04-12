# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig
from django.http import JsonResponse


class AccountingBookConfig(AppConfig):
    name = 'accounting_book'


def success_json(data):
    """
    return success json data
    :param data:
    :return:
    """
    dct = {
        "data": data,
        "info": {
            "code": 0,
            "error": False,
            "message": "ok",
        }
    }

    return _allow_json(JsonResponse(dct))


def error_json(message, code=-1):
    """
    return error message
    :param message:
    :param code:
    :return:
    """
    dct = {
        "data": False,
        "info": {
            "code": code,
            "error": True,
            "message": message,
        }
    }

    return _allow_json(JsonResponse(dct))


def _allow_json(response):
    """
    add header for ajax
    :param response:
    :return:
    """
    response.__setitem__('Access-Control-Allow-Origin', '*')
    return response

