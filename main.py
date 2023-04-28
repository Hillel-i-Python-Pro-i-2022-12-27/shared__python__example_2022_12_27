# from application.concurrency_example.async_crawler import async_crawler_main
# from application.argparse_example.argparse_example import argparse_example_main

# from application.requests_example.requests_example import requests_example

# from application.concurrency_example.asyncio_example import asyncio_example_main
# from application.concurrency_example.concurrency_example import concurrency_example
from application.logging.init_logging import init_logging


# from application.psutil_example.psutil_example import psutil_example_main


def main() -> None:
    # print(greetings())
    # files_example_txt()
    # files_example_csv()
    # requests_example()
    # concurrency_example()

    # for index, value in enumerate(range(1, 10)):
    #     print(f"{index=} {value=}")

    # asyncio_example_main()
    # async_crawler_main()

    # psutil_example_main()
    # argparse_example_main()

    ...


if __name__ == "__main__":
    init_logging()
    main()
