from unittest import mock
from unittest.mock import PropertyMock

import pytest
from freezegun import freeze_time
from rest_framework.test import APIClient

from starwars.people.models import PeopleDataset


@pytest.fixture()
def csv_tmp_dir(tmpdir):
    with mock.patch(
        "starwars.people.object_mappers.SWCsvExporter.csv_folder",
        new_callable=PropertyMock,
    ) as m:
        m.return_value = tmpdir
        yield m


@freeze_time("2021-12-06T12:00:00")
def test_csv_download_downloads_csv(db, sw_api_mock, csv_tmp_dir, people_csv):
    client = APIClient()
    client.get("/backend/api/people/download/")
    result_file_name = (
        f"{csv_tmp_dir.return_value}/06_12_2021_12:00:00.000000.csv"
    )
    with open(result_file_name, "r") as t1:
        result_file = t1.read()
        assert result_file == people_csv


@freeze_time("2021-12-06T12:00:00")
def test_csv_download_saves_model_Dataset(
    db, sw_api_mock, csv_tmp_dir, people_csv
):
    client = APIClient()
    client.get("/backend/api/people/download/")
    PeopleDataset.objects.get(filename="06_12_2021_12:00:00.000000.csv")
