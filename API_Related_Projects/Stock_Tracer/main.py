import time
from datetime import date, timedelta

## STEP 1: Use https://www.alphavantage.co
stock_api = "YOUR API"

stock_params = {
    "function": "DIGITAL_CURRENCY_DAILY",
    "symbol": "BTC",
    "market": "EUR",
    "apikey": stock_api,
}

import requests

url = "https://www.alphavantage.co/query"
r = requests.get(url, params=stock_params)

yesterday = (date.today() - timedelta(days=1))
before_yesterday = (date.today() - timedelta(days=2))
limit = (date.today() - timedelta(days=3))

print(r.json())
data = float(r.json()["Time Series (Digital Currency Daily)"][f"{yesterday}"]["4. close"])
data_2 = float(r.json()["Time Series (Digital Currency Daily)"][f"{before_yesterday}"]["4. close"])

if data - (data / 100 * 5) < data_2 < data + (data / 100 * 5):
    print("coin was stable")
else:
    print("Get news")

## STEP 2: Use https://newsapi.org

news_api = "YOUR API"
news_params = {
    "q": "bitcoin",
    "from": limit,
    "sortBy": "publishedAt",
    "apiKey": news_api,
    "language": "en",
}

from newsapi import NewsApiClient

# Init
newsapi = NewsApiClient(api_key='YOUR API KEY')
#
# /v2/top-headlines
# top_headlines = newsapi.get_top_headlines(q='bitcoin',
#                                           sources='bbc-news,the-verge',
#                                           category='business',
#                                           language='en',
#                                           country='us')

# /v2/top-headlines/sources
sources = newsapi.get_sources()

url = "https://newsapi.org/v2/everything"
n = requests.get(url, params=news_params)


# print(f"Bitcoin {change_dir_pos}{round(float((65000 - 62000) / 62000) * 100, 1)}%")

# print(f"Bitcoin {change_dir_neg}{round(float((6000 - 62000) / 62000) * 100, 1)}%")
# print(f"Headline: {n.json()["articles"][0]["title"]}")
# print(f"Brief: {n.json()["articles"][0]["description"]}")


from twilio.rest import Client

account_sid = 'YOUR ACCOUNT ID'
auth_token = 'YOUR AUTH TOKEN'
client = Client(account_sid, auth_token)

for i in range(0, 3): #you can make list comprehension here
    if n.json()["articles"][i]["title"] != "[Removed]":
        if data - data_2 <= 0:
            change_dir = "🔻"
        else:
            change_dir = "🔺"
            # f"Bitcoin {change_dir_neg}{round(float((data - data_2) / data_2) * 100, 1)}%")

        # if (60000 - 62000) <= 0:
            # print(f"Bitcoin {change_dir_neg}{round(float((60000 - 62000) / 62000) * 100, 1)}%")
            # print(f"Headline: {n.json()["articles"][i]["title"]}.")
            # print(f"Brief: {n.json()["articles"][i]["description"]}.")

        message = client.messages.create(
            from_='whatsapp:+YOUR TWILIO NUMBER',
            body=f"""*Bitcoin:* {change_dir}{round(float((data - data_2) / data_2) * 100, 1)}%\n\n*Headline:* {
                 n.json()["articles"][i]["title"]}.\n\n*Brief:* {n.json()["articles"][i]["description"]}.""",
            to='whatsapp:+YOUR WHATSAPP NUMBER'
        )
        print(message.sid)

        # if (60000 - 62000) >= 0:
        #     print(f"Bitcoin {change_dir_pos}{round(float((60000 - 62000) / 62000) * 100, 1)}%")
        #     print(f"Headline: {n.json()["articles"][i]["title"]}.")
        #     print(f"Brief: {n.json()["articles"][i]["description"]}.")
        #     test code




# Use https://www.twilio.com

