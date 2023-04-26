from newsapi import NewsApiClient

# Init
newsapi = NewsApiClient(api_key='3f3c1d3e1e9440f1bd3931b47b120f81')



# /v2/everything
all_articles = newsapi.get_everything(q='technology',
                                       from_param='2023-04-13',
                                      to='2023-04-24',
                                      language='en',
                                      #sources= 'axios,cbc-news,google-news,abc-news,associated-press,fox-news,usa-today,the-verge,business-insider',
                                      sources= 'techcrunch,ars-technica,axios,cnn,crypto-coins-news,fox-news,nbc-news',
                                      sort_by='relevancy',)
text_file = open("sample1.txt", "w")

import json
def extract_urls(response):
    urls = []
    for article in response['articles']:
        urls.append(article['url'])
    return urls

n = text_file.write(str(extract_urls(all_articles)))

# /v2/top-headlines/so)
#print(str(extract_urls(str(all_articles))))
#n = text_file.write(str(newsapi.get_sources()))
text_file.close()
