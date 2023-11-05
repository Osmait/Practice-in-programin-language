from abc import abstractmethod


class Repository(str):

    @abstractmethod
    def save(dato: str):
        pass

    @abstractmethod
    def find() -> list[str]:
        pass


class ImpRepository(Repository):
    list_dato: list[str] = []

    def save(self, dato: str):
        self.list_dato.append(dato)

    def find(self) -> list[str]:
        return self.list_dato


repository: Repository = ImpRepository()

repository.save("hola")
repository.save("Prueba")
list = repository.find()

print(list)
