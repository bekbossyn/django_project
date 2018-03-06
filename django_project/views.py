from django.http import HttpResponse


def test(request):
    return HttpResponse("<h1>Spotis 61</h1> <h1>Daniyar 005</h1><h1>two fellas are looking at me</h1>")

