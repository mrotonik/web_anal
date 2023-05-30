import smtplib
import tweepy

# Вкажіть свої ключі та токени доступу
consumer_key = '-'
consumer_secret = '-'
access_token = '--NdrZM6lsET1LZzHYqy96oFLyOSrdnd'
access_token_secret = '-'

# Автентифікація
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Створіть об'єкт API
api = tweepy.API(auth)

# Налаштуйте ім'я користувача та кількість твітів
username = 'HromadskeUA'
count = 10

# Здійснюємо запит до Twitter API
tweets = api.user_timeline(screen_name=username, count=count)
# Налаштуйте ключове слово
keyword = 'your-keyword'

# Налаштуйте сервер SMTP та вхідні дані
smtp_server = 'your-smtp-server'
smtp_port = 'your-smtp-port'
smtp_username = 'your-smtp-username'
smtp_password = 'your-smtp-password'

# Налаштуйте адресу електронної пошти для надсилання сповіщень
alert_email = 'your-email@example.com'

# Перевірте кожен твіт на наявність ключового слова та надішліть сповіщення
for tweet in tweets:
    if keyword in tweet.text:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.login(smtp_username, smtp_password)
            server.sendmail(smtp_username, alert_email, f'Keyword found in tweet: {tweet.text}')