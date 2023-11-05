from typing import Any


class SingletonMeta(type):
    _instances:dict={}
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        if self not in self._instances:
            isinstance = super().__call__(*args, **kwds)
            self._instances[self] = isinstance

        return  self._instances[self]
    
class Singleton(metaclass=SingletonMeta):
    def __init__(self):
        pass


if __name__ == "__main__":
    s1 = Singleton()
    s2 = Singleton()
    print(s1==s2)
    print(s1 is s2)