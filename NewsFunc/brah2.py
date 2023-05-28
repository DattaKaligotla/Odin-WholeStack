article = """ 
As investors continually scrutinize the stock market looking for investment opportunities, they keep an eye out for events such as short interest increases. Halliburton (NYSE:HAL) experienced a significant increase in short interest this March, highlighting that investors are uncertain about its future prospects. The trend is likely to be felt in strategic developments as investors continue to weigh their options.

The data available shows that as of March 15th, there was short interest amounting to 24,930,000 shares. This represented an 8% surge from the total of 23,080,000 shares seen on February 28th. Based on average daily volumes of 9,090,000 shares, it follows that the current short-interest ratio is now 2.7 days.

Halliburton has a market cap of $28.61 billion and boasts a P/E ratio of 18.29 and a price-to-earnings-growth ratio of 0.23. Its beta value stands at a high figure of 2.12 with its most recent opening price placed at $31.64 last Friday.

Furthermore, throughout the last year up to March’s end date point measuring trends and performances have shown no conclusive evidence towards predictions for better or worse performances in terms of share pricing by investors.

However remarkable insider activity emerged throughout the opening months of this year; corporate insiders worth .57% sold off over forty thousand shares collectively totaling around one million dollars worth cashed out during Q2 alone.

The business also recently announced a quarterly dividend payment which marked an increase from past payments made in past quarterly earnings reports whereby shareholders were provided with dividends worth $0.12; A report which created much optimism amongst HAL’s long-term supporters signifying developmental growth opportunities by aimed management via growth investments proving potentially fruitful for those invested long term.



In conclusion based on HAL’s data and activity reported throughout Q1 investors are still divided in their opinion of its investment potential. Many taking a speculative approach, this could ultimately have an impact on HAL’s financial outcomes for the coming quarters as well as creating stirrings of uncertainty within the market at large.


Halliburton: Rising to the Top of the Oilfield Services Industry
5d
1m
3m
6m
1y
2y
5y
10y

Halliburton: A Rising Giant in the Oilfield Services Industry

Halliburton, a multinational oilfield services company based in Texas, recently released its earnings results for the first quarter of 2017, and it has analysts buzzing. The firm reported a quarterly revenue of $5.58 billion, up 30.5% on a year-over-year basis. Additionally, Halliburton reported an earnings per share (EPS) of $0.72 for the quarter, which topped the consensus estimate of $0.67 by $0.05.

These strong results indicate that Halliburton is continuing to establish itself as a prominent force in the oilfield services industry. With a return on equity of 26.25% and a net margin of 7.74%, investors are certainly taking notice.



But it’s not just investors who are excited about Halliburton’s potential. Numerous equities research analysts have given glowing reviews of the company and its stock, with StockNews.com recently issuing a “buy” rating on Halliburton.

Benchmark also issued a “buy” rating on the stock back in January and set their price target at $50.00 — indicating that they believe there’s still significant room for growth in the coming months.

HSBC is similarly bullish about Halliburton, increasing their price target from $43.90 to $57.00 after Q1 earnings were released and giving the company another “buy” rating.

In fact, according to Bloomberg.com, one research analyst has assigned only a hold rating to Halliburton while fourteen others have given “buy” ratings and one has assigned it with a strong buy rating — solidifying Wall Street’s faith in this up-and-coming industry powerhouse.

All this leads to an optimistic outlook for Halliburton’s future; sell-side analysts expect that they will post an EPS of 3.09 for this fiscal year alone.

Given Halliburton’s successful Q1 earnings and the positive outlook from analysts, it’s clear that this firm is a rising giant in the oilfield services industry. Investors would be wise to keep an eye on Halliburton as it continues to grow and establish itself as a top player.
"""
import requests
from bs4 import BeautifulSoup

def extract_article_content(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')

            # Find the article element and extract its text
            article = soup.find('article')
            if article:
                paragraphs = article.find_all('p')
                content = ' '.join([p.get_text(strip=True) for p in paragraphs])
                return content
            else:
                print("Could not find the article element.")
                return None
        else:
            print(f"Request failed with status code {response.status_code}")
            return None
    except Exception as e:
        print(f"Error occurred: {e}")
        return None


article = extract_article_content('https://www.nbcnews.com/politics/congress/house-republicans-eye-wednesday-vote-debt-limit-bill-making-changes-rcna81326')
import os
import openai
import wandb
userInfo = ["Flowers"]
import secrets
thing = secrets.choice(userInfo)
userMood = "funny"
readingLevel = "Normal"
openai.api_key = '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'
outputArticle = openai.ChatCompletion.create(
  model="gpt-3.5-turbo", 
  messages = [{"role": "system", "content" : f"You will generate a unique article for the user with paragraphs based on the following article: {article}"},
{"role": "user", "content" : f"when writing the article for me, be sure to intertwine the main topics with {thing}, so it would be an engaging read for me and make it relevant and funny if possible, but do not make up information"},
{"role": "user", "content" : f"I want the tone to be very funny and engaging to read and be sassy and connect the topics to {thing}"},
{"role": "user", "content" : f"I want the reading level to be {readingLevel} and digestable, now based on all the information generate me an article in third or second person for less than 250 words"},
],
  temperature=0.55,
  max_tokens=1800,
  n = 1,
  stop = None
)
outputArticletext = outputArticle['choices'][0]['message']['content']
userTitleGen = "Just Give me an Article title based on the following article:" + outputArticletext + "user reading level: " + readingLevel
outputTitle = openai.ChatCompletion.create(
  model="gpt-3.5-turbo", 
  messages = [{"role": "system", "content" : userTitleGen}]
)
print(outputTitle['choices'][0]['message']['content'])
print("**********************")
print(outputArticletext)

