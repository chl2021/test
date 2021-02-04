# -*- coding: utf-8 -*-

import requests

def api_get():
    url = "http://10.5.151.41:45518/bit-oa-probe/api/v1.0/agentservice/list"
    header = {
        "Accept": "application/json",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Content-Type": "application/json;charset=UTF-8",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36",
        "Authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0eXBlIjoidXNlciIsImlkIjoicm9vdCIsIm5hbWUiOiLotoXnuqfnrqHnkIblkZgiLCJjb25zdW1lciI6IkJJVC1NU0EiLCJ0ZW5hbnRJZCI6ImFkbWluIiwic2VjcmV0X2lkIjoiNUNGQ0I1NDdGN0RDNDIyNUFFRjNDMkQzRDg4NUJENDQiLCJpc3MiOiJCSVQtTVNBIiwiaWF0IjoxNjEwNTA1ODQ3LCJuYmYiOjE2MTA1MDU4NDcsImV4cCI6MTYxMzA5ODE0N30.gtXP6sAJDpbYa2v_Y7DL0YdtaNFNjYrFkZxyCp4fv3I",
    }
    response = requests.get(url, headers=header)
    result = response.text.replace("null", "None")
    rs = eval(result).get("result")
    return rs
