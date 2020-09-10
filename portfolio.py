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
from datetime import datetime, timedelta


class Portfolio():
    """Fintual -- Portfolio Class

    Stores multiple stocks from a Market and calculates profit

    Attributes:
        list stocks : The stock tickers the portfolio has aquired
        Market market : The market API where stock prices is taken from

    Methods:
        profit(self, startDate, endDate) : Returns the profit between two 
        given dates
        profit(self, startDate, endDate, annualized) : Returns annualized 
        profit
    """

    def __init__(self, stocks: list(), market: Market):
        """Inits Portfolio instance with basic stocks and market attributes
        """
        self.stocks = stocks
        self.market = market

    def profit(self, startDate: str, endDate: str, annualized = False):
        """Provides profit and annualized profit for given date span

        Parameters:
            str startDate : First day of the span
            str endDate : Last day of the span
            str annualized : Defaults to False, if True provides annualized 
            profit
        
        Returns:
            int/float profit : Profit from portfolio in given date
            span under desired parameteres
        """
        if not annualized:  # Regular profit function
            profit = 0
            for stockTicker in self.stocks:
                buy = self.market.stocks[stockTicker].prices[startDate]
                sell = self.market.stocks[stockTicker].prices[endDate]
                profit += sell - buy  # Basic profit function
            if profit <= 0:
                print('Yikes! Next time use Fintual :S') # Haha!
            return profit
        else:  # Annualized profit function
            # Obtains the relative revenue
            initialCapital = 0
            finalCapital = 0
            for stockTicker in self.stocks:
                initialCapital += self.market.stocks[stockTicker].prices[startDate]
                finalCapital += self.market.stocks[stockTicker].prices[endDate]
            revenue = (finalCapital - 
            initialCapital)  / initialCapital  # == Relative revenue
            # Obtains the float fraction of years between two dates
            startDate = datetime.strptime(startDate, '%Y-%m-%d')
            endDate = datetime.strptime(endDate, '%Y-%m-%d')
            years = endDate - startDate
            yearFraction = int(years.days) / 365 # == Relative time
            # Obtains the annualized revenue
            annualizedRevenue = (((1 + revenue)**(1 / yearFraction)) - 1) 
            return  round(annualizedRevenue, 2)
