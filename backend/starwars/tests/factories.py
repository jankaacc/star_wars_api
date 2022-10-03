import factory
from faker import Faker

from starwars.people.models import PeopleDataset

faker = Faker(["en"])


class PeopleDatasetFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = PeopleDataset

    @factory.lazy_attribute
    def filename(self):
        name = faker.date_time().strftime("%d_%m_%Y_%H:%M:%S.%f")
        return f"{name}.csv"
