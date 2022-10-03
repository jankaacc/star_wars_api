from collections import OrderedDict

from petl import aggregate, dicts, nrows, rowslice
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response


class DatasetPaginator(LimitOffsetPagination):

    default_limit = 10
    max_limit = 20

    # This class has to many responsibilities

    def get_response(self, request, table):
        if count_by := self.get_count_by(request):
            columns = count_by.split(",")
            if len(columns) == 1:
                columns = count_by
            return self.count_by(table, columns)
        data = self.paginate_queryset(table, request)
        return self.get_paginated_response(data)

    def paginate_queryset(self, table, request, view=None):
        self.count = nrows(table)
        self.limit = self.get_limit(request)
        if self.limit is None:
            return None

        self.offset = self.get_offset(request)
        self.request = request
        if self.count > self.limit and self.template is not None:
            self.display_page_controls = True

        if self.count == 0 or self.offset > self.count:
            return []
        return rowslice(table, self.offset, self.offset + self.limit)

    def get_offset(self, request):
        limit = super().get_offset(request)
        if limit > self.count:
            return self.count
        return limit

    def get_paginated_response(self, data):
        return Response(
            OrderedDict(
                [
                    ("count", self.count),
                    ("next", self.get_next_link()),
                    ("previous", self.get_previous_link()),
                    ("results", [i for i in dicts(data)]),
                ]
            )
        )

    def get_count_by(self, request):
        return request.query_params.get("count_by")

    def count_by(self, table, columns):
        return Response(
            OrderedDict(
                [
                    (
                        "results",
                        list(
                            dicts(
                                aggregate(table, key=columns, aggregation=len)
                            )
                        ),
                    )
                ]
            )
        )
