from django.urls import path
from .views import (
    ChildProfileListCreateView,
    ChildrenListPageView,
    ChildrenAddPageView,
)

urlpatterns = [
    path("children/list-page", ChildrenListPageView.as_view(), name="children-list-page"),
    path("children/add-page",  ChildrenAddPageView.as_view(),  name="children-add-page"),

    path("children", ChildProfileListCreateView.as_view(), name="children-list-create"),
]
