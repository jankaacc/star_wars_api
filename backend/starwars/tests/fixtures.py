from pytest_factoryboy import register

from .factories import PeopleDatasetFactory

for factory in (PeopleDatasetFactory,):
    register(factory)
