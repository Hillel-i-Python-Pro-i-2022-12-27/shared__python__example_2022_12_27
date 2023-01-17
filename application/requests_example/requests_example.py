import json
import pathlib
import urllib.parse
from typing import TypeAlias

import requests

from application.config.paths import FILES_OUTPUT_PATH
from application.logging.loggers import get_core_logger

T_URL: TypeAlias = str


def make_request(
    session: requests.Session,
    url: T_URL,
    path: pathlib.Path,
) -> None:
    logger = get_core_logger()

    response = session.get(url)
    logger.info(f"{response=}")
    response_json = response.json()
    logger.info(f"{response_json=}")

    path.write_text(json.dumps(response_json, indent=2))

    url_part_to_image = response_json["url"]
    url_to_image = urllib.parse.urljoin(url, url_part_to_image)

    response_with_image = session.get(url_to_image)
    logger.info(f"{response_with_image=}")

    extension = response_json["file"].rsplit(".", maxsplit=1)[-1]
    path_image = FILES_OUTPUT_PATH.joinpath(f"cat.{extension}")
    path_image.write_bytes(response_with_image.content)


def requests_example() -> None:
    # url = "https://httpbin.org/get"
    url: T_URL = "https://cataas.com/cat?json=true"

    path = FILES_OUTPUT_PATH.joinpath("output.json")

    with requests.Session() as session:
        make_request(session=session, url=url, path=path)


# TODO Rename this here and in `requests_example`
