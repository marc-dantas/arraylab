# Dictionary Library

class Dictionary:
    
    def __init__(self, initial_dict: dict = None, /) -> None:
        self.__list = initial_dict if isinstance(initial_dict, dict) else {}

    def push(self, value: object) -> 'Dictionary':
        self.__list.append(value)
        return self
        
    def pop(self, index: int = -1, /) -> object:
        return self.__list.pop(index)
    
    def select(self, index: int, /) -> object:
        return self.__list[index]
    
    def __len__(self) -> int:
        return len(self.__list)
    
    def __getitem__(self, index: int) -> int:
        return self.__list[index]
    
    def __setitem__(self, index: int, value: int) -> None:
        self.__list[index] = value
    
    def __delitem__(self, index: int) -> None:
        self.__list.pop(index)
    
    def __iter__(self) -> 'iter':
        return iter(self.__list)
    
    def __str__(self) -> str:
        comma_sep = ", ".join(f"{x!r}: {type(x).__name__}" for x in self.__list) or "empty"
        return f"arraylab.Dictionary[{comma_sep}]"
