import concurrent.futures
import multiprocessing
import os
import queue
import random
import time
from typing import NamedTuple

from application.logging.loggers import get_core_logger


class Result(NamedTuple):
    number: int
    result: int


def do_something(number: int) -> Result:
    logger = get_core_logger()
    logger.info(f"Make calculations for {number}")

    time_to_sleep = random.randint(1, 5)
    logger.info(f"Sleep for {time_to_sleep} seconds. Number is {number}.")
    time.sleep(time_to_sleep)
    logger.info(f"Finish sleep for {time_to_sleep} seconds. Number is {number}.")

    return Result(number=number, result=number**2)


def do_something_by_queue(
    input_queue: multiprocessing.Queue,
    output_queue: multiprocessing.Queue,
    pseudo_cache: multiprocessing.Manager().dict,
) -> None:
    logger = get_core_logger()
    logger.info("Start calculations by queue")
    while input_queue.qsize():
        try:
            logger.info(f"Wait for item. Queue: {input_queue.qsize()=}, {output_queue.qsize()=}, {os.getpid()}")
            number = input_queue.get(timeout=1)
        except queue.Empty:
            logger.info("Queue is empty")
            return

        try:
            result = pseudo_cache[number]
            logger.info(f"Result was found in cache. {result=}")
        except KeyError:
            result = do_something(number)
            pseudo_cache[number] = result

        output_queue.put(result)
        logger.info(
            f"Put result to output queue. Queue: {input_queue.qsize()=}, {output_queue.qsize()=}, {os.getpid()}"
        )


# Primitives for concurrency:
# Queue.
# Pipe.
# Lock.
# Semaphore.
# Event.
# Manager.


def concurrency_example():
    logger = get_core_logger()
    numbers = list(range(1, 100))

    logger.info("Start calculations")

    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = executor.map(do_something, numbers)

    # with concurrent.futures.ThreadPoolExecutor() as executor:
    #     results = executor.map(do_something, numbers)

    # results = low_level_multiprocessing()

    logger.info("Finish calculations")
    for result in results:
        logger.info(f"For {result.number} result is {result.result}")


def low_level_multiprocessing():
    numbers = list(range(1, 100))

    input_queue = multiprocessing.Queue()
    output_queue = multiprocessing.Queue()

    for number in numbers:
        input_queue.put(number)

    amount_of_workers = os.cpu_count()

    # psutil

    pseudo_cache = multiprocessing.Manager().dict()

    processes = []
    for _ in range(amount_of_workers):
        process = multiprocessing.Process(target=do_something_by_queue, args=(input_queue, output_queue, pseudo_cache))
        # thread = threading.Thread(target=do_something_by_queue, args=(input_queue, output_queue, pseudo_cache))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    results = []
    while output_queue.qsize():
        results.append(output_queue.get())

    return results
