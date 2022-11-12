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
        result = []

        for elem in input_list:
            if elem > max_elem:
                max_elem = elem

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
        # if len(input_list) == 0:
        #   return -1
        # if len(input_list) == 1 and input_list[0] != query:
        #   return -1
        # if input_list[len(input_list) // 2] == query:
        #   return
        pass


print(ListExercise.search([1], 900))
# ListExercise.search([1], 900) == -1
# ListExercise.search([1], 1) == 0
# ListExercise.search([], 900) == -1
# ListExercise.search([1, 4, 5, 7, 8, 9], 9) == 5
# ListExercise.search([1, 4, 5, 7, 8, 9], 1) == 0
# ListExercise.search([1, 4, 5, 7, 8, 9], 6) == -1
