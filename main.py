#from getStockData import *
from flask import Flask, render_template 
import matplotlib.pyplot as plt
from io import BytesIO
import base64

app = Flask(__name__)

def get_stock_data(symbol, start_date, end_date):
    data = yf.download(symbol, start=start_date, end=end_date)
    return data['Close']

def plot_stock_graph(symbol, start_date, end_date):
    data = get_stock_data('aapl', '2024-01-01', '2024-01-11')

    plt.figure(figsize=(10, 6))
    plt.plot(data.index, data, label=symbol)
    plt.title(f'Stock Price of {symbol}')
    plt.xlabel('Date')
    plt.ylabel('Closing Price')
    plt.legend()
    
    # Save the plot to a BytesIO object
    img_io = BytesIO()
    plt.savefig(img_io, format='png')
    img_io.seek(0)
    
    # Encode the image to base64 for HTML display
    img_base64 = base64.b64encode(img_io.getvalue()).decode('utf-8')
    
    plt.close()  # Close the plot to free up resources
    
    return img_base64

@app.route('/')
def index():
    symbol = 'AAPL'  # Replace with your desired stock symbol
    start_date = '2024-01-01'  # Replace with your desired start date
    end_date = '2024-01-11'    # Replace with your desired end date

    graph_image = plot_stock_graph(symbol, start_date, end_date)
    
    return render_template('index.html', graph_image=graph_image)

app.run(debug=True)