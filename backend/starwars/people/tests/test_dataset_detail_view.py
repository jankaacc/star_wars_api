from unittest import mock
from unittest.mock import PropertyMock

import pytest
from rest_framework.test import APIClient

CSV_TEST_FILE = "sw_people.csv"


@pytest.fixture()
def csv_dir(tmpdir):
    with mock.patch(
        "starwars.people.models.PeopleDataset.dataset_path",
        new_callable=PropertyMock,
    ) as m:
        m.return_value = "/app/starwars/people/tests/fixtures/sw_people.csv"
        yield m


def test_detail_view_return_paginated_dataset_entries(
    db, people_dataset_factory, people_csv_file_only, csv_dir
):
    dataset = people_dataset_factory(filename=CSV_TEST_FILE)
    client = APIClient()
    response = client.get(f"/backend/api/people/{dataset.id}/")
    response = response.json()
    assert response["count"] == 20
    assert (
        response["next"]
        == f"http://testserver/backend/api/people/{dataset.id}/?limit=10&offset=10"  # noqa
    )
    assert len(response["results"]) == 10


def test_detail_view_return_grouped_dataset_entries(
    db, people_dataset_factory, people_csv_file_only, csv_dir
):
    dataset = people_dataset_factory(filename=CSV_TEST_FILE)
    client = APIClient()
    response = client.get(
        f"/backend/api/people/{dataset.id}/?count_by=homeworld,gender"
    )
    response = response.json()
    assert response == {
        "results": [
            {"gender": "female", "homeworld": "Alderaan", "value": 1},
            {"gender": "male", "homeworld": "Alderaan", "value": 5},
            {"gender": "female", "homeworld": "Tatooine", "value": 1},
            {"gender": "male", "homeworld": "Tatooine", "value": 6},
            {"gender": "n/a", "homeworld": "Tatooine", "value": 2},
            {"gender": "hermaphrodite", "homeworld": "Yavin IV", "value": 1},
            {"gender": "male", "homeworld": "Yavin IV", "value": 3},
            {"gender": "n/a", "homeworld": "Yavin IV", "value": 1},
        ]
    }
