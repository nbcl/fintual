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

import random
from datetime import datetime, timedelta
from parameters import HISTORICAL_DAYS, DAY_1, MAX_STOCK_PRICE 


class Stock():
    """Fintual -- Stock Class

    Generates and stores random stock prices for a given ticker

    Attributes:
        str ticker : Stock's symbol
        dict prices : Historical price data

    Methods:
        genPrices(self) : Generates historical price data
    """

    def __init__(self, ticker: str):
        """Inits Stock instance with basic attributes and calls genPrices()
        """
        self.ticker = ticker
        self.prices = {}
        self.genPrices()

    def genPrices(self):
        """Generates stock prices in the span of HISTORICAL_DAYS

        Parameters:
            global HISTORICAL_DAYS: Ammount of days in record
        
        Returns:
            none
        """
        for day in range(HISTORICAL_DAYS):  
            self.prices[str(DAY_1 + timedelta(days=day))] = random.randint(
                0, MAX_STOCK_PRICE)  # Assign a random price for each day
