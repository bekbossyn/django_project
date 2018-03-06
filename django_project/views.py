from django.http import HttpResponse


def test(request):
    return HttpResponse("<h1>test for PRODUCTION PsJ Real</h1>")
