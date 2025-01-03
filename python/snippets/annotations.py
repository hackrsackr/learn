import numpy as np

from typing import List, Dict, Tuple, Optional, Union, TypedDict

def add(x: int, y: int):
    return x + y

name: str = "John Doe"


age: int = 15

is_active: bool = True

values: List[int] = [1, 2, 3]

data: Dict[str, int] = {}

# Union type means x or y Union[x, y]
mixed_data: Dict[str, Union[int, str]] = {
    "1": 1,
    "two": "two",
    "zero": False
}
print(mixed_data)

for k, v in mixed_data.items():
    print(type(k), k, type(v), v)

class Movie(TypedDict):
    name: str
    year: int

movie: Movie = { 'name': 'belly',
                'year': 1999 }

print(movie, type(movie))

array_object = np.array([[1,2,3],[4,5,6]])
print(type(array_object))
coordinates: Tuple[float, float] = (10.2, 10.4)
pair: Tuple[str, float] = ("yo", 12.3)

optional_value: Optional[str] = None