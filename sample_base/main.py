import  os, sys
sys.path.append('./fw')
from app_service import AppService
from fw.log_util import LogUtil
import datetime
import logging
logger = LogUtil.setup_logger('./log/{0}.log'.format(datetime.date.today()))
logger.setLevel(logging.INFO)  # INFO, DEBUG


def main():
    # サービスの実行
    app = AppService(logger)
    app.execute()
 

if __name__ == '__main__':
    main()
