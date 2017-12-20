#!/usr/bin/python
import praw
import nltk

reddit = praw.Reddit('MchanBot')

subreddit = reddit.subreddit("mchanbot")

wholeBi = []
x = ''

f = open('Bigrams.txt','r')
bigrams = f.read().strip().split('\n')
g = open('UserWatchlist.txt','r+')
userWarning = g.read().strip().split()
h = open('CommentPermalinks.txt','r+')

#scans through reddit comments that the bot retrieves
ratio = 0.0
for submission in subreddit.hot(limit=30):
        submission.comments.replace_more(limit=0)
        for comment in submission.comments.list():
            if all(ord(c) < 128 for c in comment.body):
                x = str(comment.body)
                x = x.translate(str.maketrans('','', '!?":;$%*(\'_)#/[.,]\-{}')) #removes any characters that might crash the program

                #retrives the bigrams of the comment
                tokens = nltk.word_tokenize(x)
                bgs = nltk.bigrams(tokens)
                fdist = nltk.FreqDist(bgs)
                count = 0

                #compares the comment to the learning data of harmful and non-harmful messages
                for k,v in fdist.items():
                    wholeBi += [str(k),v]
                    if str(k) in bigrams:
                        if float(bigrams[bigrams.index(str(k))+2]) > ratio: 
                            ratio = float(bigrams[bigrams.index(str(k))+2])

                        #if the comment is deemed to be harmful
                        if ratio > 0.5: #and float(bigrams[bigrams.index(str(k))+1]) > 1:
                            h.write(str(comment.permalink)+'\n')
g.close()
g = open('UserWatchlist.txt', 'w')

#writes updated user information to a file                        
for line in userWarning:
    g.write(str(line)+'\n')

f.close()
g.close()
h.close()

