from django.urls import path
from owners import views

urlpatterns = [path("", views.OwnerListView.as_view())]
