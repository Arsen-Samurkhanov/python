# linearbag.py

class Bag:
    """Реализация структуры данных 'мешок' (bag) или мультимножества."""
    def __init__(self):
        """Создает пустой мешок."""
        self._items = list()

    def __len__(self):
        """Возвращает общее количество элементов (с учетом повторов)."""
        return len(self._items)

    def __contains__(self, item):
        """Позволяет использовать оператор 'in' для проверки наличия элемента."""
        return item in self._items

    def add(self, item):
        """Добавляет один элемент в мешок."""
        self._items.append(item)

    def remove(self, item):
        """Удаляет одно вхождение элемента из мешка.
        Вызывает ошибку AssertionError, если элемента нет.
        """
        assert item in self._items, "Элемент должен быть в мешке для удаления"
        # Находим индекс первого вхождения и удаляем его
        ndx = self._items.index(item)
        return self._items.pop(ndx)

    def __iter__(self):
        """Возвращает итератор для перебора элементов мешка."""
        return iter(self._items)