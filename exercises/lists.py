class ListExercise:
    @staticmethod
    def replace(input_list: list[int]) -> list[int]:
        """
        Заменить все положительные элементы целочисленного списка на максимальное значение
        элементов списка.
        :param input_list: Исходный список
        :return: Список с замененными элементами
        """
        max_elem = 0
        for elem in input_list:
            if elem > max_elem:
                max_elem = elem

        result = []
        for elem in input_list:
            if elem > 0:
                result.append(max_elem)
            else:
                result.append(elem)

        return result

    @staticmethod
    def search(input_list: list[int], query: int) -> int:
        """
        Реализовать двоичный поиск
        Функция должна возвращать индекс элемента
        :param input_list: Исходный список
        :param query: Искомый элемент
        :return: Номер элемента
        """
        inside_input_list = input_list
        inside_query = query

        def custom_binary_search(inside_input_list: list[int], inside_query: int,
                                 min: int = 0, max: int = len(inside_input_list) - 1) -> int:
            """
            Функция возвращает индекс элемента
            :param inside_input_list: Исходный список
            :param inside_query: Искомый элемент
            :param min: Индекс элемента с минимальным значением
            :param max: Индекс элемента с максимальным значением
            :return: Номер элемента
            """
            if min > max or inside_query > inside_input_list[max] or inside_query < inside_input_list[min]:
                return -1

            mid = (min + max) // 2
            if inside_input_list[mid] == inside_query:
                return mid

            if inside_input_list[mid] > inside_query:
                return custom_binary_search(inside_input_list, inside_query, min, mid - 1)
            else:
                return custom_binary_search(inside_input_list, inside_query, mid + 1, max)

        return custom_binary_search(inside_input_list, inside_query)
