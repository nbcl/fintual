"""MIT License

Copyright (c) 2020 nbcl

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from market import Market
from portfolio import Portfolio

# Generates two different markets
NASDAQ = Market(['FB', 'AMZN', 'AAPL', 'NFLX', 'GOOGL'])
IPSA = Market(['ENELAM', 'FALABELLA', 'CENCOSUD', 'CHILE', 'CMPC'])

# Creates new portafolios for National and International Markets
internationalPortfolio = Portfolio(['AMZN', 'AAPL'], NASDAQ)
nationalPortfolio = Portfolio(['CHILE', 'FALABELLA', 'ENELAM'], IPSA)

# Calculates profit for Q1 2020 in each portfolio
internationalQ1 = internationalPortfolio.profit('2020-01-01', '2020-04-01')
nationalQ1 = nationalPortfolio.profit('2020-01-01', '2020-04-01')

# Prints results
print('International Portfolio Profit for Q1 2020 : ', internationalQ1)
print('National Portfolio Profit for Q1 2020 : ', nationalQ1)

# Calculates annualized profit for Q1 2020 in each portfolio
internationalAnnualQ1 = internationalPortfolio.profit('2020-01-01', '2020-04-01', 'ANNUALIZED')
nationalAnnualQ1 = nationalPortfolio.profit('2020-01-01', '2020-04-01', 'ANNUALIZED')

# Prints results
print('International Portfolio Annualized Profit for Q1 2020 : ', 
internationalAnnualQ1)
print('National Portfolio Annualized Profit for Q1 2020 : ', 
nationalAnnualQ1)
