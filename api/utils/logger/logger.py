import logging


class Logger(object):
    def __init__(self):
        self.logger = logging.getLogger("cache_logger")
        self.logger.setLevel(logging.DEBUG)
        self.handler = logging.StreamHandler()
        self.handler.setLevel(logging.DEBUG)
        default_fmt = logging.Formatter(
            fmt="%(asctime)s| %(name)s | %(levelname)s | %(message)s",
            datefmt="%Y/%m/%d %I:%M:%S %p",
        )
        self.handler.setFormatter(default_fmt)
        self.logger.addHandler(self.handler)

    def set_new_format(self, new_fmt):
        new_formatter = logging.Formatter(new_fmt, datefmt="%Y/%m/%d %I:%M:%S %p")
        self.handler.setFormatter(new_formatter)

    def log_caching(self, msg):
        self.logger.info(msg)


if __name__ == "__main__":
    logger = Logger()
    logger.log_caching("Hello")
