import numpy as np


class Asset:
    def __init__(self, ticker:str, slippage=0, fee=0, max_leverage=1, min_amount=1e-7, can_short=True):
        self.ticker = ticker
        self.slippage = slippage / 100
        self.fee = fee / 100
        self.max_leverage = max_leverage
        self.margin_percentage = 1 / max_leverage
        self.min_amount = min_amount
        self.can_short = can_short


class Stock(Asset):
    def __init__(self, *args, **kwargs):
        super(Stock, self).__init__(*args, **kwargs)


class Futures(Asset):
    def __init__(self, *args, **kwargs):
        super(Futures, self).__init__(*args, **kwargs, can_short=True)


class Option(Asset):
    def __init__(self, *args, **kwargs):
        super(Option, self).__init__(*args, **kwargs, can_short=True)


