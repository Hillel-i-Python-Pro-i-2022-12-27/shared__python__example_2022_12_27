import pathlib

import psutil


def get_current_stats():
    ...


def psutil_example_main():
    cpu_load = psutil.cpu_percent(interval=0.1)
    print(f"{cpu_load=}")
    memory_load = psutil.virtual_memory().percent
    print(f"{memory_load=}")
    swap_load = psutil.swap_memory().percent
    print(f"{swap_load=}")

    # disk_partitions = list(
    #     filter(lambda disk_partition: not disk_partition.device.startswith("/dev/loop"), psutil.disk_partitions())
    # )

    current_path = pathlib.Path(__file__).parent.absolute()

    disk_usage = psutil.disk_usage(str(current_path)).percent

    print(f"{disk_usage=}")
