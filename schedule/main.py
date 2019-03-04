# -*- coding: utf-8 -*-
"""
定時実行する
"""
from crontab import CronTab
from datetime import datetime, timedelta
import logging
import math
from multiprocessing import Pool
import time
import os
from conf_path import DEV_ROOT_PATH

 
class JobConfig(object):
  """
  処理設定
  """
 
  def __init__(self, crontab):
    """
    :type crontab: crontab.CronTab
    :param crontab: 実行時間設定
    """
 
    self._crontab = crontab
 
 
  def schedule(self):
    """
    次回実行日時を取得する。
    :rtype: datetime.datetime
    :return: 次回実行日時を
    """
 
    crontab = self._crontab
    return datetime.now() + timedelta(seconds=math.ceil(crontab.next()))
 
  def next(self):
    """
    次回実行時刻まで待機する時間を取得する。
    :rtype: long
    :retuen: 待機時間(秒)
    """
 
    crontab = self._crontab
    return math.ceil(crontab.next())
 
 
def job_controller(crontab):
  """ 
  処理コントローラ
  :type crontab: str
  :param crontab: 実行設定
  """
  def receive_func(job):
    import functools
    @functools.wraps(job)
    def wrapper():
 
      jobConfig = JobConfig(CronTab(crontab))
      logging.info("->- 処理を開始しました。")
 
      while True:
 
        try:
 
          # 次実行日時を表示
          logging.info("-?- 次回実行日時\tschedule:%s" %
            jobConfig.schedule().strftime("%Y-%m-%d %H:%M:%S"))
 
          # 次実行時刻まで待機
          time.sleep(jobConfig.next())
 
          logging.info("-!> 処理を実行します。")
 
          # 処理を実行する。
          job()
 
          logging.info("-!< 処理を実行しました。")
 
        except KeyboardInterrupt:
          break
 
      logging.info("-<- 処理を終了終了しました。")
    return wrapper
  return receive_func


@job_controller("00 13 * * *")
def job_1():
  path = 'cd '+ DEV_ROOT_PATH + 'job1 ; '
  job_com(path)


@job_controller("01 13 * * *")
def job_2():
  path = 'cd '+ DEV_ROOT_PATH + 'job2 ; '
  job_com(path)

# # １分毎に実行する。
# @job_controller("* * * * *")
# def job1():
#   """
#   処理1
#   """
#   # TODO:実行したい処理を書く。
#   logging.debug("処理1")
# 
# 
# # ２分毎に実行する。
# @job_controller("*/2 * * * *")
# def job2():
#   """
#   処理2
#   """
#   # TODO:実行したい処理を書く。
#   logging.debug("処理2")

def job_com(path):
  """
  共通
  """
  os.system(path + 'make xxx')


def main():
  """
  """
 
  # ログ設定
  logging.basicConfig(level=logging.DEBUG,
    format="time:%(asctime)s.%(msecs)03d\tprocess:%(process)d" +
      "\tmessage:%(message)s",
    datefmt="%Y-%m-%d %H:%M:%S")
 
  # 処理リスト作成
  jobs = [job_1, job_2]
 
  # 処理を並列に実行
  p = Pool(len(jobs))
  try:
    for job in jobs:
      p.apply_async(job)
    p.close()
    p.join()
  except KeyboardInterrupt:
    pass
 
 
if __name__ == "__main__":
 
  main()
