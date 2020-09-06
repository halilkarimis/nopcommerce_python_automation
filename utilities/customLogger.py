import logging


class LogGen:
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)

    logging.basicConfig(filename='.\\Logs\\automation.log', format='%(asctime)s: %(levelname)s: %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p')

    @staticmethod
    def loggen():
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
