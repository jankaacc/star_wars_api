from django.urls import path

from starwars.people.views import DownloadPeople, GetPeopleDetail, ListPeople

urlpatterns = [
    path("people/download/", DownloadPeople.as_view(), name="people_download"),
    path("people/<int:pk>/", GetPeopleDetail.as_view(), name="people_detail"),
    path("people/", ListPeople.as_view(), name="people_list"),
]
