from bankr.logger import Logger
from loguru import logger as log
from bankr.usbank import USBank


def main():
    log.info("Starting Program")
    logger = Logger()
    logger.load_config()
    bank = USBank()
    log.info("Ending Program")


if __name__ == "__main__":
    main()
    bank = USBank()
    bank.credit_transfer()
