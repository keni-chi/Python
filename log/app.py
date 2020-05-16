import datetime
import log_util
import logging

# logger
log_folder = '{0}.log'.format(datetime.date.today())
logger = log_util.setup_logger(log_folder)
logger.setLevel(logging.DEBUG)  # INFO, DEBUG


def main():
    logger.info('main------------start')
    x = 'debug_test'
    logger.debug(f'==={x}===')
    logger.info('main------------end')


if __name__ == '__main__':
    print('start!')
    main()
    print('end!')
