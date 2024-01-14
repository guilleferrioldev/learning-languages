# Generator is efficient for writing fast and compact code. This is an advantage over Python iterators. They are also simpler to code than do custom iterator. Python iterator is more memory-efficient.

from sys import getsizeof
from time import time

class Iterator:
    def __init__(self, n: int) -> None:
        self.max: int = n - 1
    
    # This method is required to allow an iterator to be used with the for and in statements.
    def __iter__(self) -> int:
        self.current: int = -1
        return self 
    
    # Method returns the next element in the sequence. In the case of a finite iterator, once it reaches the end (defined by the termination condition), all of the subsequent calls to this method should should raise an exception.
    def __next__(self) -> int:
        self.current += 1 

        if self.current > self.max:
            raise StopIteration 

        return self.current 


def generator(n: int) -> int:
    yield from range(n)

def main() -> None:
    n: int = 1000
    start: float = time()
    for i in (x := Iterator(n)):
        pass
    print('Iterator took ', time() - start, ',bytes occupied in memory', getsizeof(x))

    start: float = time()
    for i in (y := generator(n)):
        pass
    print('generator took ', time() - start,',bytes occupied in memory' ,getsizeof(y))
    
    start: float = time()
    for i in (z := iter([i for i in range(n)])):
        pass
    print('iter took ', time() - start ,',bytes occupied in memory' ,getsizeof(z))
    
    
if __name__ == "__main__":
    main()



