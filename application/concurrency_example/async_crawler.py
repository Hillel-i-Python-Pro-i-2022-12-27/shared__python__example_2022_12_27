import asyncio
import itertools
from typing import TypeAlias

import aiohttp
import bs4

import urllib.parse


T_URL: TypeAlias = str
T_URLS: TypeAlias = list[T_URL]

T_TEXT: TypeAlias = str


async def get_urls_from_text(text: T_TEXT) -> T_URLS:
    soup = bs4.BeautifulSoup(markup=text, features="html.parser")
    urls = []
    for link_element in soup.find_all("a"):
        url = link_element.get("href")
        urls.append(url)

    return list(set(urls))


async def make_request(url: str, session: aiohttp.ClientSession) -> T_TEXT:
    async with session.get(url) as response:
        return await response.text()


async def handle_url(url: str, session: aiohttp.ClientSession) -> T_URLS:
    text = await make_request(url=url, session=session)
    temp_urls = await get_urls_from_text(text=text)

    result_urls = []
    for temp_url in temp_urls:
        if not temp_url.startswith("http"):
            result_urls.append(urllib.parse.urljoin(base=url, url=temp_url))
        else:
            result_urls.append(temp_url)

    return result_urls


async def make_requests(urls: list[str]) -> T_URLS:
    # input_queue = asyncio.Queue()
    # for url in urls:
    #     await input_queue.put(url)

    async with aiohttp.ClientSession() as session:
        tasks = [handle_url(url=url, session=session) for url in urls]

        results = await asyncio.gather(*tasks)
        return list(itertools.chain(*results))


async def async_crawler():
    urls_input = [
        "https://example.com",
        "https://www.djangoproject.com/",
    ]

    urls_output = sorted(set(await make_requests(urls=urls_input)))
    print(urls_output)


def async_crawler_main():
    asyncio.run(async_crawler())
