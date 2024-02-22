## Minimal django hello world project for testing purposes

It only has a single view in the root URL that prints Hello World and
a static file.

```python
# mysite.urls
path('', helloworld, name='homepage'),
# hello.views
def helloworld(request):
    return HttpResponse('Hello World <img src="/static/admin/img/icon-yes.svg">')
```

It is useful to check that Django works and that the web server can properly handle the static files.

