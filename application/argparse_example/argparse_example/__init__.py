import argparse
from typing import NamedTuple

from pydantic import BaseSettings, Field


class RunConfig(NamedTuple):
    name: str
    age: int
    is_something: bool


def from_cli() -> RunConfig:
    parser = argparse.ArgumentParser(description="Process some integers.")
    parser.add_argument("name", help="Name for processing")
    parser.add_argument("--age", help="Age for processing", type=int, default=10)
    parser.add_argument("--is-something", dest="is_something", help="Is something for processing", action="store_true")

    parsed_args = parser.parse_args()

    return RunConfig(
        name=parsed_args.name,
        age=parsed_args.age,
        is_something=parsed_args.is_something,
    )


class Settings(BaseSettings):
    name: str
    # age: str = Field(..., env='my_api_key')
    age: int = Field()
    is_something: bool = Field(default=False)

    class Config:
        env_file = ".env"


def from_env() -> RunConfig:
    settings = Settings()

    return RunConfig(
        name=settings.name,
        age=settings.age,
        is_something=settings.is_something,
    )


def argparse_example_main():
    # input_data = sys.argv

    # run_config = from_cli()
    #
    # print(run_config.age)

    # os_env = os.environ

    run_config = from_env()

    print(run_config)
