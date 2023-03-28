from application.concurrency_example.concurrency_example import concurrency_example
from application.logging.init_logging import init_logging


# from application.requests_example.requests_example import requests_example


def main() -> None:
    # print(greetings())
    # files_example_txt()
    # files_example_csv()
    # requests_example()
    concurrency_example()


if __name__ == "__main__":
    init_logging()
    main()
