from django.urls import path

from .views import (
    home_view,
    test_background_task,
    test_image_hx,
    test_partial_view,
    test_skeleton_hx,
)

urlpatterns = [
    path("", home_view, name="home"),
    path("hx/test-partial", test_partial_view, name="test-partial"),
    path("hx/test-image", test_image_hx, name="test-image-hx"),
    path("hx/test-skeleton", test_skeleton_hx, name="test-skeleton-hx"),
    path("hx/test-background-task", test_background_task, name="test-background-task"),
]
