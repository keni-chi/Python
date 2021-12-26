import app2_sub1

print('app2---start')

print(app2_sub1.x1)




import datetime
import log_util
import logging

# logger
logger = log_util.setup_logger('{0}.log'.format(datetime.date.today()))
# logger.setLevel(logging.DEBUG)  # INFO, DEBUG
logger.info('main------------start')
x = 'debug_test'
logger.debug(f'==={x}===')

logger.debug(f'==={app2_sub1.x1}===')

logger.info('main------------end')




print('app2---end')
raise Exception