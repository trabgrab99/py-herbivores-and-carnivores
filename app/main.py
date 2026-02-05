class Animal:
    alive = []

    def __init__(self,
                 name: str,
                 health: int = 100,
                 hidden: bool = False
                 ) -> None:
        self.health = health
        self.name = name
        self.hidden = hidden
        self.__class__.alive.append(self)

    def __repr__(self) -> str:
        return (
            f"{{Name: {self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )

    def alive_logic(self) -> list:
        self.__class__.alive = [
            obj for obj in self.__class__.alive
            if obj.health > 0
        ]
        return self.__class__.alive


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, obj: Animal) -> None:
        if isinstance(obj, Herbivore) and obj.hidden is False:
            obj.health -= 50
            if obj.health <= 0:
                self.__class__.alive.remove(obj)
