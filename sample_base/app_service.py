# -*- coding: utf-8 -*-
import pandas as pd 
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from fw.base_service import BaseService
from fw.vizualize_util import VizualizeUtil


class AppService(BaseService):
    def __init__(self, logger):
        self.logger = logger
        self.target_name = 'species'
        self.df_Xy = None
        self.df_X = None
        self.df_y = None

    def get_data(self):
        self.logger.info('get_data---------start')
        iris = load_iris()
        self.df_X = pd.DataFrame(iris.data, columns=iris.feature_names)
        self.df_y = pd.DataFrame(iris.target, columns=[self.target_name])
        self.df_Xy = pd.concat([self.df_X, self.df_y], axis=1)

    def preprocessing(self):
        self.logger.info('preprocessing---------start')
        # 欠損値処理、名寄せなど
        print(self.df_Xy.head())

    def main_processing(self):
        # 学習データとテストデータに分割
        y_s = self.df_y[self.target_name]
        X_train, X_test, y_train, y_test = train_test_split(self.df_X, y_s, random_state=0)

        # ランダムフォレストのモデル構築
        model = RandomForestClassifier(n_estimators=20,n_jobs=-1)
        model.fit(X_train, y_train)

        #正解率
        print ("train正解率",model.score(X_train, y_train))
        print ("test正解率",model.score(X_test, y_test))

        #予測データ作成
        y_train_pred = model.predict(X_train)
        y_test_pred = model.predict(X_test)

        # 予測と正解の比較グラフの出力
        VizualizeUtil.plot_pred_and_actual(y_train.tolist(), y_train_pred)
        VizualizeUtil.plot_pred_and_actual(y_test.tolist(), y_test_pred)
