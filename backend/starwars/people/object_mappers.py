import csv
import os
from datetime import datetime
from functools import partial
from typing import Any, Optional

from django.utils.timezone import now

from starwars.people.const import CSV_FOLDER


def format_date(value: datetime) -> str:
    date = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%fZ")
    return date.strftime("%Y-%m-%d")


class SWCsvExporter:
    def __init__(self, sw_people: list):
        self.sw_people = sw_people
        self.ev = partial(partial, self._extract_values)

    def _extract_values(
        self,
        obj,
        key: str,
        cast_to: Optional[callable] = None,
    ) -> Any:
        value = obj[key]

        if cast_to:
            return cast_to(value)

        return value

    @property
    def csv_folder(self):
        return CSV_FOLDER

    @property
    def mapping(self) -> dict:
        return {
            "date": self.ev(key="edited", cast_to=format_date),
            "gender": self.ev(key="gender"),
            "birth_year": self.ev(key="birth_year"),
            "eye_color": self.ev(key="eye_color"),
            "hair_color": self.ev(key="hair_color"),
            "height": self.ev(key="height"),
            "homeworld": self.ev(key="homeworld"),
            "mass": self.ev(key="mass"),
            "name": self.ev(key="name"),
            "skin_color": self.ev(key="skin_color"),
        }

    def process_mapping(self, mapping: dict, obj):
        return [
            mapping_args(obj) for param_name, mapping_args in mapping.items()
        ]

    def queryset_to_csv(self):
        filename_date = now().strftime("%d_%m_%Y_%H:%M:%S.%f")
        filename = f"{self.csv_folder}/{filename_date}.csv"
        with open(filename, "w", encoding="UTF8", newline="") as f:
            writer = csv.writer(f, quoting=csv.QUOTE_ALL)
            writer.writerow(self.mapping.keys())

            for obj in self.sw_people:
                row = self.process_mapping(self.mapping, obj)
                writer.writerow(row)

            return os.path.basename(f.name)
