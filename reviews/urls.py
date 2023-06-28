from django.urls import path

from . import views

urlpatterns = [
    path("", views.HomepageView.as_view(), name="homepage"),
    path("/thankyou",views.thankyou,name="thankyou")
]
