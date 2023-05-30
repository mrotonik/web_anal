import tweepy


consumer_key = '-'
consumer_secret = '-'
access_token = '1618542077083631616--'
access_token_secret = '-'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)


api = tweepy.API(auth)

# Налаштуйте ім'я користувача та кількість твітів
username = 'HromadskeUA'
count = 10

# Здійснюємо запит до Twitter API
tweets = api.user_timeline(screen_name=username, count=count)


for tweet in tweets:
    print(tweet.text)
