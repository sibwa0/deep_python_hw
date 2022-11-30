from collections import defaultdict
import logging
import logging.config
import sys

from utils import (
    # setup_logger,
    console_input,
    LOGGING_CONFIG
)

logging.config.dictConfig(LOGGING_CONFIG)

file_log = logging.getLogger("to_file")
output_log = logging.getLogger("to_stdout")


class LRUCache:

    def __init__(self, limit, **kwargs):
        self.kwargs = kwargs

        for _, val in self.kwargs.items():
            if val is not None:
                val.debug("Init LRUCache object")

        self.limit = limit
        self.size = 0
        self.def_dct = defaultdict(lambda val, size: (val, size))

    def get(self, key):
        if key not in self.def_dct:
            for _, val in self.kwargs.items():
                if val is not None:
                    val.error(
                        f"get :: Not key( {key} )"
                    )

            return None

        for _, val in self.kwargs.items():
            if val is not None:
                val.info(
                    f"get :: Found key( {key} ) ( {self.def_dct[key][0]} )"
                )
        return self.def_dct[key][0]

    def set(self, key, value):
        if self.size < self.limit:
            self.def_dct[key] = (value, self.size)
            self.size += 1

            for _, val in self.kwargs.items():
                if val is not None:
                    val.info(
                        f"set :: New :: key( {key} ) ( {value} ) :: "
                        f"size( {self.size} ), limit( {self.limit} )"
                    )

        elif self.size == self.limit:
            for _, val in self.kwargs.items():
                if val is not None:
                    val.debug(
                        "set :: Dict is full :: "
                        f"size( {self.size} ) = limit( {self.limit} )"
                    )

            for i in self.def_dct:
                for _, val in self.kwargs.items():
                    if val is not None:
                        val.debug(
                            f"set :: Current key( {i} )"
                            f"( {self.def_dct[i][0]} )"
                        )
                if self.def_dct[i][1] == self.size - 1:

                    if i == key:
                        for _, val in self.kwargs.items():
                            if val is not None:
                                val.info(
                                    f"set :: Same Key :: key( {i} ) "
                                    f"prev( {self.def_dct[i][0]} )"
                                    f" -> new( {value} )"
                                )
                    else:
                        for _, val in self.kwargs.items():
                            if val is not None:
                                val.info(
                                    "set :: New Instead :: "
                                    f"key( {i} ) ( {self.def_dct[i][0]} ) -> "
                                    f"key( {key} ) ( {value} )"
                                )
                        del self.def_dct[i]

                    self.def_dct[key] = (value, self.size - 1)

                    break

    def __str__(self) -> str:
        for _, val in self.kwargs.items():
            if val is not None:
                val.debug(f"{str(self.def_dct)}")

        return str(self.def_dct)


def main(**kwargs):
    cache = LRUCache(limit=2, **kwargs)

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

    if not console.s:
        output_log = None

    if console.s:
        file.addHandler(output)

    main(file)
