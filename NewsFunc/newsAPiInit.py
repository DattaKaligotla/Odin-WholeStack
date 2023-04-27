from newsapi import NewsApiClient

# Store our API Information here for a layer of abstraction, we really shouldn't need it
# cuz were keeping this jaunt seperate 
def extract_urls(response):
    urls = []
    for article in response['articles']:
        urls.append(article['url'])
    return urls
class NewsInit:
    def __init__(self):
        self.apiKey = ''
        self.fromDate = ''
        self.toDate = ''
    def changeToDate(self,toDate):
        self.toDate = toDate
    def changeFromDate(self,fromDate):
        self.fromDate = fromDate
    def changeKey(self,key):
        self.apiKey = key
    def getPolitical(self):
        newsapi = NewsApiClient(api_key=self.apiKey)

        all_articles = newsapi.get_everything(q='politics',
                                       from_param=self.fromDate,
                                      to=self.toDate,
                                      language='en',
                                      #sources= 'axios,cbc-news,google-news,abc-news,associated-press,fox-news,usa-today,the-verge,business-insider',
                                      sources= 'cnn,the-verge,reuters,abc-news,fox-news,usa-today,vice-news,nbc-news',
                                      sort_by='relevancy',)
        return extract_urls(all_articles)
    def getTech(self):
        newsapi = NewsApiClient(api_key=self.apiKey)

        all_articles = newsapi.get_everything(q='technology',
                                       from_param=self.fromDate,
                                      to=self.toDate,
                                      language='en',
                                      sources= 'techcrunch,the-verge,ars-technica,TechRadar,cnn,crypto-coins-news,four-four-two,fox-news,hacker-news,nbc-news,cnn,abc-news,fox-news,nbc-news',
                                      sort_by='relevancy',)
        return extract_urls(all_articles)
    def getBus(self):
        newsapi = NewsApiClient(api_key=self.apiKey)

        all_articles = newsapi.get_everything(q='business',
                                       from_param=self.fromDate,
                                      to=self.toDate,
                                      language='en',
                                      sources= 'the-washington-post,reuters,the-verge,four-four-two,fox-news,cnn,nbc-news',
                                      sort_by='relevancy',)
        return extract_urls(all_articles)
    
    def getFina(self):
            newsapi = NewsApiClient(api_key=self.apiKey)

            all_articles = newsapi.get_everything(q='financial',
                                        from_param=self.fromDate,
                                        to=self.toDate,
                                        language='en',
                                        sources= 'the-washington-post,reuters,the-verge,four-four-two,fox-news,cnn,nbc-news',
                                        sort_by='relevancy',)
            return extract_urls(all_articles)
    def getSports(self):
        newsapi = NewsApiClient(api_key=self.apiKey)

        all_articles = newsapi.get_everything(q='sports',
                                       from_param=self.fromDate,
                                      to=self.toDate,
                                      language='en',
                                      sources= 'bleacher-report,the-verge,espn,four-four-two,nfl-news',
                                      sort_by='relevancy',)
        return extract_urls(all_articles)

    def getEnt(self):
        newsapi = NewsApiClient(api_key=self.apiKey)

        all_articles = newsapi.get_everything(q='entertainment',
                                       from_param=self.fromDate,
                                      to=self.toDate,
                                      language='en',
                                      sources= 'mtv-news,the-verge,cbs-news,fox-news,mashable,cnn',
                                      sort_by='relevancy',)
        return extract_urls(all_articles)
    def getWorld(self):
        newsapi = NewsApiClient(api_key=self.apiKey)

        all_articles = newsapi.get_everything(q='world',
                                       from_param=self.fromDate,
                                      to=self.toDate,
                                      language='en',
                                      sources= 'cnn,abc-news,the-verge,fox-news,nbc-news',
                                      sort_by='relevancy',)
        return extract_urls(all_articles)
    

    
    


