#name: Zhiyi Ma
#unique name: zhiyima
#umid: 48014433

import nltk
import tweepy
import json
import sys
import csv
from collections import Counter
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize

consumer_key = "j5Xm5Zn75XkWCdp7NbzFi9Hny"
consumer_secret = "Oar9INHaGnQnT1crouN9TR8xgyi3Uff6y1mlMhOdvNM2ohNw1L"
access_token = "2765547289-2jbZQpgRzMaogTL4x9kjkod4PUQbLY71VyzMwPx"
access_token_secret = "cJ7I9HWVgaCwGPJx0qWfCIGdmZKfRdqZfK02fTFjin5CK"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)  
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth) 

user_name = sys.argv[1]
tweet_num = sys.argv[2]

favorite_num = 0
retweet_num = 0
tweet_ls = []
original_tweet_ls = []
retweet_ls = []

for tweet in tweepy.Cursor(api.user_timeline, id = user_name, tweet_mode = "extended").items(int(tweet_num)):
	box = getattr(tweet,'retweeted_status', None)
	if box is None:
		favorite_num += tweet.favorite_count
		retweet_num += tweet.retweet_count
		original_tweet_ls.append(tweet.full_text)
	
stop_word_ls = ["http", "https", "RT"]
real_word_ls = []

for tweet in original_tweet_ls:
	sliced_text = word_tokenize(tweet)

	for word in sliced_text:
		if word[0].isalpha() and word not in stop_word_ls:
			real_word_ls.append(word)

tag_ls = nltk.pos_tag(real_word_ls)
verb_ls = []
noun_ls =[]
adj_ls = []

for word,tag in tag_ls:
	if tag in ('VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ'):
		verb_ls.append((word,tag))
	if tag in ('NN' ,'NNS', 'NNP', 'NNPS'):
		noun_ls.append((word,tag))
	if tag in ('JJ', 'JJR', 'JJS'):
		adj_ls.append((word,tag))


verb_counts = Counter(word for word,tag in verb_ls)
verb_counts = sorted(verb_counts.items(), key=lambda x: (-x[1],x[0].casefold()), reverse=False)
verb_list = []
for verb, count in verb_counts[0:5]:
	count = str(count)
	verb = verb + "(" + count + ")"
	verb_list.append(verb)
verbs = " ".join(verb_list)

noun_counts = Counter(word for word,tag in noun_ls)
noun_counts = sorted(noun_counts.items(), key=lambda x: (-x[1],x[0].casefold()), reverse=False)
noun_list = []
for noun, count in noun_counts[0:5]:
	count = str(count)
	noun = noun + "(" + count + ")"
	noun_list.append(noun)
nouns = " ".join(noun_list)

adj_counts = Counter(word for word,tag in adj_ls)
adj_counts = sorted(adj_counts.items(), key=lambda x: (-x[1],x[0].casefold()), reverse=False)
adj_list = []
for adj, count in adj_counts[0:5]:
	count = str(count)
	adj = adj + "(" + count + ")"
	adj_list.append(adj)
adjs = " ".join(adj_list)

print("USER: ",user_name)
print("TWEETS ANALYZED: ", tweet_num)

print("VERBS: ", verbs)
print("NOUNS: ", nouns)
print("ADJECTIVES: ", adjs)
print("ORIGINAL TWEETS: ", len(original_tweet_ls))
print("TIMES FAVORITED (ORIGINAL TWEETS ONLY): ", favorite_num)
print("TIMES RETWEETED (ORIGINAL TWEETS ONLY): ", retweet_num)

myFile = open('/Users/mazhiyi/Documents/GitHub/si-507-waiver-assignment-f18-mzy11mzy/noun_data.csv', 'w')
#myFile = open('noun_data.csv', 'w')

with myFile as csv_file:
	csv_output = csv.writer(csv_file)
	csv_output.writerow(['Noun', 'Number'])
	csv_output.writerows(noun_counts[0:5])