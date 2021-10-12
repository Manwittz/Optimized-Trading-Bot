# strategy pattern

class SignalStrategy:
    def generate_signal(self, data):
        pass

class MovingAverageStrategy(SignalStrategy):
    def generate_signal(self, data):
        return 'Buy' if data['short_ma'] > data['long_ma'] else 'Sell'

class SignalContext:
    def __init__(self, strategy):
        self._strategy = strategy

    def set_strategy(self, strategy):
        self._strategy = strategy

    def generate_signal(self, data):
        return self._strategy.generate_signal(data)

# Usage:
# context = SignalContext(MovingAverageStrategy())
# signal = context.generate_signal({'short_ma': 50, 'long_ma': 40})
