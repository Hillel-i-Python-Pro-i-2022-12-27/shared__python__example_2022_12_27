import pathlib
from typing import Final

from application.config.paths import FILES_OUTPUT_PATH

PAGES_PATH: Final[pathlib.Path] = FILES_OUTPUT_PATH.joinpath("pages")
