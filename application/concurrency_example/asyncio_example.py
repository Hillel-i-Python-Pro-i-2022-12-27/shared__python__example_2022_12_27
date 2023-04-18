import asyncio
import random


async def make_something():
    print("Hello")
    await asyncio.sleep(1)
    print("World")


async def make_something_2(number: int):
    print(f"Hello {number}")
    time_to_wait = random.randint(1, 5)
    await asyncio.sleep(time_to_wait)
    print(f"World {number}")


async def asyncio_example():
    # await make_something()

    tasks = [make_something_2(number=number) for number in range(1, 10)]

    results = await asyncio.gather(
        *tasks,
    )

    print(results)


def asyncio_example_main():
    asyncio.run(asyncio_example())
    asyncio.get_event_loop().run_until_complete(asyncio_example())
