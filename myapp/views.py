import json, time, requests
from django.shortcuts import render
from django.http import HttpResponse
from lib.DataProcess import DataProcess
from lib.api_get import api_get
# Create your views here.


def login(request):
    # dbproc = DataProcess()
    # conn, cursor = dbproc.condb()
    # rs = dbproc.fetch(conn, cursor)
    # password = rs[1][1]
    context = {"passwd": "8877up", "url": "show/"}
    return render(request, 'login.html', context)


def show(request):
    lst = api_get()
    for item in lst:
        ltime = item.get("lastHbTime") if item.get("lastHbTime") else int(time.time())*1000
        item['lastHbTime'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(ltime)/1000))
    context = {"list": lst}

    return render(request, 'show.html', context)
