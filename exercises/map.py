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
        movies_multicountries = filter(lambda x: ',' in x['country'], list_of_movies)

        movies_multicountries_with_rating = filter(
            lambda x: x['rating_kinopoisk'] not in ['', '0'], movies_multicountries)

        result_list = [movie['rating_kinopoisk'] for movie in movies_multicountries_with_rating]

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

        filtered_movies = [movie['name'] for movie in list_of_movies if (
            movie['rating_kinopoisk'] != '' and float(movie['rating_kinopoisk']) >= rating)]

        result = list(map(lambda x: x.count(counted_letter), filtered_movies))

        return sum(result)
