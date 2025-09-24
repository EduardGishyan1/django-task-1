from django.urls import path
from .views import (
    ChildProfileListCreateView,
    ChildrenListPageView,
    ChildrenAddPageView,
)

urlpatterns = [
    path("list-page", ChildrenListPageView.as_view(), name="children-list-page"),
    path("add-page",  ChildrenAddPageView.as_view(),  name="children-add-page"),

    path("", ChildProfileListCreateView.as_view(), name="children-list-create"),
]
