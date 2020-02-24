import essential

TWITTER_TWEETS_SEARCH = 'https://api.twitter.com/1.1/search/tweets.json'

text = input('Enter a search query: ')
if len(text) > 500:
    text = text[:501]
data = essential.search_tweet(text, TWITTER_TWEETS_SEARCH)
essential.json_navigate(data)
