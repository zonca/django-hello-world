from django.shortcuts import HttpResponse

def helloworld(request):
    return HttpResponse('Hello World <img src="/static/admin/img/icon-yes.svg">')
