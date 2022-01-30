import logging

if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
        datefmt="%m/%d/%Y %I:%M:%S %p",
    )
    logging.info("I told you so!")
    logging.warning("This is fake warning log")
