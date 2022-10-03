from django.contrib import admin

from starwars.people.models import PeopleDataset


@admin.register(PeopleDataset)
class PeopleAdmin(admin.ModelAdmin):

    list_display = ("filename", "created_at")
