import itertools


class CustomIterator:
    def __init__(self, max_value: int):
        self.max_value = max_value
        self.current_value = -1

    def __iter__(self):
        return self

    # def values(self):
    #     return range(self.max_value)
    #
    # def items(self)->tuple:
    #     ...
    # def keys(self):
    #     ...

    def __next__(self):
        if self.current_value >= self.max_value:
            raise StopIteration
        self.current_value += 1

        print(f"{self.current_value=}")

        return self.current_value


def main() -> None:
    # print(list(CustomIterator(10)))

    # for i in CustomIterator(10):
    #     print(f'{i=}')

    iterable = CustomIterator(10)
    part = itertools.islice(iterable, 3, 7)
    print(list(part))


if __name__ == "__main__":
    main()
