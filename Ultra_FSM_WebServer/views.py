import time
from django.shortcuts import render
from lib.DataProcess import fetch
from lib.api_get import api_get
# Create your views here.


def login(request):
    passwd = fetch()
    context = {"passwd": passwd, "url": "show/"}
    return render(request, 'login.html', context)


def show(request):
    lst = api_get()
    for item in lst:
        ltime = item.get("lastHbTime") if item.get("lastHbTime") else int(time.time())*1000
        item['lastHbTime'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(ltime)/1000))
    context = {"list": lst}
    return render(request, 'show.html', context)
