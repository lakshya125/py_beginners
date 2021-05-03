#http://stackoverflow.com/questions/11845055/predicting-from-previous-datevalue-data
import matplotlib.pyplot as plt
import pandas
import MySQLdb
import matplotlib.pyplot as plt
from statistics import mean
import numpy as np
from sklearn.utils import check_array


y_trues = [3, -0.5, 2, 7]
y_preds = [2.5, -0.3, 2, 8]

def holt_alg(h, y_last, y_pred, T_pred, alpha, beta):
    pred_y_new = alpha * y_last + (1-alpha) * (y_pred + T_pred * h)
    pred_T_new = beta * (pred_y_new - y_pred)/h + (1-beta)*T_pred
    return (pred_y_new, pred_T_new)

def smoothing(t, y, alpha, beta):
    # initialization using the first two observations
    pred_y = y[1]
    pred_T = (y[1] - y[0])/(t[1]-t[0])
    y_hat = [y[0], y[1]]
    # next unit time point
    t.append(t[-1]+1)
    for i in range(2, len(t)):
        h = t[i] - t[i-1]
        pred_y, pred_T = holt_alg(h, y[i-1], pred_y, pred_T, alpha, beta)
        y_hat.append(pred_y)
    return y_hat

