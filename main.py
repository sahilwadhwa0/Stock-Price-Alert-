import requests
from twilio.rest import Client

account_sid = "XXXXXXXXXXXXXXX"  # your account sid id of twilio.
auth_token = "XXXXXXXXXXXXXXX"  # your authentication token of twilio.

stock_data_headers = {
	"X-RapidAPI-Key": "XXXXXXXXXXXXXXXXXXXX",  # API key for stock prize data.
	"X-RapidAPI-Host": "realstonks.p.rapidapi.com",
}

news_parameters = {
    "q": "TSLA",
    "sortBy": "popularity",
    "pageSize": "1",
    "apiKey": "XXXXXXXXXXXXXXXXXX"  # API key for stock news data.
}

# ----------------------------stock prize--------------------------------
stock_prize_url = "https://realstonks.p.rapidapi.com/TSLA"
stock_response = requests.request("GET", stock_prize_url, headers=stock_data_headers)
stock_response.raise_for_status()
diff_percentage = stock_response.json()["change_percentage"]


# ---------------------stock news-----------------------------------
news_url = "https://newsapi.org/v2/everything"
news_response = requests.get(url=news_url, params=news_parameters)
news_response.raise_for_status()

news_data = news_response.json()["articles"]

# using list comprehension in nested dictionary we are adding whole string to list by also formatting it.
tittle_news = [f"Tittle: {item['title']}\n Description: {item['description']}" for item in news_data]

# ------------------------------sending message----------------------------
if diff_percentage > 1 or diff_percentage < -1:
    for news in tittle_news:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body= news,
            from_="twilio no",
            to="verified no"
        )

