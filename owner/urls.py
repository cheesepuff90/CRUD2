from django.urls import path
from owner.views import OwnerListView, DogListView

urlpatterns = [
    path('/owner', OwnerListView.as_view()),
    path('/dog', DogListView.as_view()),
]