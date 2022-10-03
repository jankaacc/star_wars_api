from rest_framework.test import APIClient


def test_list_view_return_all_dataset_entries(db, people_dataset_factory):
    data_filenames = {
        data.filename for data in people_dataset_factory.create_batch(3)
    }
    client = APIClient()
    response = client.get("/backend/api/people/")
    response_filenames = {data["filename"] for data in response.json()}
    assert response_filenames == data_filenames
