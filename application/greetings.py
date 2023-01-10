from faker import Faker


def greetings() -> str:
    return f"Hello {Faker().first_name()}!"
