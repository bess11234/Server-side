from django.urls import path

from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:question_id>/", views.DetailView.as_view(), name="detail"),
    path("<int:question_id>/vote/", views.VoteView.as_view(), name="vote")
]
