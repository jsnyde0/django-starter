from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home_view(request):
    return render(request, "pages/home.html")


def test_partial_view(request):
    if request.htmx:
        template = "pages/home.html#test-partial"
        return render(request, template)
    else:
        return HttpResponse(
            "HTMX not working; it should have replaced the button with a partial."
        )
