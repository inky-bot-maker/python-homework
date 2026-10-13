class CycleList:
    def __init__(self, items: list):
        self._items = list(items)

    def __getitem__(self, index: int):
        if isinstance(index, slice):
            return self._items[index]
        if not self._items:
            raise IndexError("CycleList is empty")
        return self._items[index % len(self._items)]

    def __len__(self) -> int:
        return len(self._items)

    def __iter__(self):
        return iter(self._items)

    def __str__(self) -> str:
        return f"CycleList({self._items})"

    def __repr__(self) -> str:
        return f"CycleList({self._items!r})"


cl = CycleList([1, 2, 3])
print(cl[0])    
print(cl[3])     
print(cl[5])   
print(cl[-1])    
print(len(cl))   
print(list(cl)) 
print(cl)        