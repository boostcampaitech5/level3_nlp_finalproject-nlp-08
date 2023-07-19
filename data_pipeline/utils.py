import logging
import os


def utilize_loggers(name):
    logger = logging.getLogger(__name__)
    logger_name = os.path.splitext(os.path.basename(name))[0]

    logging.basicConfig(
        filename=f"./artifact/{logger_name}.log",
        format="%(asctime)s | %(levelname)s: %(message)s",
        level=logging.INFO,
        datefmt="%Y/%m/%d %I:%M:%S %p",
    )

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)
    stream_handler.setFormatter(
        logging.Formatter("%(asctime)s | %(levelname)s: %(message)s")
    )
    logger.addHandler(stream_handler)
    return logger

