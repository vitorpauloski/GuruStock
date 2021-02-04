# GuruStock

GuruStock is a Python package for extracting market data from Guru app.

## Basic usage

```python
>>> import guru
>>> session = guru.Session('YOUR_TOKEN')
>>> tickers = ['DOLH21', 'VVAR3', 'IBOV']
>>> session.getMarketData(tickers)
[{'ticker': 'DOLH21', 'name': 'Dolar Comercial Futuro', 'close': 5350, 'price': 5411, 'variation_percent': 1.14}, {'ticker': 'VVAR3', 'name': 'Via Varejo', 'close': 15.08, 'price': 15.19, 'variation_percent': 0.73}, {'ticker': 'IBOV', 'name': 'Ibovespa', 'close': 119724.72, 'price': 119448.51, 'variation_percent': -0.23}]
```
