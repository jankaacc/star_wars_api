import pytest
import requests_mock


@pytest.fixture
def load_fixture(make_load_fixture):
    return make_load_fixture(__file__)


@pytest.fixture
def sw_api_mock(load_fixture):
    with requests_mock.Mocker() as m:
        m.get(
            "http://swapi:5000/api/people",
            text=load_fixture("sw_people_page_1.json"),
        )
        m.get(
            "http://swapi:5000/api/people/?page=2",
            text=load_fixture("sw_people_page_2.json"),
        )
        m.get(
            "http://swapi:5000/api/planets",
            text=load_fixture("sw_planets_page_1.json"),
        )
        m.get(
            "http://swapi:5000/api/planets/?page=2",
            text=load_fixture("sw_planets_page_2.json"),
        )
        m.get(
            "http://swapi:5000/api/planets/1/",
            text=load_fixture("sw_planet_1.json"),
        )
        m.get(
            "http://swapi:5000/api/planets/2/",
            text=load_fixture("sw_planet_2.json"),
        )
        m.get(
            "http://swapi:5000/api/planets/3/",
            text=load_fixture("sw_planet_3.json"),
        )
        yield m


@pytest.fixture
def people_csv(load_fixture):
    yield load_fixture("sw_people.csv")


@pytest.fixture
def people_csv_file_only(load_fixture):
    yield load_fixture("sw_people.csv", read_file=False)
