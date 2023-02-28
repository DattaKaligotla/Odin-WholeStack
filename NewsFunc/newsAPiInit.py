from newsapi import NewsApiClient

# Store our API Information here for a layer of abstraction, we really shouldn't need it
# cuz were keeping this jaunt seperate 

class NewsInit:
    def __init__(self):
        self.apiKey = NewsApiClient(api_key='3f3c1d3e1e9440f1bd3931b47b120f81')
    def getKey(self):
        return self.apiKey


