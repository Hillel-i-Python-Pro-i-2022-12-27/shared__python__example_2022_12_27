from application.logging.init_logging import init_logging
from application.requests_example.requests_example import requests_example


def main() -> None:
    # print(greetings())
    # files_example_txt()
    # files_example_csv()
    requests_example()


if __name__ == "__main__":
    init_logging()
    main()
