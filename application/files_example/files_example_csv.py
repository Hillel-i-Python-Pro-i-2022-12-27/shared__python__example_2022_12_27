import csv
import pathlib
from typing import Final

from application.config.paths import FILES_OUTPUT_PATH
from application.files_example.generators import generate_humans, Human
from application.logging.loggers import get_core_logger

KEY__NAME: Final[str] = "name"
KEY__AGE: Final[str] = "age"


def write_from_csv(path: pathlib.Path) -> None:
    logger = get_core_logger()
    amount: int = 10
    with open(path, mode="w") as file:
        writer = csv.DictWriter(file, fieldnames=[KEY__NAME, KEY__AGE])

        writer.writeheader()
        for human in generate_humans(amount=amount):
            writer.writerow({KEY__NAME: human.name, KEY__AGE: human.age})

    logger.info(f"Path to file: file://{path}")


def read_from_csv(path: pathlib.Path) -> list[Human]:
    humans = []
    with open(path) as file:
        reader = csv.DictReader(file)
        for row in reader:
            human = Human(name=row[KEY__NAME], age=int(row[KEY__AGE]))
            humans.append(human)
    return humans


def files_example_csv() -> None:
    path_to_file = FILES_OUTPUT_PATH.joinpath("output.csv")

    write_from_csv(path=path_to_file)
    print(read_from_csv(path=path_to_file))
