import os

import pytest

pytest_plugins = ["starwars.tests.fixtures"]


@pytest.fixture
def make_load_fixture():
    def _make_load_fixture(current_test_file):
        def _load_fixture(filename, bytes=False, read_file=True):
            mode = "rb" if bytes else "r"
            here = os.path.dirname(os.path.abspath(current_test_file))
            fixture_path = os.path.join(here, "fixtures", filename)
            with open(fixture_path, mode) as f:
                if read_file:
                    return f.read()
                return f

        return _load_fixture

    return _make_load_fixture
