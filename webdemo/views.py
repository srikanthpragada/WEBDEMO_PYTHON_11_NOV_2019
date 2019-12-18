from django.http import HttpResponse


def welcome(request):
    # take value from parameter name in url
    if 'name' in request.GET:
        name = request.GET['name']
    else:
        name = 'Guest'
    return HttpResponse(f"<h1 style='color:blue'>{name}, welcome To Django</h1>")
