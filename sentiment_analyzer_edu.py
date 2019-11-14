'''
Importing modules
'''
import tweepy
from textblob import TextBlob

'''
Declaring variables to store the keys from Twitter API
'''
consumer_key = '<your_key_here>'
consumer_key_secret = '<your_key_here>'
access_token = '<your_key_here>'
access_token_secret = '<your_key_here>'

'''
Creating the connection using the API
'''
auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

'''
Searching for any term
See handling erros to add exception in case the users don't pass the correct argument. Talk about this with the guys on wednesday.
'''

search_term = input('What do you wanna search for? ')
num_of_terms = int(input('How many terms? '))
people_tweets = tweepy.Cursor(api.search,
                              since = "2019-11-01",
                              #until = "2019-11-14",
                              q = search_term, 
                              lang = "en").items(num_of_terms)

positive = 0
negative = 0
neutral = 0

for tweet in people_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    if analysis.sentiment[0] > 0.00:
        print('Positive')
        positive += 1
    elif analysis.sentiment[0] < 0.00:
        print('Negative')
        negative += 1
    else:
        print('Neutral')
        neutral += 1

print()
print('-=' * 3, 'TOTALS', '-=' * 3)
print('Total Positives:', positive)
print()
print('Total Negatives:', negative)
print()
print('Total Neutrals:', neutral)
print()

'''
Percentages
Formula: (part / whole) * 100
'''

print('-=' * 3, 'PERCENTAGE', '-=' * 3)
print(int((positive / num_of_terms) * 100), '% Positives')
print()
print(int((negative / num_of_terms) * 100), '% Negatives')
print()
print(int((neutral / num_of_terms) * 100), '% Neturals')
print()

'''
Create a function to return a percentage charts here. 
'''
