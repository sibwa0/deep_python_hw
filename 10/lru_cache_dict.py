from collections import defaultdict
import logging
import logging.config
from sys import stdout
import sys

from utils import (
    # setup_logger,
    console_input,
    LOGGING_CONFIG
)


class LRUCache:

    def __init__(self, limit, logger):
        logger.debug("Init LRUCache object")

        self.logger = logger
        self.limit = limit
        self.size = 0
        self.def_dct = defaultdict(lambda val, size: (val, size))

    def get(self, key):
        if key not in self.def_dct:
            self.logger.error(
                f"get :: Not key( {key} )"
            )

            return None

        self.logger.info(
            f"get :: Found key( {key} ) ( {self.def_dct[key][0]} )"
        )
        return self.def_dct[key][0]

    def set(self, key, value):
        if self.size < self.limit:
            self.def_dct[key] = (value, self.size)
            self.size += 1

            self.logger.info(
                f"set :: New :: key( {key} ) ( {value} ) :: "
                f"size( {self.size} ), limit( {self.limit} )"
            )

        elif self.size == self.limit:
            self.logger.debug(
                "set :: Dict is full :: "
                f"size( {self.size} ) = limit( {self.limit} )"
            )

            for i in self.def_dct:
                self.logger.debug(
                    f"set :: Current key( {i} ) ( {self.def_dct[i][0]} )"
                )
                if self.def_dct[i][1] == self.size - 1:

                    if i == key:
                        self.logger.info(
                            f"set :: Same Key :: key( {i} ) "
                            f"prev( {self.def_dct[i][0]} ) -> new( {value} )"
                        )
                    else:
                        self.logger.info(
                            "set :: New Instead :: "
                            f"key( {i} ) ( {self.def_dct[i][0]} ) -> "
                            f"key( {key} ) ( {value} )"
                        )
                        del self.def_dct[i]

                    self.def_dct[key] = (value, self.size - 1)

                    break

    def __str__(self) -> str:
        self.logger.debug(f"{str(self.def_dct)}")

        return str(self.def_dct)


def main(logger):
    cache = LRUCache(limit=2, logger=logger)

    cache.set("k1", "val1")
    cache.set("k2", "val2")

    cache.set("k3", "val3")

    cache.set("k3", "val4")

    cache.get("k3")

    cache.get("k100")

    str(cache)


if __name__ == "__main__":
    parser = console_input()
    console = parser.parse_args(sys.argv[1:])

    # logging.config.dictConfig(LOGGING_CONFIG)
    # file = logging.getLogger("to_file")
    # output = logging.getLogger("to_stdout")

    file_formatter = logging.Formatter("%(asctime)s\t%(name)s\t%(levelname)s\t%(message)s")
    file_handler = logging.FileHandler("file.log")
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(file_formatter)

    logger = logging.getLogger("log")
    logger.setLevel(logging.DEBUG)
    logger.addHandler(file_handler)

    if console.s:

        output_formatter = logging.Formatter("%(name)s\t%(levelname)s\t%(message)s")
        stdout_handler = logging.StreamHandler(stdout)
        stdout_handler.setLevel(logging.INFO)
        stdout_handler.setFormatter(output_formatter)

        logger.addHandler(stdout_handler)

    main(logger)
