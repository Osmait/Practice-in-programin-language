from __future__ import annotations
from abc import ABC, abstractmethod

from random import randrange


class Observer(ABC):
    @abstractmethod
    def update(self, subject: Subject) -> None:
        pass


class Subject(ABC):

    @abstractmethod
    def attach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass

    @abstractmethod
    def get_state(self) -> int:  # Nuevo método para obtener el estado
        pass


class ConcreteSubject(Subject):

    _state: int = 0
    _observers: list[Observer] = []

    def attach(self, observer: Observer) -> None:
        print("Subject:Attached an observer")
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self) -> None:
        print("Subject: Notifying observers...")
        for observer in self._observers:
            observer.update(self)

    def some_business_logic(self) -> None:

        print("\nSubject: I'm doing something important.")
        self._state = randrange(0, 10)

        print(f"Subject: My state has just changed to: {self._state}")
        self.notify()

    def get_state(self) -> int:
        return self._state  # Implementa el método para obtener el estado


class ConcreteObserverA(Observer):
    def update(self, subject: Subject) -> None:
        state = subject.get_state()
        if state < 3:
            print("ConcreteObserverA: Reacted to the event")


class ConcreteObserverB(Observer):
    def update(self, subject: Subject) -> None:
        state = subject.get_state()
        if state == 0 or state >= 2:
            print("ConcreteObserverA: Reacted to the event")


if __name__ == "__main__":
    # The client code.

    subject = ConcreteSubject()

    observer_a = ConcreteObserverA()
    subject.attach(observer_a)

    observer_b = ConcreteObserverB()
    subject.attach(observer_b)

    subject.some_business_logic()
    subject.some_business_logic()

    subject.detach(observer_a)

    subject.some_business_logic()
