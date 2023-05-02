import asyncio

import bs4

from application.get_some_content_from_page.make_request import make_request
from application.get_some_content_from_page.typing import T_TEXT


# https://kustdnipro.com/ru/gyd-dlya-pereselentsev-bolee-polnogo-v-gorode-net/


# <article class="cust-article city-article ">


def parse_page__site__kust(soup: bs4.BeautifulSoup):
    # https://www.crummy.com/software/BeautifulSoup/bs4/doc/#navigating-the-tree
    article = soup.find("article", class_="cust-article city-article")

    is_found_section = False

    contact_data_list = []

    is_found_contact_data = False
    temp_item_lines = []
    for element in article.children:
        # If element is H4
        if element.name == "h4" and element.text == "III. Еда":
            is_found_section = True

        if is_found_section:
            if is_found_contact_data:
                if element.name == "p":
                    # Check about end of contact data
                    if tag_a := element.find("a"):
                        href = tag_a.get("href")

                        temp_item_lines.append(href)
                        contact_data_list.append(temp_item_lines)
                        temp_item_lines = []
                        is_found_contact_data = False
                        continue

                temp_item_lines.append(element.text)

            elif element.name == "p":
                if element.find("strong"):
                    is_found_contact_data = True
                    temp_item_lines.append(element.text)

    if temp_item_lines:
        contact_data_list.append(temp_item_lines)

    return contact_data_list


def get_data_from_page(text: T_TEXT):
    soup = bs4.BeautifulSoup(markup=text, features="html.parser")

    return parse_page__site__kust(soup=soup)


async def main():
    url = "https://kustdnipro.com/ru/gyd-dlya-pereselentsev-bolee-polnogo-v-gorode-net/"

    page__text = await make_request(url=url)

    data_from_page = get_data_from_page(text=page__text)

    for item in data_from_page:
        print(item)

    print()


def get_some_content_from_page_main():
    asyncio.run(main())
