from random import shuffle


class ColoredObjectsService:
    """Сервис для работы с цветными объектами."""

    def __init__(self) -> None:
        self.__color_percent: dict[str, int] = {"BLUE": 55, "GREEN": 25, "RED": 20}

    @property
    def __items(self) -> list[str]:
        """Получить список объектов."""
        items = []
        for key, value in self.__color_percent.items():
            items += [key] * value
        return items

    async def choose(self, number: int) -> dict[str, str]:
        """Определить цвет предмета по номеру."""
        items = self.__items
        shuffle(items)
        return {"color": items[number - 1]}
