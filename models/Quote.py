class Quote:


    def __init__(self, open, close, high, low, vol):
        self.open = open
        self.close = close
        self.high = high
        self.low = low
        self.vol = vol
        self.change = 0

    def calc_change(self):
        self.change = (self.close - self.open) * 100 / self.open
        self.change = round(self.change, 2)

    def get_change(self):
        if self.change > 0:
            color = "green"
        else:
            color = "red"
        return self.change, color

    def create_quote(self):
        text = (f"Open: {self.open} | Close: {self.close} | High/Low: {self.high}/{self.low} |"
                f"Vol {self.vol}")
        return text

    def create_fav_quote(self, symbol):
        text = f"{symbol}: {self.close} | {self.change}% | {self.high}/{self.low}"
        return text


