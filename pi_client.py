from pageindex import PageIndexClient

# BaseClient class to initialize the PageIndexClient with the API key
class BaseClient():
    def __init__(self, api_key):
        self.client = PageIndexClient(api_key)
        print(f"BaseClient initialized with API key: {self.client}")