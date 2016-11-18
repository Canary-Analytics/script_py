from twython import Twython

TWITTER_APP_KEY = 'Gt2qbxi8yElkpWeyYqrZlG8kZ' #supply the appropriate value
TWITTER_APP_KEY_SECRET = 'U74ZyFaKEIdjlZxTiFW7PzxRXlOhsddqzPjbQEWZBoym6le8EM' 
TWITTER_ACCESS_TOKEN = '914939312-Poq0BVjSqW1oyvMh9sBB1603uprwNYgZdYcqImpS'
TWITTER_ACCESS_TOKEN_SECRET = 'ucVf8VDTA3NFV8hc0p4gVCK2JEn9xD8iHQlwpurzUnmhc'

t = Twython(app_key=TWITTER_APP_KEY, 
            app_secret=TWITTER_APP_KEY_SECRET, 
            oauth_token=TWITTER_ACCESS_TOKEN, 
            oauth_token_secret=TWITTER_ACCESS_TOKEN_SECRET)
count = 0 #Chivato
outfile = open('tweets.txt', 'a') # Indicamos el valor 'w'.
twitter = t
search = t.search(q = '#CanaryIsland', count = 20)
tweets = search['statuses']
for tweet in tweets:
	estado = tweet['text']
	estado = estado.encode('ascii', 'ignore').decode('ascii')
	outfile.write(estado + '\n')
	print tweet['text']
	print ""
	count = count + 1

#print search_results['statuses']
print count 


outfile.close()
