# singleton pattern

class Configuration:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Configuration, cls).__new__(cls)
            cls._instance.config = {}
        return cls._instance

# Usage:
# config1 = Configuration()
# config2 = Configuration()
# config1.config['API_KEY'] = '123456'
# print(config2.config['API_KEY'])  # Output will be '123456'
