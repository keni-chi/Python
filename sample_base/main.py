# -*- coding: utf-8 -*-
# パスの設定
import  os, sys
sys.path.append('./fw')

# ログの準備
from fw.src.log_util import LogUtil
import datetime
import logging
logger = LogUtil.setup_logger('./log/{0}.log'.format(datetime.date.today()))
logger.setLevel(logging.INFO)  # INFO, DEBUG

# 必要なモジュールをimport
from app_service import AppService


def main():
    # サービスの実行
    app = AppService(logger)
    app.execute()
 

if __name__ == '__main__':
    main()
