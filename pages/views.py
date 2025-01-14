from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse
from django.shortcuts import render

from .models import TestImage


def home_view(request):
    if request.user.is_authenticated:
        images = TestImage.objects.filter(user=request.user)[:3]
    else:
        images = []
    context = {"images": images}
    return render(request, "pages/home.html", context)


def test_partial_view(request):
    if request.htmx:
        template = "pages/home.html#test-partial"
        return render(request, template)
    else:
        return HttpResponse(
            "HTMX not working; it should have replaced the button with a partial."
        )


@login_required
def test_image_hx(request):
    if not request.htmx:
        # raise 404
        raise Http404("View only works with HTMX.")

    if request.method == "POST" and request.FILES.get("image"):
        TestImage.objects.create(user=request.user, image=request.FILES["image"])

    # Return the latest 3 images
    images = TestImage.objects.filter(user=request.user)[:3]
    return render(request, "pages/home.html#image-list", {"images": images})
