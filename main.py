import yfinance as yf
import pandas as pd
from datetime import datetime
from datetime import timedelta
import time
from stockData import get_current_price, get_price_history
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import keyboard

cont = True
while(cont):
    stockSym = input("Please Enter a stock's SYMBOL Ex(AAPL): ")
    print(get_current_price(stockSym))
    keyInput = input("Press Q to Quit or C to Continue: ")
    if(keyInput == 'q'):
        cont = False
    elif(keyInput == 'c'):
        cont = True




