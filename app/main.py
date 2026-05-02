class Animal:
    alive = []

    def __init__(self,
                 name: str,
                 hidden: bool = False) -> None:
        self.health = 100
        self.name = name
        self._hidden = hidden
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (
            f"{{Name: {self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self._hidden}}}"
        )


class Herbivore(Animal):

    def __init__(self,
                 name: str,
                 hidden: bool = False) -> None:
        super().__init__(name, hidden)

    def hide(self) -> None:
        self._hidden = not self._hidden


class Carnivore(Animal):

    def __init__(self,
                 name: str,
                 hidden: bool = False) -> None:
        super().__init__(name, hidden)

    def bite(self, animal: Animal) -> None:
        if isinstance(animal, Carnivore):
            return

        if animal._hidden:
            return

        animal.health -= 50

        if animal.health <= 0:
            animal.health = 0
            Animal.alive.remove(animal)
