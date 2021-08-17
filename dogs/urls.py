from django.urls import path
from dogs import views

urlpatterns = [path("", views.DogListView.as_view())]
