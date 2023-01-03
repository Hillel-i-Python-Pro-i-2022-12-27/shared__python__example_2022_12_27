from typing import TypeAlias

T_NUMBER: TypeAlias = int
T_NUMBERS: TypeAlias = list[T_NUMBER]

T_MY_DICT: TypeAlias = dict[str, T_NUMBERS]


def make_list(amount_of_items: T_NUMBER = 10) -> T_NUMBERS:
    """Make list of numbers from 0 to amount_of_items - 1"""

    return list(range(amount_of_items))


def main(amount_of_items: T_NUMBER = 10) -> None:
    message = "Hello, World"
    for _ in range(amount_of_items):
        print(f'{message}!')

    print(make_list(amount_of_items=amount_of_items))


if __name__ == "__main__":
    main()
