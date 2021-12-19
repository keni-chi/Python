# -*- coding: utf-8 -*-
import pandas as pd 
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from fw.base_service import BaseService
from fw.error_util import AppException
from fw.vizualize_util import VizualizeUtil


class AppService(BaseService):
    def __init__(self, logger):
        self.logger = logger
        self.target_name = 'species'
        self.df_Xy = None

    def init(self):
        self.logger.info('init---------start')
        # TODO: データの読み込みやdfへの整形など
        iris = load_iris()
        df_X = pd.DataFrame(iris.data, columns=iris.feature_names)
        df_y = pd.DataFrame(iris.target, columns=[self.target_name])
        self.df_Xy = pd.concat([df_X, df_y], axis=1)
        self.logger.info('init---------end')

    def preprocessing(self):
        self.logger.info('preprocessing---------start')
        # TODO: 前処理（外れ値チェック、欠損値処理、名寄せなど）

        # 欠損値を含む行を削除        
        self.df_Xy = self.df_Xy.dropna(how='any')
        self.logger.info('preprocessing---------end')

    def run(self):
        self.logger.info('run---------start')
        # TODO: アプリ処理

        # 説明変数と目的変数へ分割
        df_X = self.df_Xy.drop(self.target_name, axis=1)
        y_s = self.df_Xy[self.target_name]

        # 説明変数の平均値を計算
        df_X_mean = self.calc_mean(df_X)
        print(df_X_mean)

        # 学習データとテストデータに分割
        X_train, X_test, y_train, y_test = train_test_split(df_X, y_s, random_state=0)

        # ランダムフォレストのモデル構築
        model = RandomForestClassifier(n_estimators=20,n_jobs=-1)
        model.fit(X_train, y_train)

        #正解率
        print ("train正解率",model.score(X_train, y_train))
        print ("test正解率",model.score(X_test, y_test))

        #予測データ作成
        y_test_pred = model.predict(X_test)

        # 予測と正解の比較グラフの出力
        file_path = 'data/output_fig/test.png'
        VizualizeUtil.plot_pred_and_actual(file_path, y_test.tolist(), y_test_pred)

        # 意図的にエラーを発生させてAppServiceの以降の処理を実行しない
        raise AppException('[code:app001] サンプルappエラーのメッセージ')
        print('これは実行されない')
        self.logger.info('run---------end')

    def calc_mean(self, df_X):
        return df_X.mean()
