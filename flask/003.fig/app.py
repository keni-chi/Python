#app.py
from flask import Flask, render_template
from io import BytesIO
import urllib
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure
import numpy as np

import sklearn.datasets as datasets
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

app = Flask(__name__)


def plot_pred_and_actual(y_pred, y_actual):
    # グラフ生成
    fig = plt.figure(figsize=(8,4))
    ax = fig.add_subplot(111)
    ax.scatter(2,2,color="white")
    ax.plot(y_pred,lw=1,color="red",label="y_pred")
    ax.plot(y_actual,lw=1,color="blue",label="y_actual")
    ax.legend()
    # Web用処理
    canvas = FigureCanvasAgg(fig)
    png_output = BytesIO()
    canvas.print_png(png_output)
    img_data = urllib.parse.quote(png_output.getvalue())
    return img_data


def analyze(rs):
    print('analyze----------------start')
    iris = datasets.load_iris()
    X = iris['data']
    y = iris.target
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=rs)

    model = RandomForestClassifier(n_estimators=20)
    model.fit(X_train, y_train)

    print ("train正解率",model.score(X_train, y_train))
    print ("test正解率",model.score(X_test, y_test))

    #予測データ作成
    y_train_pred = model.predict(X_train)
    x = X_train[:, 0]
    x = list(range(len(y_train_pred)))
    y = y_train_pred.tolist()

    print('accuracy_score: ')
    acc = accuracy_score(y_train, y_train_pred)
    print(acc)

    return y_train, y_train_pred


@app.route("/plot/<func>")
def plot_graph(func='sin'):
    # 分析
    y_train, y_train_pred = analyze(int(func))
    # 画像生成
    img_data = plot_pred_and_actual(y_train, y_train_pred)

    return img_data


@app.route("/")
def index():
    return render_template("index.html", img_data=None)

if __name__ == "__main__":
    app.run(debug=True, port=9999)