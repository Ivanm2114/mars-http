import logging

logging.basicConfig(level=logging.ERROR)


def log():

    logging.debug('Debug')
    logging.info('Info')
    logging.warning('Warning')
    logging.error('Error')
    logging.critical('Critical or Fatal')


if __name__ == '__main__':
    log()