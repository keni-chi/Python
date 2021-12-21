# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt


class PltUtil:
    def __init__(self):
        pass

    @classmethod
    def plot_pred_and_actual(cls, file_path, y_pred, y_actual):
        fig = plt.figure(figsize=(14,7))
        ax = fig.add_subplot(111)
        ax.scatter(2,2,color="white")
        ax.plot(y_pred,lw=1,color="red",label="y_pred")
        ax.plot(y_actual,lw=1,color="blue",label="y_actual")
        ax.legend()
        plt.savefig(file_path)