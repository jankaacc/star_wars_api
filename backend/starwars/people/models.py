from django.db import models

from starwars.core.models import TimeStampedModel
from starwars.people.const import CSV_FOLDER


class PeopleDataset(TimeStampedModel):

    filename = models.CharField(max_length=40, verbose_name="Filename")

    @property
    def dataset_path(self):
        return f"{CSV_FOLDER}/{self.filename}"
