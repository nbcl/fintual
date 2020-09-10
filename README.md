# Fintual Portfolio

Stock market & portfolio implementation in pure Python.

## Description

The following project is capable of generating random historical stock price data for a given set of tickers in a Market. Said data can be used to construct stock portfolios from which profit and annualized revenue statistics can be obtained in a given date span. 

```python
NASDAQ = Market(['FB', 'AMZN', 'AAPL', 'NFLX', 'GOOGL'])
internationalPortfolio = Portfolio(['AMZN', 'AAPL'], NASDAQ)
internationalQ1 = internationalPortfolio.profit('2020-01-01', '2020-04-01')

print('International Portfolio Profit for Q1 2020 : ', internationalQ1)

>>> International Portfolio Profit for Q1 2020 :  $4934
```

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.
There are no prerequisites for this implementation.

```python
python main.py
```


## Configuration

Further configuration and assesment can be achieved by trying custom testcases in the main module. The following section is a run-down on how to construct two different financial markets and portfolios.

```python
# Generates two different markets
NASDAQ = Market(['FB', 'AMZN', 'AAPL', 'NFLX', 'GOOGL'])
IPSA = Market(['ENELAM', 'FALABELLA', 'CENCOSUD', 'CHILE', 'CMPC'])

# Creates new portfolios for National and International Markets
internationalPortfolio = Portfolio(['AMZN', 'AAPL'], NASDAQ)
nationalPortfolio = Portfolio(['CHILE', 'FALABELLA', 'ENELAM'], IPSA)
```

Now we can go ahead and recieve the Q1 2020 revenue for each portfolio.

```python
# Calculates profit for Q1 2020 in each portfolio
internationalQ1 = internationalPortfolio.profit('2020-01-01', '2020-04-01')
nationalQ1 = nationalPortfolio.profit('2020-01-01', '2020-04-01')

# Prints results
print('International Portfolio Profit for Q1 2020 : ', internationalQ1)
print('National Portfolio Profit for Q1 2020 : ', nationalQ1)

>>> International Portfolio Profit for Q1 2020 :  4934
>>> National Portfolio Profit for Q1 2020 :  490
```

We can also recieve this information annualized.

```python
# Calculates annualized profit for Q1 2020 in each portfolio
internationalAnnualQ1 = internationalPortfolio.profit('2020-01-01', '2020-04-01', 'ANNUALIZED')
nationalAnnualQ1 = nationalPortfolio.profit('2020-01-01', '2020-04-01', 'ANNUALIZED')

# Prints results
print('International Portfolio Annualized Profit for Q1 2020 : ', 
internationalAnnualQ1)
print('National Portfolio Annualized Profit for Q1 2020 : ', 
nationalAnnualQ1)

>>> International Portfolio Annualized Profit for Q1 2020 :  1.531
>>> National Portfolio Annualized Profit for Q1 2020 :  0.459
```

## Assumptions

Portfolio implementation is constructed under the following assumptions.

* Only built-in libraries are to be used
* Correct input is given on function call 
* Implementation and structure are to be prioritized over data generation
    * Stock prices are generated randomly (APIs / DB are forbidden)


## Comments

Note that historical stock data is randomly generated thus +1000% returns can ocurr.


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
