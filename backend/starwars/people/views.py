import logging

from django.shortcuts import get_object_or_404
from drf_spectacular.utils import OpenApiParameter, extend_schema
from petl import fromcsv
from rest_framework.generics import ListAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from starwars.people.models import PeopleDataset
from starwars.people.object_mappers import SWCsvExporter
from starwars.people.paginators import DatasetPaginator
from starwars.people.serializers import PeopleDatasetSerializer
from starwars.people.service import sw_service

logger = logging.getLogger(__file__)


class DownloadPeople(APIView):
    def get(self, request: Request, format=None) -> Response:
        logger.info("Downloading recent SW characters csv")
        people = sw_service.get_all_sw_characters()
        csv_filename = SWCsvExporter(
            sw_people=people,
        ).queryset_to_csv()
        PeopleDataset.objects.create(filename=csv_filename)
        return Response("ok")


class ListPeople(ListAPIView):

    serializer_class = PeopleDatasetSerializer
    queryset = PeopleDataset.objects.all()


class GetPeopleDetail(APIView):
    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="limit",
                description="Number of results shown",
                required=False,
                type=int,
            ),
            OpenApiParameter(
                name="offset",
                description="Start from offset result",
                required=False,
                type=int,
            ),
            OpenApiParameter(
                name="count_by",
                description="Count values occurrence",
                required=False,
                type=str,
            ),
        ]
    )
    def get(self, request: Request, pk: int) -> Response:
        dataset = get_object_or_404(PeopleDataset, pk=pk)
        table = fromcsv(dataset.dataset_path)

        paginator = DatasetPaginator()
        return paginator.get_response(request, table)
