from functools import partial

from starwars.people.repository import SWRepository


class SWService:
    def __init__(self):
        self.repository = SWRepository()

    @staticmethod
    def _format_planets(results: list):
        return [planet["name"] for planet in results]

    @staticmethod
    def _format_characters(planets: list, results: list):
        people = []
        for character in results:
            planet_index = int(character["homeworld"].split("/")[-2]) - 1
            character["homeworld"] = planets[planet_index]
        people.extend(results)
        return people

    def get_all_sw_planets_names(self):
        res = self.repository.get_all_entities(
            module=self.repository.PLANETS, format=self._format_planets
        )
        return res

    def get_all_sw_characters(self):
        planets = self.get_all_sw_planets_names()
        format_characters = partial(self._format_characters, planets=planets)
        return self.repository.get_all_entities(
            module=self.repository.PEOPLE, format=format_characters
        )


sw_service = SWService()
