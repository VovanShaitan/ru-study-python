from csv import DictReader
from typing import Union


class MapExercise:

    @staticmethod
    def rating(list_of_movies: list[dict]) -> float:
        """
        !!Задание нужно решить используя map!!
        Посчитать средний рейтинг фильмов (rating_kinopoisk), у которых две или больше стран.
        Фильмы у которых рейтинг не задан или равен 0 не учитывать в расчете среднего.
        :param list_of_movies: Список фильмов.
        Ключи словаря: name, rating_kinopoisk, rating_imdb, genres, year, access_level, country
        :return: Средний рейтинг фильмов у которых две или больше стран
        """
        def created_by_multicountries(film_country):
            return True if ',' in film_country else False

        def has_rating(film_rating_kinopoisk):
            return True if film_rating_kinopoisk not in ['', '0'] else False

        result_list = [film['rating_kinopoisk'] for film in list_of_movies if
                       has_rating(film['rating_kinopoisk']) and created_by_multicountries(film['country'])]

        return sum(list(map(float, result_list))) / len(result_list)

    @staticmethod
    def chars_count(list_of_movies: list[dict], rating: Union[float, int]) -> int:
        """
        !!Задание нужно решить используя map!!
        Посчитать количество букв 'и' в названиях всех фильмов с рейтингом (rating_kinopoisk) больше
        или равным заданному значению
        :param list_of_movies: Список фильмов
        Ключи словаря: name, rating_kinopoisk, rating_imdb, genres, year, access_level, country
        :param rating: Заданный рейтинг
        :return: Количество букв 'и' в названиях всех фильмов с рейтингом больше
        или равным заданному значению
        """
        counted_letter = 'и'

        filtered_films = [film['rating_kinopoisk'] for film in list_of_movies if (
            film['rating_kinopoisk'] != '' and float(film['rating_kinopoisk']) >= rating)]

        result = list(map(lambda x: x.count(counted_letter), filtered_films))
        return sum(result)


def list_of_movies(self) -> list[dict]:
    with open("tests/fixtures/movies.csv", "r") as movies:
        list_of_movies = list(DictReader(movies))
    return list_of_movies


print(MapExercise.rating(list_of_movies))
