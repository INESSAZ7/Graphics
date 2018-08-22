import matplotlib.pyplot as plt
from fileManager import *
import sklearn.linear_model as lm
import pandas as pd
import numpy as np








def myLinearRegression(x ,y):
    A = np.vstack([x, np.ones(len(x))]).T
    k,b = np.linalg.lstsq(A, y,rcond = None)[0]
    return k,b


def myShowLinearRegression(k, b, x , y ):
    plt.scatter(x, y)
    plt.plot(x, k * x + b, 'r', label='Аппроксимационная прямая')
    plt.legend()
    plt.show()
    print("k = "+"%.6f" % k)
    print("b = "+"%.6f" % b)

def graphic():
    x = vozvrat_znach_x_from_file()
    y = vozvrat_znach_y_from_file()
    xerr = vozvrat_znach_xerr_from_file()
    yerr = vozvrat_znach_yerr_from_file()
    text_ox = text_ox_file()
    plt.title('График', color='blue', fontsize=18)
    plt.xlabel(text_ox, color='crimson')
    plt.ylabel('Ось y')
    plt.grid()
    plt.errorbar(x, y, xerr=xerr, yerr=yerr, fmt='o', ecolor='red')
    k, b = myLinearRegression(x, y)
    myShowLinearRegression(k, b, x, y)















'''
#МашинЛернинг)
def my_LinearRegression():
    X = np.array([[1],[2],[3],[4]])
    Y = np.array([1,2,3,4])
    xerr = vozvrat_znach_xerr_from_file()
    yerr = vozvrat_znach_yerr_from_file()

    plt.errorbar(X, Y, xerr=xerr, yerr=yerr, fmt='o', ecolor='red')

    skm = lm.LinearRegression()
    skm.fit(X, Y)
    print(skm.intercept_, skm.coef_)
    xfit = np.linspace(-1, 110)
    Xfit = xfit[:, np.newaxis]
    yfit = skm.predict(Xfit)
    plt.scatter(X,Y)
    plt.plot(xfit, yfit)
    plt.show()
'''



