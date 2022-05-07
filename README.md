# arraylab
### A Python library for experimenting with Arrays.

#### Importing
```py
from arraylab import (...,)
```

#### Modules
```py
import arraylab.array
import arraylab.dictionary
import arraylab.stack
```

> NOTE: For each module, there is a corresponding class with the same name.


#### Classes
```py
class Array()  # From arraylab.array
Array.__init__(self, initial_list: list = None, /)
Array.include(self, other: Array, /) -> Array
Array.push(self, value: object, /) -> Array
Array.pop(self, index: int = -1, /) -> object
Array.select(self, index: int, /) -> object
Array.select_slice(self, start: int, end: int = -1, /) -> Array
```

```py
class Dictionary(...)  # From arraylab.dictionary
Dictionary.__init__(self, initial_list: list = None, /)
Dictionary.include(self, other: Dictionary, /) -> Dictionary
Dictionary.push(self, key: object, value: object, /) -> Dictionary
Dictionary.pop(self, key: object = None, /) -> object
Dictionary.select(self, key: object, /) -> object
```

```py
class Stack(...)  # From arraylab.stack
Stack.__init__(self, initial_array: Array = None, /)
Stack.include(self, other: Stack, /) -> Stack
Stack.push(self, value: object, /) -> Stack
Stack.drop(self, /) -> Stack
Stack.dump(self, /) -> Stack
Stack.duplicate(self, /) -> Stack
Stack.swap(self, /) -> Stack
Stack.over(self, /) -> Stack
Stack.rotate(self, /) -> Stack
Stack.select(self, key: int, /) -> object
```

#### Functions
```py
# From arraylab.utils
def array(initial_list: list = None, /) -> Array
def dictionary(initial_list: list = None, /) -> Dictionary
def stack(initial_array: Array = None, /) -> Stack
```

> By @marc-dantas