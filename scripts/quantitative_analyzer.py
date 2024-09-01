import talib as ta
import pynance as pn

def moving_average(data, window_size):
    return ta.SMA(data, timeperiod=window_size)

def technical_indicators(data):
    # Calculate various technical indicators
    data['SMA'] = moving_average(data['Close'], 20)
    data['RSI'] = ta.RSI(data['Close'], timeperiod=14)
    data['EMA'] = ta.EMA(data['Close'], timeperiod=20)
    macd, macd_signal, _ = ta.MACD(data['Close'])
    data['MACD'] = macd
    data['MACD_Signal'] = macd_signal
    # Add more indicators as needed
    return data
    
