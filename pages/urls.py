from django.urls import path

from .views import home_view, test_image_hx, test_partial_view

urlpatterns = [
    path("", home_view, name="home"),
    path("hx/test-partial", test_partial_view, name="test-partial"),
    path("hx/test-image", test_image_hx, name="test-image-hx"),
]
