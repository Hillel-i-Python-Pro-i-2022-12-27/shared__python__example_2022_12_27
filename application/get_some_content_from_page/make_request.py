import hashlib
import json

import aiohttp

from application.get_some_content_from_page.constants import PAGES_PATH
from application.get_some_content_from_page.typing import T_URL, T_TEXT
from application.logging.loggers import get_core_logger


async def make_request(url: T_URL) -> T_TEXT:
    logger = get_core_logger()
    hash_for_input = hashlib.sha3_512(url.encode())

    page_dir_path = PAGES_PATH.joinpath(f"{hash_for_input.name}:{hash_for_input.hexdigest()}")

    if not page_dir_path.exists():
        logger.info(f"Downloading page {url=}")
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                page__text = await response.text()

        page_dir_path.mkdir(parents=True, exist_ok=True)
        page_file_path = page_dir_path.joinpath("page.html")
        page_file_path.write_text(page__text, encoding="utf-8")

        info_file_path = page_dir_path.joinpath("info.json")
        info = {
            "url": url,
        }
        info_file_path.write_text(json.dumps(info, indent=2), encoding="utf-8")

    else:
        logger.info(f"Page already downloaded {url=}")
        info_file_path = page_dir_path.joinpath("info.json")
        info = json.loads(info_file_path.read_text(encoding="utf-8"))

        if info["url"] != url:
            raise ValueError("Different URL for same hash.")

        page_file_path = page_dir_path.joinpath("page.html")
        page__text = page_file_path.read_text(encoding="utf-8")

    logger.info(f"cache_folder: {page_dir_path.as_uri()}")
    logger.info(f"page: {page_file_path.as_uri()}")

    return page__text
