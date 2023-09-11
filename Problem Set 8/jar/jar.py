class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Capacity can not be negative")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        if self.size + n > self.capacity:
            raise ValueError("Can not deposit that many cookies")
        self.size += n

    def withdraw(self, n):
        if n > self.size:
            raise ValueError("Can not withdraw that many cookies")
        self.size -= n

    # getter
    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

    # setter
    @capacity.setter
    def capacity(self, capacity):
        self._capacity = capacity

    @size.setter
    def size(self, size):
        self._size = size


def main():
    jar = Jar()
    jar.deposit(3)
    print(jar)


if __name__ == "__main__":
    main()
