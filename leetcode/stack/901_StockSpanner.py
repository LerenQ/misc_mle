class StockSpanner:
    '''
    Design an algorithm that collects daily price quotes 
    for some stock and returns the span of that stock's price for the current day.

    The span of the stock's price today is defined as the maximum number of consecutive days 
    (starting from today and going backward) 
    for which the stock price was less than or equal to today's price.

    '''
    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        cnt = 1
        while self.stack and (self.stack[-1][0] <= price):
            cnt += self.stack.pop()[1]
        self.stack.append((price, cnt))
        return cnt


# Your StockSpanner object will be instantiated and called as such:
obj = StockSpanner()

